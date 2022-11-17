
from services import SMTPSender


from djangoProject import celery_app
from models import SendingTask


@celery_app.task
def send_mail(sending_task_id):
    task = SendingTask.objects.get(id=sending_task_id)
    try:
        server = SMTPSender()
        server.send_mail(task.message.id, list(task.receivers.values_list('id', flat=True)))
        server.close()
        task.status = 5
        task.save()
        print 'okay'
    except Exception as e:
        print e
        print str(e)
        task.status = 4
        task.save()


