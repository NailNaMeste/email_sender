# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class MessageModel(models.Model):

    title = models.CharField('Заголовок/Тема письма', max_length=128, blank=True)
    text = RichTextField(
        'Текст',
        blank=True,
        help_text="Тут можно написать шаблон, НО! пожалуйста, не используйте тут"
                  " русские символы, сегодня не хочется разбираться с кодировками"
    )
    html_text = models.FileField('Файл шаблона', upload_to='messages/', blank=True)

    class Meta:
        verbose_name = 'Текст сообщения'
        verbose_name_plural = 'Тексты сообщений'

    def __str__(self):
        return "ID {}".format(self.id)


class Receiver(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True)
    date_birth = models.DateField(blank=True)

    class Meta:
        verbose_name = verbose_name_plural = 'Получатели'

    def __str__(self):
        return "{} {}".format(self.email, self.first_name)


class SendingTask(models.Model):
    CREATED = 0
    SCHEDULED = 1
    SENT = 2
    WAS_READ = 3
    ERROR = 4
    SUCCESS = 5
    STATUS_CHOICES = (
        (CREATED, 'Создано'),
        (SCHEDULED, 'Запланировано'),
        (SENT, 'Отправляется'),
        (WAS_READ, 'Получено'),
        (ERROR, 'Ошибка'),
        (SUCCESS, 'Успешно')
    )
    name = models.CharField(max_length=64)
    receivers = models.ManyToManyField('Receiver')
    message = models.ForeignKey('MessageModel')
    time_to_start = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=CREATED)

    class Meta:
        verbose_name = verbose_name_plural = 'Задачи на отправку'

    def __str__(self):
        return self.name

