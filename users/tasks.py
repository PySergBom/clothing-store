from django.utils.timezone import now

from celery import shared_task
import uuid
from datetime import timedelta

from users.models import EmailVerification, User


@shared_task
def send_verification_email_task(user_id):
    user = User.objects.get(id=user_id)
    expiration = now() + timedelta(hours=48)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
    record.send_verification_email()