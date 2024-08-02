from rest_framework import serializers
from .models import *

"""
POST /schedule-email: Endpoint to schedule an email.
GET /scheduled-emails: Endpoint to retrieve a list of scheduled emails.
GET /scheduled-emails/{id}: Endpoint to retrieve details of a specific scheduled email.
DELETE /scheduled-emails/{id}: Endpoint to cancel a scheduled email.
"""


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

    def validate(self, data):
        recipients = data.get('recipients')
        cc = data.get('cc')
        bcc = data.get('bcc')
        if not recipients and not cc and not bcc:
            raise serializers.ValidationError("At least one recipient is required.")
        return data


class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'

    def validate(self, data):
        email = data.get('email')
        recipient = data.get('recipient')
        if email.sender == recipient:
            raise serializers.ValidationError("Sender cannot be a recipient.")
        return data


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

    def validate(self):
        attachment = self.get('attachment')
        if attachment.size > 1024 * 1024:
            raise serializers.ValidationError("Attachment size cannot exceed 1MB.")
        return attachment


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
