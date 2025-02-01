from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator, LANGUAGES

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def get_translated_question(self, lang='en'):
        language_mapping = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return language_mapping.get(lang, self.question)

    def get_translated_answer(self, lang='en'):
        language_mapping = {
            'hi': self.answer_hi,
            'bn': self.answer_bn,
        }
        return language_mapping.get(lang, self.answer)

    def save(self, *args, **kwargs):
        translator = Translator()
        try:
            if not self.question_hi:
                self.question_hi = translator.translate(self.question, src='en', dest='hi').text
            if not self.question_bn:
                self.question_bn = translator.translate(self.question, src='en', dest='bn').text
            if not self.answer_hi:
                self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
            if not self.answer_bn:
                self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
        except Exception as e:
            print(f"Error during translation: {e}")  # You can log this error if needed
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
