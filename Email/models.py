from django.db import models
import schedule


# These models are designed to create an Emailing Automation sysyetm
# Below is the design of the models. Emails contain recipients (main, cc, bcc) subject, body, schedule, and attachments as well


class Email(models.Model):
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    def send_email(self):
        from Email.utils import Mailer
        recipients = {
            "to": Recipient.objects.filter(email=self, type="TO"),
            "cc": Recipient.objects.filter(email=self, type='CC'),
            "bcc": Recipient.objects.filter(email=self, type='BCC')
        }

        attachments = Attachment.objects.filter(email=self)
        attachment_files = [attachment.attachment for attachment in attachments]

        if Mailer.send_email(recipients, self.subject, self.body, attachment_files):
            EmailStatus.objects.create(email=self, status='success', message='Email sent successfully')
        else:
            EmailStatus.objects.create(email=self, status='failed', message='Email sending failed')


class Recipient(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    recipient = models.EmailField()
    type = models.CharField(max_length=4, choices=[
        ('TO', 'TO'),
        ('CC', 'CC'),
        ('BCC', 'BCC')
    ])

    def __str__(self):
        return self.recipient


class Attachment(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to='media/attachments/')

    def __str__(self):
        return self.attachment.name


class Schedule(models.Model):
    """
    Schedule email for daily, weekly, monthly, or quarterly basis.
    Schedule will have a creation datetime and modified datetime.
    Schedule Options:
        1. Daily - can be at a specific time (default 00:00)
        2. Weekly - can be on a specific day at a specific time (default Monday, 00:00)
        3. Monthly - can be on a specific date at a specific time (default 1st, 00:00)
        4. Quarterly - can be on a specific date at a specific time (default 1st, 00:00)
    """

    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=20, choices=[
        ('daily', 'daily'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
        ('quarterly', 'quarterly')
    ])
    time = models.TimeField()
    day = models.CharField(max_length=10, null=True, blank=True, choices=(
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday')

    ))
    date = models.IntegerField(null=True, blank=True)

    @staticmethod
    def create_schedule(email, _schedule, time, day=None, date=None):
        try:
            s = Schedule()
            s.email = email
            s.schedule = _schedule
            s.time = time
            s.day = day
            s.date = date
            s.save()
        except Exception as e:
            raise e

        # Create a schedule for the email
        email.send_email()
        if _schedule == 'daily':
            schedule.every().day.at(time).do(email.send_email)
        elif _schedule == 'weekly':
            if day == 'monday':
                schedule.every().monday.at(time).do(email.send_email)
            elif day == 'tuesday':
                schedule.every().tuesday.at(time).do(email.send_email)
            elif day == 'wednesday':
                schedule.every().wednesday.at(time).do(email.send_email)
            elif day == 'thursday':
                schedule.every().thursday.at(time).do(email.send_email)
            elif day == 'friday':
                schedule.every().friday.at(time).do(email.send_email)
            elif day == 'saturday':
                schedule.every().saturday.at(time).do(email.send_email)
            elif day == 'sunday':
                schedule.every().sunday.at(time).do(email.send_email)
        elif _schedule == 'monthly':
            schedule.every(30).days.at(date).do(email.send_email)
        elif _schedule == 'quarterly':
            schedule.every(3*30).days.at(date).do(email.send_email)
        else:
            raise ValueError("Invalid schedule")

    def __str__(self):
        return str(self.date)


class EmailStatus(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.status
