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
from patients.models import Patients, Visits, Extrabills, Paymentdetails, Admissions
from .models import Patient
import pandas as pd
from patients.models import Items
from django.db.models import Q
from django.db.models import F

# Returns the current local date

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


def dashboard(request):
    patients = Patient.objects.all().count()
    ward = Ward.objects.all()
    physio_sessions = PhysioSession.objects.all().count()
    inpatient = PhysioSession.objects.filter(patient_type="IN PATIENT").count()
    outpatient = PhysioSession.objects.filter(
        patient_type="OUT PATIENT").count()
    patient_month = PhysioSession.objects.filter(
        date__month=date.today().month).count()
    patient_last_month = PhysioSession.objects.filter(
        date__month=date.today().month-1).count()
    patient_quarter = PhysioSession.objects.filter(
        date__month__in=[1, 2, 3]).count()
    therapist = CustomUser.objects.filter(therapist=True)
    patient_year = PhysioSession.objects.filter(
        date__year=date.today().year).count()
    current_year = date.today().year

    last_year = date.today().year-1
    current_month = date.today().month
    last_month = date.today().month-1
    current_week = date.today().isocalendar()[1]
    last_week = date.today().isocalendar()[1]-1

    jan_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[1], date_of_visit__year=date.today().year-1).count()
    feb_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[2], date_of_visit__year=date.today().year-1).count()
    mar_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[3], date_of_visit__year=date.today().year-1).count()
    apr_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[4], date_of_visit__year=date.today().year-1).count()
    may_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[5], date_of_visit__year=date.today().year-1).count()
    jun_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[6], date_of_visit__year=date.today().year-1).count()
    jul_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[7], date_of_visit__year=date.today().year-1).count()
    aug_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[8], date_of_visit__year=date.today().year-1).count()
    sep_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[9], date_of_visit__year=date.today().year-1).count()
    oct_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[10], date_of_visit__year=date.today().year-1).count()
    nov_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[11], date_of_visit__year=date.today().year-1).count()
    dec_last_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[12], date_of_visit__year=date.today().year-1).count()
    physio_session_last_year = [jan_last_year, feb_last_year, mar_last_year, apr_last_year, may_last_year,
                                jun_last_year, jul_last_year, aug_last_year, sep_last_year, oct_last_year, nov_last_year, dec_last_year]

    # jan = PhysioSession.objects.filter(date_of_visit__month__in=[1]).count()
    # feb = PhysioSession.objects.filter(date_of_visit__month__in=[2]).count()
    # mar = PhysioSession.objects.filter(date_of_visit__month__in=[3]).count()
    # apr = PhysioSession.objects.filter(date_of_visit__month__in=[4]).count()
    # may = PhysioSession.objects.filter(date_of_visit__month__in=[5]).count()
    # jun = PhysioSession.objects.filter(date_of_visit__month__in=[6]).count()
    # jul = PhysioSession.objects.filter(date_of_visit__month__in=[7]).count()
    # aug = PhysioSession.objects.filter(date_of_visit__month__in=[8]).count()
    # sep = PhysioSession.objects.filter(date_of_visit__month__in=[9]).count()
    # oct = PhysioSession.objects.filter(date_of_visit__month__in=[10]).count()
    # nov = PhysioSession.objects.filter(date_of_visit__month__in=[11]).count()
    # dec = PhysioSession.objects.filter(date_of_visit__month__in=[12]).count()
    jan_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[1], date_of_visit__year=date.today().year).count()
    feb_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[2], date_of_visit__year=date.today().year).count()
    mar_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[3], date_of_visit__year=date.today().year).count()
    apr_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[4], date_of_visit__year=date.today().year).count()
    may_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[5], date_of_visit__year=date.today().year).count()
    jun_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[6], date_of_visit__year=date.today().year).count()
    jul_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[7], date_of_visit__year=date.today().year).count()
    aug_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[8], date_of_visit__year=date.today().year).count()
    sep_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[9], date_of_visit__year=date.today().year).count()
    oct_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[10], date_of_visit__year=date.today().year).count()
    nov_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[11], date_of_visit__year=date.today().year).count()
    dec_current_year = PhysioSession.objects.filter(
        date_of_visit__month__in=[12], date_of_visit__year=date.today().year).count()

    physio_session_current_year = [jan_current_year, feb_current_year, mar_current_year, apr_current_year, may_current_year,
                                   jun_current_year, jul_current_year, aug_current_year, sep_current_year, oct_current_year, nov_current_year, dec_current_year]
    print(physio_session_current_year)
    patient_last_year = PhysioSession.objects.filter(
        date__year=date.today().year-1)
    print(patient_month, patient_last_month, patient_quarter)

    context = {
        'ward': ward,
        'therapist': therapist,
        "current_year": current_year,
        "last_year": last_year,
        'patients': patients,
        'inpatient': inpatient,
        'outpatient': outpatient,
        'physio_sessions': physio_sessions,
        "physio_session_current_year": physio_session_current_year,
        "physio_session_last_year": physio_session_last_year,
    }

    return render(request, 'Dashboard/dashboard.html', context)


def day_report(request):
    pyhsio_sessions_day = PhysioSession.objects.filter(
        date_of_visit=date.today()).count()
    return HttpResponse(f'<span>{pyhsio_sessions_day}</span>')
# def week_report(request):
#     pyhsio_sessions = PhysioSession.objects.filter(date__week=date.today().isocalendar()[1])
#     return

# def month_report(request):
#     pyhsio_sessions = PhysioSession.objects.filter(date__month=date.today().month)


def ward_reports(request):
    wards = Ward.objects.all().order_by('-id')
    ward_count = []
    for w in wards:
        patient_count = PhysioSession.objects.filter(ward=w).count()
        ward_count.append(patient_count)
    return render(request, 'Ward/ward_report.html', {'wards': wards, "ward_count": ward_count})


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
        username = request.POST.get("department")
        password = request.POST.get("password")
        user = authenticate(
            requessername=username, password=password)
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


# @auth_user_should_not_access
def register_user(request):
    if request.method == "POST":
        context = {"has_error": False, "data": request.POST}
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        print(username, first_name, last_name, phone, password, password2)

        if len(password) < 6:
            messages.add_message(
                request, messages.ERROR, "Password should be at least 6 characters"
            )
            context["has_error"] = True
            return render(request, "register.html", context, status=409)

        if password != password2:
            messages.add_message(request, messages.ERROR, "Password mismatch")
            context["has_error"] = True

        if CustomUser.objects.filter(username=username).exists():
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
            username=username, first_name=first_name, last_name=last_name, phone_number=phone)

        user.therapist = True
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS,
                             f"{user.username} Registered successfully")
        return redirect('register')

    # if request.method == "GET":
    #     df = pd.read_csv('therapist.csv')
    #     surname = df['Surname']
    #     last_name = df['First name']
    #     df_dict = pd.DataFrame().assign(
    #         surname=surname, last_name=last_name).to_dict(orient='records')
    #     for x in df_dict:
    #         user = CustomUser.objects.create_user(
    #             username=x['surname'], first_name=x['last_name'], last_name=x['surname'], phone_number='123456789')
    #         user.therapist = True
    #         user.set_password('123456')
    #         user.save()

    return render(request, "register.html")


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
        doctor_id = request.POST.get("doctor")
        receipt_no = request.POST.get("receipt_no")
        date_of_visit = request.POST.get('date_of_visit')
        patient_no = request.POST.get('patient_pin')
        patient_name = request.POST.get('patient_name')
        patient_surname = request.POST.get('patient_surname')
        patient_type = request.POST.get('patient_type')
        ward_id = request.POST.get('ward')
        doctor = Doctor.objects.get(id=doctor_id)
        diagnosis = Diagnosis.objects.get(id=diagnosis_id)
        ward = Ward.objects.get(id=ward_id)
        user = request.user.pk
        therapy = therapy_id.split(',')

        user = CustomUser.objects.get(id=user)
        print(user)
        physiosession = PhysioSession.objects.create(diagnosis=diagnosis, doctor=doctor, receipt_no=receipt_no, date_of_visit=date_of_visit,
                                                     therapist=user, ward=ward, patient_no=patient_no, patient_name=patient_name, patient_type=patient_type, patient_surname=patient_surname)

        physiosession.save()
        physiosession.therapy.add(therapy)

        messages.add_message(request, messages.SUCCESS,
                             "Physio Session booked successfully")
        return redirect('physio-session-table')
    # if request.method == "GET":
    #     PhysioSession.objects.filter(patient_type='OUT PATIENT').delete()
    #     df = pd.read_csv('out_patient.csv').to_dict('records')
    #     # df ={'Surname': 'Mwesigye', 'First_Name': 'Emma', 'Date': '2022-07-11', 'Doctor': 'Kyazze solomon', 'Diagnosis': 'Lumbar and cervical spondylosis', 'Therapy': 'Orthotics', 'Therapist': 'Mugalu', 'Ward': 'Others', 'Receipt': 'R22-131059', 'Pin_Nr': 'P220023980'},
    #     for i in df:
    #         # if it does not exist
    #         if not CustomUser.objects.filter(username=str(i['Therapist']).strip().capitalize()).exists():
    #             print(i['Therapist'])
    #             therapist = CustomUser.objects.create_user(username=i['Therapist'], password='12345678', email=i['Therapist']+'@gmail.com',
    #                                                        first_name=i['Therapist'], last_name=i['Therapist'], is_staff=True, is_active=True, is_superuser=False, therapist=True)
    #             therapist.save()
    #         if not  Ward.objects.filter(name=i['Ward']).exists():
    #             print(i['Ward'])
    #         # if not  Therapy.objects.filter (name=i['Therapy']).exists():
    #         #     print(i['Therapy'])
    #         #     therapy = Therapy.objects.create(name=i['Therapy'])
    #         #     therapy.save()

    #         if not Doctor.objects.filter(name=i['Doctor']).exists():
    #             print(i['Doctor'])
    #             doctor = Doctor.objects.create(name=i['Doctor'])
    #             doctor.save()

    #         if not  Diagnosis.objects.filter(name=i['Diagnosis']).exists():
    #             print(i['Diagnosis'])
    #             diagnosis = Diagnosis.objects.create(name=i['Diagnosis'])
    #             diagnosis.save()
    #         physio_session = PhysioSession.objects.create(date_of_visit=str(i['Date']), receipt_no=i['Receipt'], patient_no=i['Pin_Nr'], patient_name=i['First_Name'],
    #                                                       patient_surname=i['Surname'], patient_type='OUT PATIENT', ward=Ward.objects.get(name=i['Ward']), doctor=Doctor.objects.get(name=i['Doctor']), therapist=CustomUser.objects.get(username=i['Therapist']),
    #                                                       diagnosis=Diagnosis.objects.get(
    #                                                         name=i['Diagnosis']),
    #                                                         old_therapy=i['Therapy'])

    #         physio_session.save()
    #         messages.add_message(
    #             request, messages.SUCCESS, f"Physio Session {i['Surname']} booked successfully")

    return render(request, 'Patient/add_physio_session.html', {'form': physioSessionForm})


def physio_session_table(request):
    physioSession = PhysioSession.objects.all().order_by('-id')[0:100]

    return render(request, 'Patient/physio_session_table.html', {'physioSessions': physioSession})
#  <------- HTMX ---------->


def get_patient(request, pk):
    res = "not thing much"
    pk = f"P{pk}"
    p = get_object_or_404(Patients, pk=pk)

    # pt=Paymentdetails.objects.filter(visitno__visitno="P2300000010001").select_related("receiptno").filter(Q(itemcode="PHS04") | Q(itemcode="PHS004") |Q(itemcode="PH0010"))
    # showw all the  p method
    print(p.totalvisits)
    if p.totalvisits == None:
        print("it runser")
        messages.add_message(request, messages.ERROR,
                             "Please first register for a visit")
        return redirect('physio-session')

    else:
        # pick the last visit in the list
        visit_no = str(Visits.objects.filter(
            patientno__patientno=p.patientno).order_by('-visitid')[0])
        print(visit_no)
        res = {
            "pk": "",
            "surname": p.lastname,
            'firstname': p.firstname,
            "pin_no": p.patientno,
            "visit_no": visit_no,
            "patient_type": "",
            "receipt_no": "",
            "invoice_no": "",
            "extra_billno": "",
            "admission_no": "",
            "patient_type": "",
        }
        try:
            receipt = Paymentdetails.objects.filter(visitno__visitno=f"{res['visit_no']}").select_related(
                "receiptno").filter(Q(itemcode="PHS04") | Q(itemcode="PHS004") | Q(itemcode="PH0010")).values()
            if receipt.exists():
                receipt_no_dic = receipt[0]
                new_receipt_no = receipt_no_dic['receiptno_id']
                res['receipt_no'] = new_receipt_no
                if 'invoice_no' in res:
                    del res['invoice_no']

                res["patient_type"] = "OUT-PATIENT"
                print(res)

                print({"receipt": res["receipt_no"]})

            elif Items.objects.filter(visitno=f"{res['visit_no']}").exists():
                for i in Items.objects.filter(visitno=f"{res['visit_no']}"):
                    if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
                        res['invoice_no'] = i.invoiceno
                        if 'receipt_no' in res:
                            del res['receipt_no']
                        res["patient_type"] = "OUT-PATIENT"
                        print(res)

                        print({"invoice": res["invoice_no"]})
            # if Extrabills.objects.filter(visitno=f"{res['visit_no']}").exists():
            #     # Extrabills.objects.filter(
            #     #     visitno=f"{res['visit_no']}").exists()
            #     print("it is working")
            #     for i in Extrabills.objects.filter(visitno=f"{res['visit_no']}"):
            #         # if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
            #         res['invoice_no'] = "no_invoice"
            #         res['receipt_no'] = "no_receipt"
            #         res['extra_bill_no'] = i.extrabillno
            #         admissin_no = Admissions.objects.get(
            #             visitno=f"{res['visit_no']}").admissionno
            #         res['admission_no'] = admissin_no
            #         res["patient_type"] = "IN-PATIENT"
            #         print(res)
            #         print({"admission": res["admission_no"]})

        except:
            print("it is not working")
            messages.add_message(request, messages.ERROR,
                                 "Please first register for a visit")
            return render(request, 'Patient/add_physio_session.html')
        print(res)
        if Extrabills.objects.filter(visitno=f"{res['visit_no']}").exists():
            # Extrabills.objects.filter(
            #     visitno=f"{res['visit_no']}").exists()
            print("it is working")
            for i in Extrabills.objects.filter(visitno=f"{res['visit_no']}"):
                # if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
                print(i.extrabillno)

                res['extra_bill_no'] = i.extrabillno
                if 'receipt_no' in res:
                    del res['receipt_no']

                if 'invoice_no' in res:
                    del res['invoice_no']

                admission_no = Admissions.objects.get(
                    visitno=f"{res['visit_no']}").admissionno
                res['admission_no'] = admission_no
                res["patient_type"] = "IN-PATIENT"
                print({"admission": res["admission_no"]})
        print(res)
        return JsonResponse({"data": res}, status=200)

    # try:
    #     receipt=Paymentdetails.objects.filter(visitno__visitno=f"{res['visit_no']}").select_related("receiptno").filter(Q(itemcode="PHS04") | Q(itemcode="PHS004") |Q(itemcode="PH0010")).values()
    #     receipt_no_dic = receipt[0]
    #     new_receipt_no = receipt_no_dic['receiptno_id']
    #     res['receipt_no']=new_receipt_no
    #     print(res)
    #     print(receipt)
    # except:
    #     messages.add_message(request, messages.ERROR,"Please first register for a visit")
    #     return render(request, 'Patient/add_physio_session.html')

    # p = Paymentdetails.objects.filter(visitno__visitno=f"{res['visit_no']}").select_related("receiptno").get(itemcode__items="PHS004")
    # z = Paymentdetails.objects.filter(
    #     visitno__visitno=f"{res['visit_no']}").prefetch_related('itemcode')
    # items = Items.objects.filter(visitno__visitno=f"{res['visit_no']}")
    # test = Paymentdetails.objects.select_related("receiptno")
    # print(z)

    # for t in p:

    #     print('hello')
    #     print(t.receiptno)
        # print(t.visitno)
    # for i in items:
    #     if i.itemcode == "PHS004" or i.itemcode == "PHS005" or i.itemcode == "PHS0010":
    #         p = i

    # print(items)
    # for i in p:
    #     # print(i.itemcode)
    #     print(i.my_itemcode)
    # item = Items.objects.get(visitno=res['visit_no'])
    # print(item)d
    # items = Items.objects.filter(visitno__visitno=f"{res['visit_no']}")

    # for i in items:
    #     if i.itemcode == "PHS004" or i.itemcode == "PHS005" or i.itemcode == "PHS0010":
    #         print(i)
    #         print(p)


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


def ward_table(request):
    ward = Ward.objects.all()

    # df = pd.read_csv('ward.csv')
    # df_ward = df["Ward"].to_list()
    # for x in df_ward:
    #     ward1 = Ward.objects.create(name=x)
    #     ward1.save()
    #     messages.add_message(request, messages.SUCCESS,
    #  f"Ward {x} added successfully")
    return render(request, 'ward/ward_table.html', {'wards': ward})


def check_ward(request):
    ward = request.POST.get('name')
    name_split = ward.split(' ')
    first_name = str(name_split[0]).capitalize()
    last_name = str(name_split[1]).capitalize()
    full_name = f"{first_name} {last_name}"
    # when u add .exists it returns true or false
    if Ward.objects.filter(name=full_name).exists():
        print('true')
        return HttpResponse('<div style="color:red;"> This Ward is already registered</div>')
    else:
        return HttpResponse('<div style="color:green;"> This is Ward name is Ok </div>')


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
    doctor = Doctor.objects.all().order_by('name')

    # df_doctor = pd.read_csv('doctor.csv').drop_duplicates()
    # df_doctor_name = df_doctor['Doctor']
    # df_doctor_description = df_doctor['Status']
    # df = pd.DataFrame({'Doctor': df_doctor_name, 'Description': df_doctor_description})
    # doctor_dict = df.to_dict('records')
    # for d in doctor_dict:
    #     print(d)
    #     doctor1 = Doctor.objects.create(name=d['Doctor'], specialist=d['Description'])
    #     doctor1.save()
    # print(doctor_dict)

    return render(request, 'doctor/doctor_table.html', {'doctors': doctor})


def check_doctor(request):
    doctor = request.POST.get('name')
    name_split = doctor.split(' ')
    first_name = str(name_split[0]).capitalize()
    last_name = str(name_split[1]).capitalize()
    full_name = f"{first_name} {last_name}"
    print(full_name)
    # when u add .exists it returns true or false
    if Doctor.objects.filter(name=full_name).exists():
        print('true')
        return HttpResponse('<div style="color:red;"> This Doctor is already registered</div>')
    else:
        return HttpResponse('<div style="color:green;"> This is Doctor is Ok </div>')


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
    # fetch diagnosis basicing on  all the diagnosis order by  alphabetically
    diagnosis = Diagnosis.objects.all().order_by('name')
    # df = pd.read_csv('diagnosis.csv')
    # df_diagnosis = df["Diagnosis"].to_list()
    # for x in df_diagnosis:
    #     diagnosis1 = Diagnosis.objects.create(name=x)
    #     diagnosis1.save()
    #     messages.add_message(request, messages.SUCCESS,
    #                          f"Diagnosis {x} added successfully")
    return render(request, 'Diagnosis/diagnosis_table.html', {'diagnosiss': diagnosis})


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
    therapy = Therapy.objects.all().order_by('name')

    # df_therapy = pd.read_csv('therapy.csv')
    # df_therapy = df_therapy.drop_duplicates()
    # df_therapy = df_therapy['Therapy'].to_list()
    # for x in  df_therapy:
    #     therapy_create = Therapy.objects.create(
    #         name=x,
    #         )
    #     therapy_create.save()
    #     messages.add_message(request, messages.SUCCESS, f"Therapy added successfully")

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

                # print(f"{str(i.patientno)}000{str(i.totalvisits)}")
                data.append(item)
            res = data
        else:
            res = "No Patient not found ........"

            # return JsonResponse({"data": list(qs.values())})
        # print(qs)
        return JsonResponse({"data": res}, status=200)
    return JsonResponse({"data": "Not found"}, status=400)
