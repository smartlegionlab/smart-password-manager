import logging
from typing import List, Optional, Dict, Any, Union

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailService:
    
    def __init__(self):
        pass
    
    def send_simple(
        self,
        subject: str,
        message: str,
        to: List[str],
        from_email: Optional[str] = None,
        is_html: bool = False,
    ) -> bool:
        try:
            send_mail(
                subject=subject,
                message=strip_tags(message) if is_html else message,
                from_email=from_email or settings.DEFAULT_FROM_EMAIL,
                recipient_list=to,
                fail_silently=False,
                html_message=message if is_html else None,
            )
            logger.info(f"Email sent to: {to}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {to}: {e}")
            return False
    
    def send_template(
        self,
        subject: str,
        template: str,
        context: Dict[str, Any],
        to: List[str],
        from_email: Optional[str] = None,
    ) -> bool:
        try:
            print(f"Rendering the template: {template}")
            print(f"Context: {context}")
            
            html_body = render_to_string(template, context)
            print(f"HTML received, length: {len(html_body)}")
            
            text_body = strip_tags(html_body)
            
            result = send_mail(
                subject=subject,
                message=text_body,
                from_email=from_email or settings.DEFAULT_FROM_EMAIL,
                recipient_list=to,
                fail_silently=False,
                html_message=html_body,
            )
            print(f"send_mail returned: {result}")
            logger.info(f"Template email sent to: {to}")
            return True
        except Exception as e:
            logger.error(f"Failed to send template email to {to}: {e}")
            print(f"ERROR: {e}")
            import traceback
            traceback.print_exc()
            return False


class VerificationEmail:
    
    @staticmethod
    def send(user_email: str, verification_url: str, username: str) -> bool:
        return EmailService().send_template(
            subject='Email confirmation',
            template='emails/verification.html',
            context={
                'username': username,
                'verification_url': verification_url,
                'site_name': getattr(settings, 'SITE_NAME', 'Наш сайт'),
            },
            to=[user_email],
        )


class PasswordResetEmail:
    
    @staticmethod
    def send(user_email: str, reset_url: str, username: str) -> bool:
        return EmailService().send_template(
            subject='Password recovery',
            template='emails/password_reset.html',
            context={
                'username': username,
                'reset_url': reset_url,
                'site_name': getattr(settings, 'SITE_NAME', 'Наш сайт'),
            },
            to=[user_email],
        )


class NotificationEmail:
    
    @staticmethod
    def send(user_email: str, title: str, message: str, action_url: Optional[str] = None) -> bool:
        return EmailService().send_template(
            subject=title,
            template='emails/notification.html',
            context={
                'title': title,
                'message': message,
                'action_url': action_url,
                'action_text': 'Go to' if action_url else None,
            },
            to=[user_email],
        )


class WelcomeEmail:
    
    @staticmethod
    def send(user_email: str, username: str) -> bool:
        return EmailService().send_template(
            subject='Welcome! 🎉',
            template='emails/welcome.html',
            context={
                'username': username,
                'site_name': getattr(settings, 'SITE_NAME', 'Наш сайт'),
            },
            to=[user_email],
        )



class Email:
    
    @staticmethod
    def send(subject: str, message: str, to: Union[str, List[str]], is_html: bool = False) -> bool:
        to_list = [to] if isinstance(to, str) else to
        return EmailService().send_simple(subject, message, to_list, is_html=is_html)
    
    @staticmethod
    def template(template_path: str, context: Dict, to: Union[str, List[str]], subject: str = None) -> bool:
        to_list = [to] if isinstance(to, str) else to
        if not subject:
            subject = context.get('subject', 'Notification')
        return EmailService().send_template(subject, template_path, context, to_list)
    
    @staticmethod
    def verification(to: str, url: str, username: str) -> bool:
        return VerificationEmail.send(to, url, username)
    
    @staticmethod
    def reset_password(to: str, url: str, username: str) -> bool:
        return PasswordResetEmail.send(to, url, username)
    
    @staticmethod
    def notification(to: str, title: str, message: str, action_url: str = None) -> bool:
        return NotificationEmail.send(to, title, message, action_url)
    
    @staticmethod
    def welcome(to: str, username: str) -> bool:
        return WelcomeEmail.send(to, username)
