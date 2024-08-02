from rest_framework import serializers
from .models import *

"""
POST /schedule-email: Endpoint to schedule an email.
GET /scheduled-emails: Endpoint to retrieve a list of scheduled emails.
GET /scheduled-emails/{id}: Endpoint to retrieve details of a specific scheduled email.
DELETE /scheduled-emails/{id}: Endpoint to cancel a scheduled email.
"""


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def validate(self, data):
        schedule = data.get('schedule')
        time = data.get('time')
        day = data.get('day')
        date = data.get('date')
        if schedule == 'daily' and day:
            raise serializers.ValidationError("Day is not required for daily schedule.")
        if schedule == 'weekly' and not day:
            raise serializers.ValidationError("Day is required for weekly schedule.")
        if schedule == 'monthly' and not date:
            raise serializers.ValidationError("Date is required for monthly schedule.")
        if schedule == 'quarterly' and not date:
            raise serializers.ValidationError("Date is required for quarterly schedule.")
        return data
