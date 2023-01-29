from django.db import models
from django.urls import reverse

# Create your models here.


class Topic(models.Model):
    # Тема, которую изучает пользователь
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    # Текстовое поле для заголовков, с автоматическим присвоением даты при создании.

    def __str__(self):
        # Возвращает текстовое представление модели
        return self.text


class Entry(models.Model):
    # Информация изученная пользователем по теме
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', null=False)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + '...'

    def get_url(self):
        return reverse('note', args=[self.id])
