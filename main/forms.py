from django.forms import ModelForm
from django import forms
from .models import *
from .widgets import DateTimePickerInput
from django.contrib.auth.forms import UserCreationForm


class UserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username',  'password',)
        # widgets = {
        #     "date": forms.DateTimeField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
        # }


class DeviceForm(ModelForm):
    class Meta:
        model = Devices
        fields = 'name', 'type', 'cables', 'status'


class PersonBookingForm(ModelForm):
    class Meta:
        model = PersonBooking
        fields = ('name', 'email', 'contact',
                  'devices', 'date', 'time', 'end_time')
        widgets = {
            "date": DateTimePickerInput()
        }


class CableForm(ModelForm):
    class Meta:
        model = Cable
        fields = 'name',

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
        fields = 'pin_no', 'surname', 'first_name', 'title', 'sex', 'date_of_birth', 'address', 'phone_number', 'patient_type'


class PhysioSessionForm(ModelForm):
    class Meta:
        model = PhysioSession
        fields = 'patient','date_of_visit',"doctor","diagnosis","therapy","therapist", "ward","receipt_no"
        # widgets = {
        #     "date": DateTimePickerInput(),
        #     "next_visit_date": DateTimePickerInput(),
        #     "next_visit_time": forms.TimeInput(attrs={'type': 'time'}),
        #     "time": forms.TimeInput(attrs={'type': 'time'})
        # }
        
class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = 'name', 'status'


class TherapyForm(ModelForm):
    class Meta:
        model = Therapy
        fields = 'name', 'status','breif_description'



class TherapistForm(ModelForm):
    class Meta:
        model = Therapist
        fields = 'name', 'email', 'telephone', 'status'
        
    
class DiagnosisForm(ModelForm):
    class Meta:
        model = Diagnosis
        fields = 'name', 'status', 'breif_description'


class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields = 'name', 'breif_description', 'status'