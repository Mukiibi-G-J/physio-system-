from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

cableTypes = (
    ("HDMI", "HDMI"),
    ("VGA", "VGA"),
    ("DVI", "DVI"),
    ("POWER CABLE", "POWER CABLE"),
)


class Cable(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Devices(models.Model):
    name = models.CharField(max_length=200, unique=True)
    type = models.CharField(max_length=200)
    cables = models.ManyToManyField(Cable, blank=False)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):

    # department = models.CharField(max_length=100)

    # date = models.CharField(max_length=100)
    # email = models.EmailField(unique=True)
    # contact = models.CharField(max_length=9)
    # devices = models.ManyToManyField(Devices)
    phone_number = PhoneNumberField()


class PersonBooking(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    date = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=False, null=False, blank=False)
    end_time = models.TimeField(auto_now_add=False, null=False, blank=False)
    devices = models.ForeignKey(
        Devices, related_name='dev', on_delete=models.CASCADE)
    approve = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Therapy(models.Model):
    name = models.CharField(max_length=255, unique=True)
    breif_description = models.TextField(
        null=True, blank=True, default="No description")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    breif_description = models.TextField(
        null=True, blank=True, default="No description")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    choice_titles = [
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Ms', 'Ms'),       ('Dr', 'Dr'),
        ('Prof', 'Prof'),
        ('Rev', 'Rev'),
        ("Hajati", "Hajati"),
        ("Haji", "Haji"),
        ("Fr", "Fr"),

    ]
    gender = [
        ('Female', "Female"),
        ("Male", 'Male')
    ]

    patient_type_chocie = [
        ("Inpatient", "Inpatient"),
        ("Outpatient", "Outpatient")

    ]
    patient_id = models.CharField(max_length=200)
    pin_no = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    title = models.CharField(choices=choice_titles, max_length=10)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now_add=False)
    phone_number = models.CharField(max_length=10)
    sex = models.CharField(choices=gender, max_length=10)
    in_patient = models.BooleanField(default=False)
    out_patient = models.BooleanField(default=False)
    patient_type = models.CharField(max_length=200, choices=patient_type_chocie)
    created_at =models.DateTimeField(auto_now=True)
    
    @property
    def get_full_name(self):
        return self.surname + " " + self.first_name

    def __str__(self):
        return self.get_full_name


class Doctor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=255)
    breif_description = models.TextField(
        null=True, blank=True, default="No description")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class PhysioSession(models.Model):
    patientType = [
        ('IN PATIENT', 'IN PATIENT'),
        ('OUT PATIENT', 'OUT PATIENT')
    ]
    therapist = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    date_of_visit = models.DateField(auto_now_add=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.PROTECT)
    therapy = models.ForeignKey(Therapy, on_delete=models.PROTECT)
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT)
    status = models.BooleanField(default=False)
    receipt_no = models.CharField(max_length=255)


class Therapist(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    therapist = models.ForeignKey(Therapy, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
