from django.contrib import admin

# Register your models here.

from .models import EventDetails
from .models import User

admin.site.register(EventDetails)
admin.site.register(User)