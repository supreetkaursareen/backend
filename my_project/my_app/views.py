from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from my_app.models import FAQ

# my_app/views.py
from django.http import HttpResponse  # Add this import

def home(request):
    return HttpResponse("Welcome to the Home Page!")

@api_view(['GET'])
def get_faqs(request):
    lang = request.GET.get('lang', 'en')  # Default to 'en' if lang is not provided
    faqs = FAQ.objects.all()

    faqs_data = []
    for faq in faqs:
        faqs_data.append({
            'question': faq.get_translated_question(lang),
            'answer': faq.get_translated_answer(lang),
        })

    return Response(faqs_data, status=status.HTTP_200_OK)
