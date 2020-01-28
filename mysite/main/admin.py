from django.contrib import admin
from .models import Tutorials,Essays,Usernames,Vehicles

from django.db import models

#Register your models here.

admin.site.register(Vehicles)
admin.site.register(Tutorials)
admin.site.register(Usernames)
admin.site.register(Essays)
