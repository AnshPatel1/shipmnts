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


class Recipient(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    recipient = models.EmailField()
    type = models.CharField(max_length=4, choices=[
        ('main', 'main'),
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
    day = models.CharField(max_length=10, null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)

    @staticmethod
    def create_schedule(email, schedule, time, day=None, date=None):
        # Create a schedule for the email
        # Use scehdule library to create a schedule for the emails
        if schedule == 'daily':
            schedule.every().day.at(time).do(email)
        pass


    def __str__(self):
        return str(self.date)


class EmailStatus(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.status


