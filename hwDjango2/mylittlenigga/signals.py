from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.db.models.signals import post_save, pre_save
from django.dispatch import Signal
from django.dispatch import receiver
from django.core.signing import Signer
signal = Signal()

@receiver(signal, sender=User)
def check_user_email(sender, **kwargs):
    signer = Signer()
    print('testSOIJFOI')
    user = kwargs['instance']
    username = user.username
    niga = signer.sign(value=username)
    email = EmailMessage(subject='Check email', body=f'127.0.0.1:8000/accept/{niga}', to=[user.email])
    email.send()
