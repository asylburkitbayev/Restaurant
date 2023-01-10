import random
from django.conf import settings
from django.core.mail import send_mail


def generate_activation_code():
    return random.randint(100000, 999999)


def send_verification_mail(email, code):
    subject = 'Код подтверждения'
    message = 'Код для активации вашего аккаунта:' \
              'никому не сообщайте данный код' \
              f'Код: {code}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list)
    print(f"Код успешно отправлен на email {email}")

