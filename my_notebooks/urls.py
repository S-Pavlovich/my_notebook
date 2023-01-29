# Схемы URL для my_notebook.language
from django.urls import include, re_path, path
from . import views


urlpatterns = [
    path('', views.language_list),
    path('<int:language>', views.language_by_number, name='language_num'),
    path('<str:language>', views.language, name='language'),
]