from django.forms import ModelForm, Form
from django import forms
from .models import *
from .widgets import DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
        )
        # widgets = {
        #     "date": forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        # }


# class NewUserForm(UserCreationForm):
#     	email = forms.EmailField(required=True)

#         class Meta:
#             model = User
#             fields = ("email", "password1", "password2")

#         def save(self, commit=True):
#             user = super(NewUserForm, self).save(commit=False)
#             user.email = self.cleaned_data['email']
#             if commit:
#                 user.save()
#             return use
# 'occupation','marital_status','religion'


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        # fields = 'pin_no', 'surname', 'first_name', 'title', 'sex', 'date_of_birth', 'address', 'phone_number', 'patient_type'
        fields = (
            "gender",
            "address",
            "phone_number",
            "date_of_birth",
        )


class PhysioSessionAdmissionForm(ModelForm):
    more_notes = forms.CharField(widget=forms.Textarea(attrs={"rows": 4, "cols": 50}))

    class Meta:
        model = PhysioSessionAdmission
        fields = (
            "date_of_visit",
            "doctor",
            "diagnosis",
            "therapy",
            "therapist",
            "ward",
            
            "more_notes",
            # "admission_no",
        )

    therapy = forms.ModelMultipleChoiceField(
        queryset=Therapy.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple,
    )
    diagnosis = forms.ModelChoiceField(
        queryset=Diagnosis.objects.all().order_by("name"),
    )

    # widgets = {
    #     "date": DateTimePickerInput(),
    #     "next_visit_date": DateTimePickerInput(),
    #     "next_visit_time": forms.TimeInput(attrs={'type': 'time'}),
    #     "time": forms.TimeInput(attrs={'type': 'time'})
    # }


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "name", "specialist", "status"


class TherapyForm(ModelForm):
    class Meta:
        model = Therapy
        fields = "name", "status", "breif_description"


class TherapistForm(ModelForm):
    class Meta:
        model = Therapist
        fields = "name", "email", "telephone", "status"


class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = "name", "status", "breif_description"


class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields = "name", "breif_description", "status"


class BackDate(forms.Form):
    date = forms.DateField(label="Date")
    patient_no = forms.CharField(label="Patient Number")
    PATIENT_CHOICES = [("inpatient", "In-Patient"), ("outpatient", "Out-Patient")]
    patient_type = forms.ChoiceField(choices=PATIENT_CHOICES)
