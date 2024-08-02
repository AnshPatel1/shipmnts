from django.core.mail import EmailMessage
import shipmnts.settings as settings


class Mailer:
    # send_email method is used to send an email (recipient{to[], cc[], bcc[]}, subject, message, attachment[])
    @staticmethod
    def send_email(recipient, subject, message, attachment=None):
        try:
            mail = EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient['to'],
                                cc=recipient['cc'], bcc=recipient['bcc'])
            if attachment:
                for file in attachment:
                    mail.attach_file(file)
            mail.send()
            return True
        except Exception as e:
            print(e)
            return False
