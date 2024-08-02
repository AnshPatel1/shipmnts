from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import *
from .serializers import *


# POST /schedule-email: Endpoint to schedule an email.
# GET /scheduled-emails: Endpoint to retrieve a list of scheduled emails.
# GET /scheduled-emails/{id}: Endpoint to retrieve details of a specific scheduled email.
# DELETE /scheduled-emails/{id}: Endpoint to cancel a scheduled email.


class ScheduleEmailViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Schedule.create_schedule(serializer.validated_data)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Schedule.cancel_schedule(instance)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

