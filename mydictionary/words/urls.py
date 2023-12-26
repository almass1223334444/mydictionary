from django.urls import path
from .views import HomePageView, WordsListView, AddWordView

urlpatterns = [
    path('home/', HomePageView.as_view(), name='home'),
    path('words_list/', WordsListView.as_view(), name='words_list'),
    path('add_word/', AddWordView.as_view(), name='add_word'),
]
