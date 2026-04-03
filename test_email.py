import os
import django
from django.core.mail import send_mail
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogApp.settings')
django.setup()

try:
    send_mail(
        'Test Subject',
        'Test message body.',
        settings.EMAIL_HOST_USER,
        ['payalkgoel21@gmail.com'],
        fail_silently=False,
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
