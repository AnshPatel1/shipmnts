from django.contrib import admin
from Email.models import *

admin.site.register(Email)
admin.site.register(Recipient)
admin.site.register(Attachment)
admin.site.register(Schedule)

