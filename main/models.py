from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib import messages


class CustomUser(AbstractUser):
    therapist = models.BooleanField(default=False)
    phone_number = PhoneNumberField()


class Therapy(models.Model):
    name = models.CharField(max_length=255, unique=True)
    breif_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Diagnosis(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    breif_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=255, unique=True)

    specialist = models.CharField(
        max_length=255, null=True, blank=True, default="Orthopaedic Officer"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Ward(models.Model):
    name = models.CharField(max_length=255, unique=True)
    breif_description = models.TextField(
        null=True, blank=True, default="No description"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# class Addmission(models.Model):
class Patient(models.Model):
    patient_no = models.CharField(max_length=255, unique=True)
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    date_of_birth = models.DateField(auto_now_add=False)
    phone_number = models.CharField(max_length=10)
    surname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    @property
    def get_full_name(self):
        return self.surname + " " + self.first_name

    def __str__(self):
        return self.get_full_name


class PhysioSessionAdmission(models.Model):
    admission_no = models.CharField(max_length=255)
    therapist = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    patient = models.ForeignKey(
        Patient, on_delete=models.PROTECT, related_name="patient_physio_admission"
    )
    date_of_visit = models.DateField(auto_now_add=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(
        Diagnosis, on_delete=models.CASCADE, related_name="diagnosis_physio_admission"
    )
    ward = models.ForeignKey(Ward, on_delete=models.PROTECT, null=True)
    discharge = models.BooleanField(default=False)
    discharge_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    more_notes = models.TextField()
    patient_type = models.CharField(max_length=255)
    clinic_master_admission_no = models.CharField(max_length=255, blank=True, null=True)
    quantity_of_sessions = models.PositiveIntegerField(default=0)

    def save(self, patient_no=None, *args, **kwargs):
        if not self.pk:
            last_admission = PhysioSessionAdmission.objects.filter(
                patient__patient_no=patient_no
            )
            print(last_admission)
            # last_admission = PhysioSessionAdmission.objects.order_by("-id").first()
            if len(last_admission) > 0:
                last_admission = last_admission.last()
                admission_parts = last_admission.admission_no.split("-")
                last_id = int(last_admission.admission_no.split("-")[-1][3:])

                print(last_id)
                self.admission_no = (
                    f"{self.patient.patient_no}-PHA{str(last_id + 1).zfill(4)}"
                )

            else:
                self.admission_no = f"{self.patient.patient_no}-PHA0001"
        super().save(*args, **kwargs)


class PhysioSession(models.Model):
    physiosession_no = models.CharField(max_length=255)
    admission_no = models.ForeignKey(
        PhysioSessionAdmission, models.PROTECT, related_name="physio_admission_no"
    )
    therapy = models.ManyToManyField(Therapy, default="Old Therapy")
    more_notes = models.TextField()
    therapist = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)

    def save(self, patient_no=None, *args, **kwargs):
        if not self.pk:
            last_admission = (
                PhysioSessionAdmission.objects.filter(patient__patient_no=patient_no)
                .order_by("-id")
                .first()
            )
            if last_admission.quantity_of_sessions > 0:
                new_quantity_0f_session = int(last_admission.quantity_of_sessions) - 1

                last_admission.quantity_of_sessions = new_quantity_0f_session
                last_admission.save()
                last_physioSession = (
                    PhysioSession.objects.filter(admission_no=last_admission)
                    .order_by("-id")
                    .first()
                )

                if last_physioSession:
                    last_id = int(
                        last_physioSession.physiosession_no.split("-")[-1][2:]
                    )
                    self.physiosession_no = (
                        f"{patient_no}-PH{str(last_id + 1).zfill(4)}"
                    )
                    self.admission_no = last_admission
                    print(self.admission_no)
                else:
                    self.physiosession_no = f"{patient_no}-PH0001"
                    self.admission_no = last_admission
            else:
                messages.error("No more sessions available for the admission.")

        super().save(*args, **kwargs)

    # @property
    # def full_name(self):
    #     return f"{self.patient_name} {self.patient_surname}"

    # def __str__(self):
    #     return self.full_name


class Therapist(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    telephone = models.CharField(max_length=10)
    therapist = models.ForeignKey(Therapy, on_delete=models.PROTECT)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Receipt(models.Model):
    physiosessionadmission = models.ForeignKey(
        PhysioSessionAdmission,
        models.PROTECT,
        related_name="receipt_physiosessionadmission",
    )
    receipt_number = models.CharField(max_length=50, unique=True)
    quantity_of_session = models.PositiveIntegerField()
    visit_no = models.CharField(max_length=255)
    payment_date = models.DateField()
    # add other fields as needed


class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=50)
    quantity_of_session = models.PositiveIntegerField()
    invoice_date = models.DateField()


class TotalSession(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    total_quantity_of_session = models.PositiveIntegerField()


class DiagnosisForPatient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
