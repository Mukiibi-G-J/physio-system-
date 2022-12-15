from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import DeviceForm, UserForm, PersonBookingForm
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.urls import reverse
from .decorators import auth_user_should_not_access
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
from django.http import JsonResponse
# Import date class from datetime module
from datetime import date
from  patients.models import Patients
from  .models import  Patient

# Returns the current local date

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

def dashboard(request):
    patients = Patient.objects.all().count()
    physio_sessions = PhysioSession.objects.all().count()
    patient_month = PhysioSession.objects.filter(date__month=date.today().month).count()
    patient_last_month = PhysioSession.objects.filter(date__month=date.today().month-1).count()
    patient_quarter = PhysioSession.objects.filter(date__month__in=[1,2,3]).count()
    patient_year = PhysioSession.objects.filter(date__year=date.today().year).count()
    current_year = date.today().year
    
    last_year = date.today().year-1
    current_month = date.today().month
    last_month = date.today().month-1
    current_week = date.today().isocalendar()[1]
    last_week = date.today().isocalendar()[1]-1
    
    jan_last_year = PhysioSession.objects.filter(date__month__in=[1],date__year=date.today().year-1).count()
    feb_last_year = PhysioSession.objects.filter(date__month__in=[2],date__year=date.today().year-1).count()
    mar_last_year = PhysioSession.objects.filter(date__month__in=[3],date__year=date.today().year-1).count()
    apr_last_year = PhysioSession.objects.filter(date__month__in=[4],date__year=date.today().year-1).count()
    may_last_year = PhysioSession.objects.filter(date__month__in=[5],date__year=date.today().year-1).count()
    jun_last_year = PhysioSession.objects.filter(date__month__in=[6],date__year=date.today().year-1).count()
    jul_last_year = PhysioSession.objects.filter(date__month__in=[7],date__year=date.today().year-1).count()
    aug_last_year = PhysioSession.objects.filter(date__month__in=[8],date__year=date.today().year-1).count()
    sep_last_year = PhysioSession.objects.filter(date__month__in=[9],date__year=date.today().year-1).count()
    oct_last_year = PhysioSession.objects.filter(date__month__in=[10],date__year=date.today().year-1).count()
    nov_last_year = PhysioSession.objects.filter(date__month__in=[11],date__year=date.today().year-1).count()
    dec_last_year = PhysioSession.objects.filter(date__month__in=[12],date__year=date.today().year-1).count()
    physio_session_last_year = [jan_last_year,feb_last_year,mar_last_year,apr_last_year,may_last_year,jun_last_year,jul_last_year,aug_last_year,sep_last_year,oct_last_year,nov_last_year,dec_last_year] 
    
    jan = PhysioSession.objects.filter(date__month__in=[1]).count()
    feb = PhysioSession.objects.filter(date__month__in=[2]).count()
    mar = PhysioSession.objects.filter(date__month__in=[3]).count()
    apr = PhysioSession.objects.filter(date__month__in=[4]).count()
    may = PhysioSession.objects.filter(date__month__in=[5]).count()
    jun = PhysioSession.objects.filter(date__month__in=[6]).count()
    jul = PhysioSession.objects.filter(date__month__in=[7]).count()
    aug = PhysioSession.objects.filter(date__month__in=[8]).count()
    sep = PhysioSession.objects.filter(date__month__in=[9]).count()
    oct = PhysioSession.objects.filter(date__month__in=[10]).count()
    nov = PhysioSession.objects.filter(date__month__in=[11]).count()
    dec = PhysioSession.objects.filter(date__month__in=[12]).count()
    physio_session_current_year = [jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec]
          
    
    
    patient_last_year = PhysioSession.objects.filter(date__year=date.today().year-1)
    print(patient_month,patient_last_month,patient_quarter)

    context = {
        'patients': patients,
        'physio_sessions': physio_sessions,
        "physio_session_current_year":physio_session_current_year,
        "physio_session_last_year":physio_session_last_year,
    }
    
    
    return render(request, 'Dashboard/dashboard.html', context)

def device_status(request):
    devices = PersonBooking.objects.all()
    for d in devices:

        print(d.devices.name)
    return render(request, 'device_status.html', {'devices': devices})



def ward_reports(request):
    wards = Ward.objects.all().order_by('-id')
    ward_count = []
    for w in wards:
        patient_count = PhysioSession.objects.filter(ward=w).count()
        ward_count.append(patient_count)
    return render(request, 'Ward/ward_report.html', {'wards': wards,"ward_count":ward_count})
@login_required
def home(request):
    form = PersonBookingForm()
    if request.method == "POST":
        data = request.POST
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        devices = request.POST.get("devices")
        date_1 = request.POST.get("date")
        end_time = request.POST.get("end_time")
        start_time = request.POST.get("time")

        start = int(start_time.split(':')[0])
        end = int(end_time.split(':')[0])
        if start > end:
            if not 7 <= start <= 18 and not 7 <= end <= 18:
                messages.add_message(
                    request, messages.ERROR, "Time should be between 7am to 6pm")
                return render(request, 'index.html', {'form': form, "data": data})
            messages.add_message(request, messages.ERROR,
                                 "End Time should greater than Start Time")
            return render(request, 'index.html', {'form': form, "data": data})

        todays_date = date.today().strftime("%y-%m-%d")
        new = '20'+todays_date
        current_booked = PersonBooking.objects.all().filter(date=new)
        for cb in current_booked:
            print(cb.time)
            if int(str(cb.time).split(':')[0]) == start:
                messages.add_message(
                    request, messages.ERROR, "This Time is already booked")
                return render(request, 'index.html', {'form': form, "data": data})
            elif start > int(str(cb.time).split(':')[0]) and start > int(str(cb.end_time).split(':')[0]):
                messages.add_message(
                    request, messages.SUCCESS, "This TIME is Ok")
                return render(request, 'index.html', {'form': form})
            elif start < int(str(cb.time).split(':')[0]) and start < int(str(cb.end_time).split(':')[0]):
                print('ok')
                pbooking = PersonBooking()
                device = Devices.objects.get(id=devices)
                pbooking.name = name
                pbooking.email = email
                pbooking.contact = contact
                pbooking.date = date_1
                pbooking.end_time = end_time
                pbooking.time = start_time
                pbooking.devices = device
                messages.add_message(
                    request, messages.SUCCESS, "This TIME is Ok")
                pbooking.save()
                return render(request, 'index.html', {'form': form})
            elif start > int(str(cb.time).split(':')[0]) and start < int(str(cb.end_time).split(':')[0]):
                print("error")
                messages.add_message(
                    request, messages.ERROR, "This Time is already booked")
                return render(request, 'index.html', {'form': form, "data": data})

        year = date_1.split('-')[0].split('0')[1]
        month = date_1.split('-')[1]
        day = date_1.split('-')[2]
        date_final = year+'-'+month+'-'+day
        print(date_final)
        today = date.today().strftime("%y-%m-%d")

        print(today)
        if date_final < today:
            messages.add_message(request, messages.ERROR,
                                 "Date should be  today or greater than today")
            return render(request, 'index.html', {'form': form, "data": data})

            # return HttpResponse('<div style="color:green;"> This is Date is Ok </div>')
        pbooking = PersonBooking()
        device = Devices.objects.get(id=devices)
        pbooking.name = name
        pbooking.email = email
        pbooking.contact = contact
        pbooking.date = date_1
        pbooking.end_time = end_time
        pbooking.time = start_time
        pbooking.devices = device

        pbooking.save()
        messages.add_message(request, messages.SUCCESS,
                             "Booking was succuess created successfully")

        print(name, email, contact, devices, date, end_time, start_time)

    return render(request, 'index.html', {'form': form})


@login_required
def add_device(request):
    form = DeviceForm()

    context = {
        'form': form,
        "data": request.POST,
    }
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        context = {

            'form': form,
            "data": "",
        }

        if form.is_valid():
            form.save()
            return redirect('device-list')
        else:
            return render(request, 'add_device.html', context)
    return render(request, 'add_device.html', context)


@login_required
def device_list(request):
    devices = Devices.objects.all()

    for device in devices:
        print(device)
        print(device.cables.all())
    context = {

        "devices": devices

    }
    return render(request, 'device_list.html', context)


@auth_user_should_not_access
def login_user(request):
    context = {

    }
    if request.method == 'POST':
        username = request.POST.get("department").upper()
        password = request.POST.get("password")
        user = authenticate(
            request, username=username, password=password)
        if not user:
            print('test3')
            messages.add_message(request, messages.ERROR,
                                 "Invalid credentials, try again")
            return render(request, "login.html", context, status=401)
        login(request, user)
        messages.add_message(request, messages.SUCCESS,
                             f"Welcome {user.username}")
        return redirect('home')

    return render(request, 'login.html', context)


def logout_user(request):

    logout(request)

    messages.add_message(request, messages.SUCCESS, "Successfully logged out")

    return redirect(reverse("login"))


@auth_user_should_not_access
def register_user(request):
    if request.method == "POST":
        context = {"has_error": False, "data": request.POST}
        department = str(request.POST.get("department")).upper()
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        print(department, phone, password, password2)

        if len(password) < 6:
            messages.add_message(
                request, messages.ERROR, "Password should be at least 6 characters"
            )
            context["has_error"] = True
            return render(request, "register.html", context, status=409)

        if password != password2:
            messages.add_message(request, messages.ERROR, "Password mismatch")
            context["has_error"] = True

        if CustomUser.objects.filter(username=department).exists():
            messages.add_message(
                request, messages.ERROR, "Username is taken, choose another one"
            )
            context["has_error"] = True

            return render(request, "register.html", context, status=409)

        # if User.objects.filter(email=email).exists():
        #     messages.add_message(
        #         request, messages.ERROR, "Email is taken, choose another one"
        #     )
        #     context["has _error"] = True

        # if context["has_error"]:
        #     return render(request, "authentication/register.html", context)

        user = CustomUser.objects.create_user(
            username=department, phone_number=phone)
        user.set_password(password)
        user.save()
        return redirect('login')
    return render(request, "register.html")


def check_department(request):
    department = str(request.POST.get('department')).upper()
    print(department)
    # when u add .exists it returns true or false
    if CustomUser.objects.filter(username=department).exists():
        print('true')
        return HttpResponse('<div style="color:red;"> This Department is already registered</div>')
    else:
        return HttpResponse('<div style="color:green;"> This is Department is Ok </div>')


def check_phone(request):
    phone = request.POST.get('phone')
    print(phone)

    # when u add .exists it returns true or false
    if phone.isdigit():
        if CustomUser.objects.filter(phone_number=phone).exists():
            print("true")
            return HttpResponse('<div style="color:red;"> This Phone is already registered</div>')

        else:
            print('false')
            return HttpResponse('<div style="color:green;"> This is Phone is Ok </div>')

    else:
        return HttpResponse('<div style="color:red;"> This Phone is should be a digit</div>')


def check_password(request):
    password = request.POST.get("password")
    password2 = request.POST.get("password2")
    print(password, password2)
    if len(password) < 6:
        return HttpResponse('<div style="color:red;"> This Password is should be greater than 6</div>')

    if password != password2:
        return HttpResponse('<div style="color:red;"> This Password1 is not equal to Password2</div>')
    else:
        return HttpResponse('<div style="color:green;"> This is password is Ok </div>')


def check_phone_2(request):
    phone = request.POST.get('contact')
    print(phone)

    # when u add .exists it returns true or false
    if phone.isdigit():
        return HttpResponse('<div style="color:green;"> This is Phone is Ok </div>')

    else:
        print('false')
        return HttpResponse('<div style="color:red;"> This Phone is should be digits</div>')


def current_date(request):
    print(request.POST)
    date_1 = request.POST.get('date')
    year = date_1.split('-')[0].split('0')[1]
    month = date_1.split('-')[1]
    day = date_1.split('-')[2]
    date_final = year+'-'+month+'-'+day
    print(date_final)
    today = date.today().strftime("%y-%m-%d")
    print(today)
    if date_final < today:
        return HttpResponse('<div style="color:red;"> This Date is should be greater than today</div>')
    else:
        return HttpResponse('<div style="color:green;"> This is Date is Ok </div>')


def check_time(request):
    time = request.POST.get("time")
    end_time = request.POST.get("end_time")
    start = int(time.split(':')[0])
    end = int(end_time.split(':')[0])
    print(time, end_time)
    print(start, end)
    if start < end:
        if 7 <= start <= 18 and 7 <= end <= 18:
            print('true')
            return HttpResponse('<div style="color:green;"> This is Time is Ok </div>')

        else:
            return HttpResponse('<div style="color:red;"> This Time is should be between 7am to 6pm</div>')
    return HttpResponse('<div style="color:red;"> End Time should greater than Start Time</div>')


def add_cables(request):
    if request.method == "POST":
        name = request.POST.get('name')
        if Cable.objects.filter(name=name).exists():
            messages.add_message(request, messages.ERROR,
                                 "Cable is already registered")
            return render(request, 'add_cables.html')

        user = Cable.objects.create(name=name)
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             "Cable added successfully")
        return redirect('home')

    return render(request, "add_cables.html")

# <---------------------------------------patient_--------------------->


def patient(request):
    patientForm = PatientForm()

    if request.method == "POST":
        patientForm = PatientForm(request.POST)
        surname = request.POST.get('surname')
        first_name = request.POST.get('first_name')
        if patientForm.is_valid():
            if Patient.objects.filter(surname=surname, first_name=first_name).exists():
                messages.add_message(request, messages.ERROR,
                                     "Patient is already registered")
                return render(request, 'Patient/add_patient.html')
            else:
                patientForm.save()
                messages.add_message(request, messages.SUCCESS,
                                     f"Patient {surname}  {first_name} added successfully")
                return redirect('patient-table')

    return render(request, 'Patient/add_patient.html', {'form': patientForm})


def patient_table(request):
    patient = Patient.objects.all()
    return render(request, 'Patient/patient_table.html', {'patients': patient})


def physio_session(request):
    physioSessionForm = PhysioSessionForm()
    if request.method == "POST":

        # physioSession = PhysioSessionForm(request.POST)
        therapy_id = request.POST.get("therapy")
        diagnosis_id = request.POST.get("diagnosis")
        doctor_id=  request.POST.get("doctor")
        receipt_no = request.POST.get("receipt_no")
        date_of_visit =request.POST.get('date_of_visit')
        patient_id = request.POST.get('id')
        ward_id = request.POST.get('ward')
        patient = Patient.objects.get(id=patient_id)
        doctor = Doctor.objects.get(id=doctor_id)
        therapy = Therapy.objects.get(id=therapy_id)
        diagnosis = Diagnosis.objects.get(id=diagnosis_id)
        ward   = Ward.objects.get(id=ward_id)
        user = request.user.pk

        user = CustomUser.objects.get(id=user)
        print(user)
        physiosession = PhysioSession.objects.create(therapy=therapy, diagnosis=diagnosis, doctor=doctor, receipt_no=receipt_no, date_of_visit=date_of_visit, patient='ooo', therapist=user, ward=ward)
        physiosession.save()
        messages.add_message(request, messages.SUCCESS, "Physio Session booked successfully")
        return redirect('physio-session-table')
    return render(request, 'Patient/add_physio_session.html', {'form': physioSessionForm})

def physio_session_table(request):
    physioSession = PhysioSession.objects.all()
    
    return render(request, 'Patient/physio_session_table.html', {'physioSessions': physioSession})
#  <------- HTMX ---------->


def search_patient(request):
    pass


def get_patient(request, pk):
    res = "not thing much"
    pk = f"P{pk}"
    print
    p = get_object_or_404(Patients, pk=pk)
    print(p)
    res = { 
            "pk": "",
            "surname": p.lastname,
            'firstname':p.firstname,
            "pin_no": p.patientno,
            "patient_type": "",

        }
    return JsonResponse({"data": res}, status=200)

# @csrf_exempt
# def search_patient(request):
#     search_text = request.POST.get('search')
#     results = Patient.objects.filter(surname__icontains=search_text)
#     context = {'results': results}
#     # return render(request, '_partials/search.html', context)
#     res = None
#     data = []
#     if len(results) > 0 and len(search_text) > 0:
#         for i in results:
#             item = {
#                 "pk": i.pk,
#                 "name": i.surname,
#                 "pin no": i.pin_no,
#                 "patinet type": i.patient_type,
#             }
#             data.append(item)
#         res = data
#     else:
#         res = "No games found ........"

#             # return JsonResponse({"data": list(qs.values())})
#         # print(qs)
#         return render(request, '_partials/search.html', {"results": res})
#     return render(request, '_partials/search.html', {"results":"res"})
# <--------------------ward-------------------------------->
def add_ward(request):
    wardform = WardForm()
    if request.method == "POST":
        name = request.POST.get('name')
        if Ward.objects.filter(name=name).exists():
            messages.add_message(request, messages.ERROR,
                                 "Ward is already registered")
            return render(request, 'ward/add_ward.html')

        wardform = WardForm(request.POST)
        if wardform.is_valid():
            wardform.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"Ward {name} added successfully")
            return redirect('ward-table')
    return render(request, 'ward/add_ward.html', {'form': wardform})

def  ward_table(request):
    ward = Ward.objects.all()
    
    return render(request, 'ward/ward_table.html', {'wards': ward})
# <--------------------------------doctors-------------------------------------->
def add_doctor(request):
    doctorform = DoctorForm()
    if request.method == "POST":
        name = request.POST.get('name')
        doctorform = DoctorForm(request.POST)
        if doctorform.is_valid():
            doctorform.save()
            print("cleaned data", doctorform.cleaned_data)

            messages.add_message(request, messages.SUCCESS,
                                 f"Doctor {name} added successfully")
            return redirect('doctor-table')

        else:
            messages.add_message(request, messages.ERROR,
                                 "Doctor is already registered")
            return redirect('add-doctor')
    return render(request, 'doctor/add_doctor.html', {'form': doctorform})


def doctor_table(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctor/doctor_table.html', {'doctors': doctor})


# <--------------------------------Diagonsis-------------------------------------->

def add_diagnosis(request):
    diagnosisForm = DiagnosisForm()
    if request.method == "POST":
        name = request.POST.get('name')
        diagnosisform = DiagnosisForm(request.POST)
        if diagnosisform.is_valid():
            diagnosisform.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"Diagnosis {name} added successfully")
            return redirect('diagnosis-table')

        else:
            messages.add_message(request, messages.ERROR,
                                 "Diagnosis is already registered")
            return redirect('add-diagnosis')
    return render(request, 'Diagnosis/add_diagnosis.html', {'form': diagnosisForm})


def diagnosis_table(request):
    diganosis = Diagnosis.objects.all()
    return render(request, 'Diagnosis/diagnosis_table.html', {'diagnosiss': diganosis})
# <---------------------------------Therapy--------------------------->


def add_therapy(request):
    therapyForm = TherapyForm()
    if request.method == "POST":
        name = request.POST.get('name')
        therapyform = TherapyForm(request.POST)
        if therapyform.is_valid():
            therapyform.save()
            messages.add_message(request, messages.SUCCESS,
                                 f"Therapy {name} added successfully")
            return redirect('therapy-table')

        else:
            messages.add_message(request, messages.ERROR,
                                 "Therapy is already registered")
            return redirect('add-therapy')
    return render(request, 'Therapy/add_therapy.html', {'form': therapyForm})


def therapy_table(request):
    therapy = Therapy.objects.all()
    return render(request, 'Therapy/therapy_table.html', {'therapys': therapy})


def search_results(request):
    #! if request.is_ajax and request.method == "POST":
    #! checkin if request is ajax
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        
        name = request.POST.get("name").capitalize()
        res = None
        qs = Patients.objects.filter(patientno__icontains=name)
        data = []
        
        
        if len(qs) > 0 and len(name) > 0:
            for i in qs:
                item = {
                    # "pk": i.patientid,
                    "pin_no": i.patientno,
                    "name": i.firstname,
                    "surname": i.lastname,

                }
                data.append(item)
            res = data
        else:
            res = "No Patient not found ........"

            # return JsonResponse({"data": list(qs.values())})
        # print(qs)
        return JsonResponse({"data": res}, status=200)
    return JsonResponse({"data": "Not found"}, status=400)


def searchPatient(request):
    search_text = request.POST.get('search')
    qs = Patient.objects.filter(surname__icontains=search_text)
    data = []
    if len(qs) > 0 and len(search_text) > 0:
        for i in qs:
            item = {
                "pk": i.pk,
                "pin_no": i.pin_no,
                "surname": i.surname,
                "name": i.first_name,

            }
            data.append(item)
        res = data
        print(data)
        for d in data:
            print(d)
            pin_no = d.get("pin_no")
            surname = d.get('surname')
            name = d.get('name')
            full = f'{pin_no}  {surname} {name}'
            html = ('<div class="card-body">'
                    '<div class="list-group">'
                    '<a href="#" class="list-group-item list-group-item-action">{}</a>'
                    '</div>'

                    ' </div> '

                    ).format(full)
    else:
        res = "No patient not found ........"
        html = ('<div class="card-body">'
                '<div class="list-group">'
                '<a href="#" class="list-group-item list-group-item-action">{}</a>'
                '</div>'

                ' </div> ').format(res)
        return HttpResponse(html)
    print("error")

    return HttpResponse(html)
    # return HttpResponse("noo000000000000000")
