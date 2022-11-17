# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import datetime
from models import Receiver, MessageModel, SendingTask
from tasks import send_mail


@admin.register(MessageModel)
class MessageModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Receiver)
class ReceiverAdmin(admin.ModelAdmin):
    pass


@admin.register(SendingTask)
class SendingTaskAdmin(admin.ModelAdmin):
    actions = ['send_mail', ]
    readonly_fields = ['status', ]
    list_display = ['name', 'status']

    def send_mail(self, request, queryset):
        for item in queryset:
            if item.time_to_start:
                send_mail.apply_async(
                    [item.id],
                    eta=item.time_to_start
                )
                item.status = 1
                item.save()
            else:
                send_mail.delay(item.id)
                item.status = 2
                item.save()

    send_mail.short_description = 'Отправить'
