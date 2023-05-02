from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(CustomUser)
admin.site.register(Devices)
admin.site.register(Cable)
admin.site.register(PersonBooking)
admin.site.register(Patient)

admin.site.register(Therapy)
admin.site.register(Diagnosis)
admin.site.register(Ward)
admin.site.register(Doctor)


@admin.register(PhysioSession)
class PhysisoSessionAdmin(admin.ModelAdmin):
    list_display = ('patient_surname', 'date_of_visit', 'status')
    list_filter = ('patient_surname', 'date_of_visit',  'status', 'patient_type', 'ward', 'doctor')
    search_fields = ('patpatient_surname', 'date_of_visit', 'status')
    list_per_page = 25

