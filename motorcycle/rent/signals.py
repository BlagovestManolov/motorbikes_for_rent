# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from django.utils.html import strip_tags

from motorcycle.rent.models import Rental, ContactUs
from django.template.loader import render_to_string


def send_successful_contact_us_email(user):
    html_message = render_to_string(
        'email/contact_us_email_template.html',
        {'profile': user},
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject='Thank You for Your Inquiry!',
        message=plain_message,
        html_message=html_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=(user.email,)
    )


@receiver(post_save, sender=ContactUs)
def send_contact_us_message(sender, instance, **kwargs):
    if instance.send_email:
        send_successful_contact_us_email(instance)

#
# @receiver(post_save, sender=Rental)
# def send_email_rent(sender, instance, **kwargs):
#     html_message = render_to_string(
#         'email/rental_email_template.html',
#         {'instance': instance},
#     )
#     plain_message = strip_tags(html_message)
#     if instance.send_email:
#         subject = 'Thank you for choosing us!'
#         message = plain_message
#         html_message = html_message
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [instance.email]
#
#         send_mail(subject, message, from_email, recipient_list)
#
#
# @receiver(post_save, sender=ContactUs)
# def send_email_contact_us(sender, instance, **kwargs):
#     html_message = render_to_string(
#         'email/contact_us_email_template.html',
#         {'instance': instance},
#     )
#     plain_message = strip_tags(html_message)
#     if instance.send_email:
#         subject = 'Thank You for Your Inquiry!'
#         message = plain_message
#         html_message = html_message
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [instance.email]
#
#         send_mail(subject, message, from_email, recipient_list)
