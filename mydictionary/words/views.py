from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView
from .forms import WordForm
from .models import Word

class HomePageView(TemplateView):
    template_name = 'home.html'

class WordsListView(ListView):
    model = Word
    template_name = 'words_list.html'
    context_object_name = 'words'

class AddWordView(FormView):
    template_name = 'add_word.html'
    form_class = WordForm
    success_url = '/home/'

    def form_valid(self, form):
            # Сохраняем слово в базе данных
        word_instance = form.save()

            # Записываем слова в файл
        with open("C:/Users/almas/Desktop/django/mydictionary/wordlist.txt", "a", encoding="utf-8") as file:
            file.write(f"{word_instance.word1}-{word_instance.word2}\n")

            # Добавим отладочный вывод
        print(f"Added to file: {word_instance.word1}-{word_instance.word2}")

        return super().form_valid(form)





from django.shortcuts import render

# Create your views here.
