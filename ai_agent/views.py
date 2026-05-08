from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .agent import run_agent


def home(request):
    return render(request, "ai_agent/chat.html")


def chat_page(request):
    """Chat UI দেখাবে"""
    return render(request, 'ai_agent/chat.html')


@csrf_exempt
def chat_api(request):
    """Agent-কে message পাঠাবে, response নেবে"""
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        if not user_message:
            return JsonResponse({"error": "Message দাও"}, status=400)

        response = run_agent(user_message)
        return JsonResponse({"reply": response})

    return JsonResponse({"error": "POST method use কর"}, status=405)