import os
import smtplib
from email.MIMEText import MIMEText
from email.mime.multipart import MIMEMultipart

from django.template.loader import render_to_string
from main.models import Receiver, MessageModel
from djangoProject import settings


class SMTPSender:
    def __init__(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.login = settings.GOOGLE_EMAIL
        self.app_password = settings.GOOGLE_APP_PAS
        print self.login, self.app_password
        try:
            self.server.login(self.login, self.app_password)
        except Exception as e:
            print str(e)

    def send_mail(self, message_id, receiver_ids):
        receivers = Receiver.objects.filter(id__in=receiver_ids)
        message_model = MessageModel.objects.get(id=message_id)
        msg = MIMEMultipart()
        msg['Subject'] = message_model.title
        for receiver in receivers:
            if message_model.html_text:
                context = {
                    "first_name": receiver.first_name,
                    "last_name": receiver.last_name,
                    "date_birth": receiver.date_birth.strftime("%m/%d/%Y")
                }
                text = render_to_string(message_model.html_text.path, context).encode('ascii')
            else:
                text = message_model.text
            msg.attach(MIMEText(text, 'html'))
            text = msg.as_string()
            self.server.sendmail(
                from_addr=self.login,
                to_addrs=receiver.email,
                msg=text
            )

    def close(self):
        self.server.quit()

