from django.contrib import admin

# Register your models here.
from .models import *




admin.site.register(CustomUser)
admin.site.register(Devices)
admin.site.register(Cable)
admin.site.register(PersonBooking)
admin.site.register(Patient)
admin.site.register(PhysioSession)
admin.site.register(Therapy)
admin.site.register(Diagnosis)
admin.site.register(Ward)