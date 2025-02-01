from django.http import JsonResponse
from yourapp.models import FAQ

def get_faqs(request):
    lang = request.GET.get('lang', 'en')  # Default to 'en' if no language is specified
    faqs = FAQ.objects.filter(language=lang)
    faq_data = [{"question": faq.question, "answer": faq.answer} for faq in faqs]
    return JsonResponse(faq_data, safe=False)
