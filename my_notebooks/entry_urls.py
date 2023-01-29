# Схемы URL для my_notebook.entry
from django.urls import include, re_path, path
from . import views


urlpatterns = [
    path('', views.entries),
    path('<int:note_number>', views.notes, name='note'),
]