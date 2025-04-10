from django.shortcuts import render
from django.http import JsonResponse
from chat.chatbot_service import get_response

def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = get_response(user_input)
        return JsonResponse({'response': response})
    return render(request, 'chat/index.html')