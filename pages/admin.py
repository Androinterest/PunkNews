from django.contrib import admin
from .models import contact
from .models import extUser

# Register your models here.
admin.site.register(contact)
admin.site.register(extUser)

