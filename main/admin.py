from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(CustomUser)
admin.site.register(Patient)

admin.site.register(Therapy)
admin.site.register(Diagnosis)
admin.site.register(Ward)
admin.site.register(Doctor)


@admin.register(PhysioSessionAdmission)
class PhysisoSessionAdmin(admin.ModelAdmin):
    list_display = ("admission_no", "therapist", "patient")
    list_filter = ("admission_no", "therapist", "patient", "doctor")
    search_fields = ("admission_no", "therapist", "patient", "status")
    list_per_page = 25


@admin.register(Receipt)
class Receipt(admin.ModelAdmin):
    list_display = ("visit_no", "receipt_number", "quantity_of_session", "payment_date")


@admin.register(PhysioSession)
class PhysioSessionAdmin(admin.ModelAdmin):
    list_display = (
        "physiosession_no",
        "therapist",
        "created_at",
    )


# @admin.register(PhysioSessionAdmission)
# class PhysioSessionAdmission(admin.ModelAdmin):
