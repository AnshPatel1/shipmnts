from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Email.views import *


def get_router():
    """
    POST /schedule-email: Endpoint to schedule an email.
    GET /scheduled-emails: Endpoint to retrieve a list of scheduled emails.
    GET /scheduled-emails/{id}: Endpoint to retrieve details of a specific scheduled email.
    DELETE /scheduled-emails/{id}: Endpoint to cancel a scheduled email.
    """

    router = DefaultRouter()
    router.register('email', EmailViewSet, basename='email')
    router.register('recipient', RecipientViewSet, basename='recipient'),
    router.register('attachment', AttachmentViewSet, basename='attachment')
    router.register('schedule-email', ScheduleEmailViewSet, basename='schedule-email')
    router.register('scheduled-emails', ScheduleEmailViewSet, basename='scheduled-emails')

    return router
