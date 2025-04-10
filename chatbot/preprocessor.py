import pandas as pd
import re
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_DATA_PATH = os.path.join(BASE_DIR, "data", "Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv")
CLEANED_DATA_PATH = os.path.join(BASE_DIR, "data", "chat_data_cleaned.csv")

def clean_text(text):
    text = str(text).lower().strip()
    text = re.sub(r"\{.*?\}", "", text)    
    text = re.sub(r"[{}]", "", text)      
    text = re.sub(r"\s+", " ", text)       
    return text

if not os.path.exists(SOURCE_DATA_PATH):
    raise FileNotFoundError(f"Source dataset not found at {SOURCE_DATA_PATH}")

try:
    df = pd.read_csv(SOURCE_DATA_PATH)
except pd.errors.EmptyDataError:
    raise ValueError(f"Source dataset at {SOURCE_DATA_PATH} is empty or malformed!")


required_columns = ["instruction", "response"]
if not all(col in df.columns for col in required_columns):
    raise ValueError(f"Missing required columns: {required_columns}")

if df.empty:
    raise ValueError("Dataset is empty!")


df["instruction"] = df["instruction"].apply(clean_text)
df["response"] = df["response"].apply(clean_text)
df["text"] = df["instruction"] + " " + df["response"]

os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)
df.to_csv(CLEANED_DATA_PATH, index=False)

if not os.path.exists(CLEANED_DATA_PATH):
    raise FileNotFoundError("Cleaned dataset save failed!")
if pd.read_csv(CLEANED_DATA_PATH).empty:
    raise ValueError("Cleaned dataset is empty!")

print(f" Cleaned dataset saved to {CLEANED_DATA_PATH} with {len(df)} rows")
