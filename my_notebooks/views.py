from django.shortcuts import render, get_object_or_404
from .models import Topic, Entry
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.


def index(request):
    # Домашняя страница my_notebook
    return render(request, 'my_notebook/index.html')


def topics(request):
    topic = Topic.objects.order_by('date_added')
    context = {'topics': topic}
    return render(request, 'my_notebook/topics.html', context)


def entries(request):
    entry = Entry.objects.order_by('date_added')
    context = {'entries': entry}
    return render(request, 'my_notebook/entries.html', context)


def notes(request, note_number: int):
    # Динамическая страница с записями
    note = Entry.objects.all()
    each_note = get_object_or_404(Entry, id=note_number)
    context = {'note_context': each_note}
    return render(request, 'my_notebook/entry.html', context)


language_dict = [
    'pascal', 'python', 'java', 'javascript', 'c', 'c++', 'php', 'kotlin', 'swift', 'go', 'r', 'dart'
]


def language_list(request):
    context = {'language_render': language_dict}
    return render(request, 'my_notebook/language.html', context)


def language(request, language: str):
    # Динамическая страница с языками
    if language in language_dict:
        return HttpResponse(f'Язык программирования - {language.title()}')
    else:
        return HttpResponseNotFound(f'Неизвестный язык программирования - {language.title()}')


def language_by_number(request, language: int):
    # Динамическая страница с языками для чисел в URL
    if language > len(language_dict):
        return HttpResponseNotFound(f'Неизвестный порядковый номер   - {language}')
    name_language = language_dict[language]
    redirect_url = reverse('language', args=[name_language])
    return HttpResponseRedirect(redirect_url)
