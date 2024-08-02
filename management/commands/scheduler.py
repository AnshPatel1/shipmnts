# management/commands/scheduler.py
from django.core.management.base import BaseCommand
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from Email.models import Schedule

class Command(BaseCommand):
    help = 'Runs the scheduler.'

    def handle(self, *args, **options):
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoJobStore(), "default")

        schedules = Schedule.objects.all()
        for schedule in schedules:
            if schedule.schedule == 'daily':
                scheduler.add_job(schedule.email.send_email, 'cron', hour=schedule.time.hour, minute=schedule.time.minute)
            elif schedule.schedule == 'weekly':
                scheduler.add_job(schedule.email.send_email, 'cron', day_of_week=schedule.day, hour=schedule.time.hour, minute=schedule.time.minute)
            elif schedule.schedule == 'monthly':
                scheduler.add_job(schedule.email.send_email, 'cron', day=schedule.date, hour=schedule.time.hour, minute=schedule.time.minute)
            elif schedule.schedule == 'quarterly':
                scheduler.add_job(schedule.email.send_email, 'cron', month='*/3', day=schedule.date, hour=schedule.time.hour, minute=schedule.time.minute)

        register_events(scheduler)
        scheduler.start()
        self.stdout.write(self.style.SUCCESS('Scheduler started...'))