from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import UserForm
from .models import *
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.urls import reverse
from .decorators import auth_user_should_not_access
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
from django.http import JsonResponse, HttpResponseRedirect

# Import date class from datetime module
from datetime import date, time
from django.utils import timezone
from patients.models import Patients, Visits, Extrabills, Paymentdetails, Admissions
from .models import Patient
import pandas as pd
from patients.models import Items
from django.db.models import Q
from django.db.models import F
from django.forms.models import model_to_dict

from django.utils.timezone import make_aware
import xlwt
from django.db.models import CharField, Value
from django.db.models.functions import Concat


from .models import Patient

# Returns the current local date

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


def dashboard(request):
    # patients = Patient.objects.all().count()
    # ward = Ward.objects.all()
    # physio_sessions = PhysioSessionAdmission.objects.all().count()
    # inpatient = PhysioSessionAdmission.objects.filter(patient_type="IN PATIENT").count()
    # outpatient = PhysioSessionAdmission.objects.filter(
    #     patient_type="OUT PATIENT"
    # ).count()
    # patient_month = PhysioSessionAdmission.objects.filter(
    #     date__month=date.today().month
    # ).count()
    # patient_last_month = PhysioSessionAdmission.objects.filter(
    #     date__month=date.today().month - 1
    # ).count()
    # patient_quarter = PhysioSessionAdmission.objects.filter(
    #     date__month__in=[1, 2, 3]
    # ).count()
    # therapist = CustomUser.objects.filter(therapist=True)
    # patient_year = PhysioSessionAdmission.objects.filter(
    #     date__year=date.today().year
    # ).count()
    # current_year = date.today().year

    # last_year = date.today().year - 1
    # current_month = date.today().month
    # last_month = date.today().month - 1
    # current_week = date.today().isocalendar()[1]
    # last_week = date.today().isocalendar()[1] - 1

    # jan_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[1], date_of_visit__year=date.today().year - 1
    # ).count()
    # feb_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[2], date_of_visit__year=date.today().year - 1
    # ).count()
    # mar_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[3], date_of_visit__year=date.today().year - 1
    # ).count()
    # apr_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[4], date_of_visit__year=date.today().year - 1
    # ).count()
    # may_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[5], date_of_visit__year=date.today().year - 1
    # ).count()
    # jun_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[6], date_of_visit__year=date.today().year - 1
    # ).count()
    # jul_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[7], date_of_visit__year=date.today().year - 1
    # ).count()
    # aug_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[8], date_of_visit__year=date.today().year - 1
    # ).count()
    # sep_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[9], date_of_visit__year=date.today().year - 1
    # ).count()
    # oct_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[10], date_of_visit__year=date.today().year - 1
    # ).count()
    # nov_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[11], date_of_visit__year=date.today().year - 1
    # ).count()
    # dec_last_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[12], date_of_visit__year=date.today().year - 1
    # ).count()
    # physio_session_last_year = [
    #     jan_last_year,
    #     feb_last_year,
    #     mar_last_year,
    #     apr_last_year,
    #     may_last_year,
    #     jun_last_year,
    #     jul_last_year,
    #     aug_last_year,
    #     sep_last_year,
    #     oct_last_year,
    #     nov_last_year,
    #     dec_last_year,
    # ]

    # # jan = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[1]).count()
    # # feb = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[2]).count()
    # # mar = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[3]).count()
    # # apr = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[4]).count()
    # # may = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[5]).count()
    # # jun = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[6]).count()
    # # jul = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[7]).count()
    # # aug = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[8]).count()
    # # sep = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[9]).count()
    # # oct = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[10]).count()
    # # nov = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[11]).count()
    # # dec = PhysioSessionAdmission.objects.filter(date_of_visit__month__in=[12]).count()
    # jan_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[1], date_of_visit__year=date.today().year
    # ).count()
    # feb_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[2], date_of_visit__year=date.today().year
    # ).count()
    # mar_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[3], date_of_visit__year=date.today().year
    # ).count()
    # apr_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[4], date_of_visit__year=date.today().year
    # ).count()
    # may_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[5], date_of_visit__year=date.today().year
    # ).count()
    # jun_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[6], date_of_visit__year=date.today().year
    # ).count()
    # jul_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[7], date_of_visit__year=date.today().year
    # ).count()
    # aug_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[8], date_of_visit__year=date.today().year
    # ).count()
    # sep_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[9], date_of_visit__year=date.today().year
    # ).count()
    # oct_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[10], date_of_visit__year=date.today().year
    # ).count()
    # nov_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[11], date_of_visit__year=date.today().year
    # ).count()
    # dec_current_year = PhysioSessionAdmission.objects.filter(
    #     date_of_visit__month__in=[12], date_of_visit__year=date.today().year
    # ).count()

    # physio_session_current_year = [
    #     jan_current_year,
    #     feb_current_year,
    #     mar_current_year,
    #     apr_current_year,
    #     may_current_year,
    #     jun_current_year,
    #     jul_current_year,
    #     aug_current_year,
    #     sep_current_year,
    #     oct_current_year,
    #     nov_current_year,
    #     dec_current_year,
    # ]
    # print(physio_session_current_year)
    # patient_last_year = PhysioSessionAdmission.objects.filter(
    #     date__year=date.today().year - 1
    # )
    # print(patient_month, patient_last_month, patient_quarter)

    # context = {
    #     "ward": ward,
    #     "therapist": therapist,
    #     "current_year": current_year,
    #     "last_year": last_year,
    #     "patients": patients,
    #     "inpatient": inpatient,
    #     "outpatient": outpatient,
    #     "physio_sessions": physio_sessions,
    #     "physio_session_current_year": physio_session_current_year,
    #     "physio_session_last_year": physio_session_last_year,
    # }

    return render(request, "Dashboard/dashboard.html", context={})


def day_report(request):
    pyhsio_sessions_day = PhysioSessionAdmission.objects.filter(
        date_of_visit=date.today()
    ).count()
    return HttpResponse(f"<span>{pyhsio_sessions_day}</span>")


# def week_report(request):
#     pyhsio_sessions = PhysioSessionAdmission.objects.filter(date__week=date.today().isocalendar()[1])
#     return

# def month_report(request):
#     pyhsio_sessions = PhysioSessionAdmission.objects.filter(date__month=date.today().month)


def ward_reports(request):
    wards = Ward.objects.all().order_by("-id")
    ward_count = []
    for w in wards:
        patient_count = PhysioSessionAdmission.objects.filter(ward=w).count()
        ward_count.append(patient_count)
    return render(
        request, "Ward/ward_report.html", {"wards": wards, "ward_count": ward_count}
    )


@auth_user_should_not_access
def login_user(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get("department")
        password = request.POST.get("password")
        user = authenticate(requessername=username, password=password)
        if not user:
            print("test3")
            messages.add_message(
                request, messages.ERROR, "Invalid credentials, try again"
            )
            return render(request, "login.html", context, status=401)
        login(request, user)
        messages.add_message(request, messages.SUCCESS, f"Welcome {user.username}")
        return redirect("home")

    return render(request, "login.html", context)


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
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone,
        )

        user.therapist = True
        user.set_password(password)
        user.save()
        messages.add_message(
            request, messages.SUCCESS, f"{user.username} Registered successfully"
        )
        return redirect("register")

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
    phone = request.POST.get("phone")
    print(phone)

    # when u add .exists it returns true or false
    if phone.isdigit():
        if CustomUser.objects.filter(phone_number=phone).exists():
            print("true")
            return HttpResponse(
                '<div style="color:red;"> This Phone is already registered</div>'
            )

        else:
            print("false")
            return HttpResponse('<div style="color:green;"> This is Phone is Ok </div>')

    else:
        return HttpResponse(
            '<div style="color:red;"> This Phone is should be a digit</div>'
        )


def check_password(request):
    password = request.POST.get("password")
    password2 = request.POST.get("password2")
    print(password, password2)
    if len(password) < 6:
        return HttpResponse(
            '<div style="color:red;"> This Password is should be greater than 6</div>'
        )

    if password != password2:
        return HttpResponse(
            '<div style="color:red;"> This Password1 is not equal to Password2</div>'
        )
    else:
        return HttpResponse('<div style="color:green;"> This is password is Ok </div>')


def check_phone_2(request):
    phone = request.POST.get("contact")
    print(phone)

    # when u add .exists it returns true or false
    if phone.isdigit():
        return HttpResponse('<div style="color:green;"> This is Phone is Ok </div>')

    else:
        print("false")
        return HttpResponse(
            '<div style="color:red;"> This Phone is should be digits</div>'
        )


def current_date(request):
    print(request.POST)
    date_1 = request.POST.get("date")
    year = date_1.split("-")[0].split("0")[1]
    month = date_1.split("-")[1]
    day = date_1.split("-")[2]
    date_final = year + "-" + month + "-" + day
    print(date_final)
    today = date.today().strftime("%y-%m-%d")
    print(today)
    if date_final < today:
        return HttpResponse(
            '<div style="color:red;"> This Date is should be greater than today</div>'
        )
    else:
        return HttpResponse('<div style="color:green;"> This is Date is Ok </div>')


def check_time(request):
    time = request.POST.get("time")
    end_time = request.POST.get("end_time")
    start = int(time.split(":")[0])
    end = int(end_time.split(":")[0])
    print(time, end_time)
    print(start, end)
    if start < end:
        if 7 <= start <= 18 and 7 <= end <= 18:
            print("true")
            return HttpResponse('<div style="color:green;"> This is Time is Ok </div>')

        else:
            return HttpResponse(
                '<div style="color:red;"> This Time is should be between 7am to 6pm</div>'
            )
    return HttpResponse(
        '<div style="color:red;"> End Time should greater than Start Time</div>'
    )


#! <---------------------------------------patient--------------------->


def patient(request):
    patientForm = PatientForm()

    if request.method == "POST":
        patientForm = PatientForm(request.POST)
        surname = request.POST.get("surname")
        first_name = request.POST.get("first_name")
        if patientForm.is_valid():
            if Patient.objects.filter(surname=surname, first_name=first_name).exists():
                messages.add_message(
                    request, messages.ERROR, "Patient is already registered"
                )
                return render(request, "Patient/add_patient.html")
            else:
                patientForm.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    f"Patient {surname}  {first_name} added successfully",
                )
                return redirect("patient-table")

    return render(request, "Patient/add_patient.html", {"form": patientForm})


def patient_table(request):
    patient = Patient.objects.all()
    return render(request, "Patient/patient_table.html", {"patients": patient})


def patient_registration(request):
    physioSessionAdmissionForm = PhysioSessionAdmissionForm()
    if request.method == "POST":
        date_of_visit = str(request.POST.get("date_of_visit"))
        date_of_birth = str(request.POST.get("date_of_birth")).split("T")[0]

        receipt_no = request.POST.getlist("receipt_no")
        quantity = request.POST.getlist("quantity")
        totalquantity = request.POST.get("totalquantity")
        patient_surname = request.POST.get("patient_surname")
        patient_name = request.POST.get("patient_name")
        patient_type = request.POST.get("patient_type")
        more_notes = request.POST.get("more_notes")
        patient_pin = request.POST.get("patient_pin")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        visit_no = request.POST.getlist("visit_no")
        diagnosis = Diagnosis.objects.get(id=request.POST.get("diagnosis"))
        doctor = Doctor.objects.get(id=request.POST.get("doctor"))
        gender = request.POST.get("gender")
        print(date_of_birth)
        print(request.POST)

        if Patient.objects.filter(patient_no=patient_pin).exists():
            patient = Patient.objects.get(patient_no=patient_pin).patient_no
            messages.add_message(
                request, messages.ERROR, "Patient is all ready regisetered"
            )

            return redirect("patient_profile", pk=patient)

        patient = Patient.objects.create(
            gender=gender,
            address=address,
            date_of_birth=date_of_birth,
            phone_number=phone,
            surname=patient_surname,
            first_name=patient_name,
            patient_no=patient_pin,
        )

        physiosessionadmission = PhysioSessionAdmission.objects.create(
            therapist=request.user,
            doctor=doctor,
            date_of_visit=date_of_visit,
            diagnosis=diagnosis,
            more_notes=more_notes,
            # ward=ward,
            patient_type=patient_type,
            patient=patient,
            quantity_of_sessions=totalquantity,
        )

        for quan, rec, vis in zip(quantity, receipt_no, visit_no):
            receipt = Receipt.objects.create(
                physiosessionadmission=physiosessionadmission,
                receipt_number=rec,
                quantity_of_session=quan,
                payment_date=date_of_visit,
                visit_no=vis,
            )

        messages.add_message(
            request, messages.SUCCESS, "Patient Registered successfully"
        )
        return redirect("patient-registration")
    # if request.method == "GET":
    #     PhysioSessionAdmission.objects.filter(patient_type='OUT PATIENT').delete()
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
    #         physio_session = PhysioSessionAdmission.objects.create(date_of_visit=str(i['Date']), receipt_no=i['Receipt'], patient_no=i['Pin_Nr'], patient_name=i['First_Name'],
    #                                                       patient_surname=i['Surname'], patient_type='OUT PATIENT', ward=Ward.objects.get(name=i['Ward']), doctor=Doctor.objects.get(name=i['Doctor']), therapist=CustomUser.objects.get(username=i['Therapist']),
    #                                                       diagnosis=Diagnosis.objects.get(
    #                                                         name=i['Diagnosis']),
    #                                                         old_therapy=i['Therapy'])

    #         physio_session.save()
    #         messages.add_message(
    #             request, messages.SUCCESS, f"Physio Session {i['Surname']} booked successfully")

    return render(
        request, "Patient/add_physio_session.html", {"form": physioSessionAdmissionForm}
    )


def inpatient_registration(request):
    physioSessionAdmissionForm = PhysioSessionAdmissionForm()
    if request.method == "POST":
        data = request.POST
        patient_name = data["patient_name"]
        patient_surname = data["patient_surname"]
        patient_pin = data["patient_pin"]
        date_of_visit = data["date_of_visit"]
        admission_no = data["admission_no"]
        patient_type = data["patient_type"]
        more_notes = data["more_notes"]
        address = data["address"]
        phone = data["phone"]
        date_of_birth = str(request.POST.get("date_of_birth")).split("T")[0]
        gender = data["gender"]

        diagnosis = Diagnosis.objects.get(id=data["diagnosis"])
        doctor = Doctor.objects.get(id=data["doctor"])
        ward = Ward.objects.get(id=data["ward"])
        print(request.POST)
        if Patient.objects.filter(patient_no=patient_pin).exists():
            patient = Patient.objects.get(patient_no=patient_pin).patient_no
            messages.add_message(
                request, messages.ERROR, "Patient is all ready regisetered"
            )

            return redirect("patient_profile", pk=patient)
        patient = Patient.objects.create(
            gender=gender,
            address=address,
            date_of_birth=date_of_birth,
            phone_number=phone,
            surname=patient_surname,
            first_name=patient_name,
            patient_no=patient_pin,
        )

        physiosessionadmission = PhysioSessionAdmission.objects.create(
            therapist=request.user,
            doctor=doctor,
            date_of_visit=date_of_visit,
            diagnosis=diagnosis,
            more_notes=more_notes,
            ward=ward,
            clinic_master_admission_no=admission_no,
            patient_type=patient_type,
            patient=patient,
        )

        messages.add_message(
            request, messages.SUCCESS, "Patient Registered successfully"
        )
    return render(
        request,
        "Patient/in_patient_registration.html",
        {"form": physioSessionAdmissionForm},
    )


def back_date_registration(request):
    form_back_date = BackDate()
    PhysioSessionAdmissionForm = PhysioSessionAdmissionForm()
    res = None
    if request.method == "POST":
        # print(request.POST)
        date = request.POST["date"]
        patient_no = request.POST["patient_no"]
        patient_type = request.POST["patient_type"]
        p = get_object_or_404(Patients, pk=patient_no)
        res = {
            "visit_date": "",
            "pk": "",
            "surname": p.lastname,
            "firstname": p.firstname,
            "pin_no": p.patientno,
            "visit_no": [],
            "patient_type": "",
            "receipt_no": [],
            "invoice_no": [],
            "extra_billno": "",
            "admission_no": "",
            "patient_type": "",
        }
        visits = Visits.objects.filter(patientno__patientno=patient_no)

        # formatted_visits = [visit.visitdate.strftime("%Y-%m-%d")  for visit in visits ]
        formatted_visit = []
        for visit in visits:
            visitdate = visit.visitdate.strftime("%Y-%m-%d")
            if date in visitdate:
                format_visit = {
                    "visitno": visit.visitno,
                    "patientno": visit.patientno,
                    "visitdate": visit.visitdate.strftime("%Y-%m-%d"),
                }
                formatted_visit.append(format_visit)

            # else:
            #     res = None
            #     messages.add_message(request, messages.ERROR, "select the right date")
            #     return render(
            #         request,
            #         "Patient/back_date_registration.html",
            #         {
            #             "form": PhysioSessionAdmissionForm,
            #             "form_back_date": form_back_date,
            #         },
            #     )
        if len(formatted_visit) == 0:
            res = None
            messages.add_message(request, messages.ERROR, "select the right date")
            return render(
                request,
                "Patient/back_date_registration.html",
                {
                    "form": PhysioSessionAdmissionForm,
                    "form_back_date": form_back_date,
                },
            )

        print(formatted_visit)
        # u = Visits.objects.filter(
        #     patientno__patientno=patient_no, visitdate__range=given_date).exists()
        if len(formatted_visit) > 0:
            if patient_type == "outpatient":
                # if Visits.objects.filter(patientno__patientno=patient_no, visitdate=date).exists():
                for visit in formatted_visit:
                    receipt = (
                        Paymentdetails.objects.filter(visitno__visitno=visit["visitno"])
                        .select_related("receiptno")
                        .filter(
                            Q(itemcode="PHS04")
                            | Q(itemcode="PHS004")
                            | Q(itemcode="PH0010")
                        )
                        .values()
                    )

                    if receipt.exists():
                        receipt_no_dic = receipt[0]
                        print(receipt_no_dic)
                        new_receipt_no = receipt_no_dic["receiptno_id"]
                        new_visitno_id = receipt_no_dic["visitno_id"]
                        new_quantity = receipt_no_dic["quantity"]
                        new_unit_price = receipt_no_dic["unitprice"]
                        new_amount = receipt_no_dic["amount"]

                        #     # res['receipt_no'] = new_receipt_no

                        my_receipt_dic = {
                            "receiptno_id": new_receipt_no,
                            "visitno_id": new_visitno_id,
                            "quantity": new_quantity,
                            "unit_price": new_unit_price,
                            "amount": new_amount,
                        }
                        #     # print(receipt)
                        #     # print(my_receipt_dic)
                        print(res)
                        res["visit_date"] = visitdate
                        res["receipt_no"].append(my_receipt_dic)
                        print(res)
                    elif Items.objects.filter(visitno=visit["visitno"]).exists():
                        for i in Items.objects.filter(visitno=visit["visitno"]):
                            if (
                                i.itemcode == "PHS04"
                                or i.itemcode == "PHS004"
                                or i.itemcode == "PH0010"
                            ):
                                date = i.lastupdate
                                quantity = i.quantity
                                invoiceno = i.invoiceno
                                visitno_id = i.visitno_id
                                my_invoice_dic = {
                                    "invoiceno": invoiceno,
                                    "visitno_id": visitno_id,
                                    "quantity": quantity,
                                }
                                res["visitdate"] = visitdate
                                res["receipt_no"].append(my_invoice_dic)
                                print(res)
            else:
                messages.add_message(
                    request, messages.ERROR, "patient is not an out patient"
                )
                return render(
                    request,
                    "Patient/back_date_registration.html",
                    {
                        "form": PhysioSessionAdmissionForm,
                        "form_back_date": form_back_date,
                    },
                )

    return render(
        request,
        "Patient/back_date_registration.html",
        {
            "form": PhysioSessionAdmissionForm,
            "form_back_date": form_back_date,
            "res": res,
        },
    )


def get_in_patient(request, pk):
    res = "res"
    pk = f"P{pk}"
    p = get_object_or_404(Patients, pk=pk)

    # pt=Paymentdetails.objects.filter(visitno__visitno="P2300000010001").select_related("receiptno").filter(Q(itemcode="PHS04") | Q(itemcode="PHS004") |Q(itemcode="PH0010"))

    # showw all the  p method
    print(p.totalvisits)
    if p.totalvisits == None:
        messages.add_message(
            request, messages.ERROR, "Please first register for a visit"
        )
        return JsonResponse(
            {"message": "Please first register for a visit"}, status=400
        )

    else:
        visit = Visits.objects.filter(patientno__patientno=p.patientno)
        print(visit)
        # print(visit)
        visit_no = []  # initialize visit_no to None
        admission_list = []
        res = {
            "pk": "",
            "surname": p.lastname,
            "firstname": p.firstname,
            "pin_no": p.patientno,
            "date_of_birth": p.birthdate,
            "phone": p.phone,
            "gender": p.genderid.datades,
            "address": p.address,
            "visit_no": [],
            "patient_type": "",
            "receipt_no": [],
            "invoice_no": [],
            "extra_billno": "",
            "admission_no": "",
            "admission_date": "",
            "patient_type": "",
        }

        #! gabage code
        # for visit_number in visit:
        #     vist_date = visit_number.visitdate
        #     visit_no.append(visit_number)
        latest_visit = max(visit, key=lambda v: v.visitdate)
        admission_no = Admissions.objects.get(visitno=f"{latest_visit}")
        res["admission_no"] = (admission_no.admissionno,)
        res["admission_date"] = admission_no.admissiondatetime
        res["patient_type"] = "IN-PATIENT"

        print(res)
        return JsonResponse({"data": res}, status=200)
        # latest_dict = max(admission_list, key=lambda x: x['admission_date'])

        # if len(admission_list)>0:
        #     res["patient_type"] = "IN-PATIENT"
        #     res["admission_no"] = latest_dict["admission_no"]
        #     if 'invoice_no' in res:
        #         del res['invoice_no']
        #     if "receipt_no" in res:
        #         del res["receipt_no"]
        #     # print(latest_dict)
        #     if 'visit_no' in res:
        #         del res["visit_no"]
        #         print("adfa",res)

        #         final_res.append(latest_dict)
        #     # todays_date = str(datetime.date.today())
        #     # edited_visit_date = str(visit_number.visitdate).split()[0]
        #     # print(m)
        #     # print(visit_number)

        #     # if edited_visit_date == todays_date:
        #         # print("my visit date", edited_visit_date)
        #         # extra =Extrabills.objects.filter(visitno=f"{visit_number}").exists()
        #         # print("my",extra)
        #     print("my",visit_no)
        #     if Extrabills.objects.filter(visitno=f"{visit_number}").exists():
        #         extra =Extrabills.objects.filter(visitno=f"{visit_number}")
        #         print("my",extra)
        #         admission_no = Admissions.objects.get(visitno=f"{visit_number}")
        #         admission_info= {
        #             "admission_no":admission_no.admissionno,
        #             "admission_date":admission_no.admissiondatetime

        #         }
        #         print("john",admission_no)
        #         admission_list.append(admission_info)
        #         # print(admission_list)
        #         t= Extrabills.objects.filter(visitno=f"{visit_number}")


def get_patient(request, pk):
    res = "not thing much"
    pk = f"P{pk}"
    p = get_object_or_404(Patients, pk=pk)

    # pt=Paymentdetails.objects.filter(visitno__visitno="P2300000010001").select_related("receiptno").filter(Q(itemcode="PHS04") | Q(itemcode="PHS004") |Q(itemcode="PH0010"))

    # showw all the  p method

    if p.totalvisits == None:
        messages.add_message(
            request, messages.ERROR, "Please first register for a visit"
        )
        # return redirect("patient-registration")
        return JsonResponse(
            {"message": "Please first register for a visit"}, status=400
        )

    else:
        # pick the last visit in the list
        # visit_no = str(Visits.objects.filter(
        #     patientno__patientno=p.patientno).order_by('-visitid')[0])
        visit = Visits.objects.filter(patientno__patientno=p.patientno)
        # print(visit)
        visit_no = []  # initialize visit_no to None
        admission_list = []
        res = {
            "pk": "",
            "surname": p.lastname,
            "firstname": p.firstname,
            "pin_no": p.patientno,
            # "date_of_birth": p.birthdate.strftime("%A, %B %d, %Y"),
            "date_of_birth": p.birthdate,
            "phone": p.phone,
            "gender": p.genderid.datades,
            "address": p.address,
            "visit_no": [],
            "patient_type": "",
            "receipt_no": [],
            "invoice_no": [],
            "extra_billno": "",
            "admission_no": "",
            "patient_type": "",
        }
        final_res = []

        todays_date = str(datetime.date.today())

        for visit_number in visit:
            edited_visit_date = str(visit_number.visitdate).split()[0]
            if edited_visit_date == todays_date:
                visit_no.append(visit_number)

                # extra =Extrabills.objects.filter(visitno=f"{visit_number}").exists()
                # print("my",extra)

            # if Extrabills.objects.filter(visitno=f"{visit_number}").exists():
            #     extra =Extrabills.objects.filter(visitno=f"{visit_number}")
            #     print("my",extra)
            #     admission_no = Admissions.objects.get(visitno=f"{visit_number}")
            #     admission_info= {
            #         "admission_no":admission_no.admissionno,
            #         "admission_date":admission_no.admissiondatetime

            #     }
            #     print("john",admission_no)
            #     admission_list.append(admission_info)
            #     # print(admission_list)
            #     t= Extrabills.objects.filter(visitno=f"{visit_number}")

            # print(t)
        # print(visit_no)
        # print(admission_list)

        print(len(visit_no))
        if len(visit_no) == 0:
            res = None
            messages.add_message(
                request, messages.ERROR, "No visit found for today's date"
            )

            return JsonResponse(
                {"message": "Please first register for a visit"}, status=400
            )
        if len(visit_no) > 0:
            for single_visit_no in visit_no:
                visit_dict = model_to_dict(single_visit_no)
                my_visit_dict = {
                    "visitid": visit_dict["visitid"],
                    "visitno": visit_dict["visitno"],
                }

                try:
                    receipt = (
                        Paymentdetails.objects.filter(
                            visitno__visitno=f"{single_visit_no}"
                        )
                        .select_related("receiptno")
                        .filter(
                            Q(itemcode="PHS04")
                            | Q(itemcode="PHS004")
                            | Q(itemcode="PH0010")
                        )
                        .values()
                    )
                    print(receipt)
                    print(Items.objects.filter(visitno=f"{single_visit_no}"))
                    if receipt.exists():
                        receipt_no_dic = receipt[0]
                        new_receipt_no = receipt_no_dic["receiptno_id"]
                        new_visitno_id = receipt_no_dic["visitno_id"]
                        new_quantity = receipt_no_dic["quantity"]
                        new_unit_price = receipt_no_dic["unitprice"]
                        new_amount = receipt_no_dic["amount"]

                        # res['receipt_no'] = new_receipt_no

                        my_receipt_dic = {
                            "receiptno_id": new_receipt_no,
                            "visitno_id": new_visitno_id,
                            "quantity": new_quantity,
                            "unit_price": new_unit_price,
                            "amount": new_amount,
                        }
                        # print(receipt)
                        # print(my_receipt_dic)
                        res["receipt_no"].append(my_receipt_dic)
                        if "invoice_no" in res:
                            del res["invoice_no"]

                        res["patient_type"] = "OUT-PATIENT"
                        res["visit_no"].append(my_visit_dict)

                        # print(receipt)
                        # res["receipt_no"].append(receipt)
                        # res["receipt_no"].append(receipt)
                        final_res.append(res)
                    elif Items.objects.filter(visitno=f"{single_visit_no}").exists():
                        for i in Items.objects.filter(visitno=f"{single_visit_no}"):
                            print(i.itemcode, i.invoiceno)
                            # if i.invoiceno =="":
                            #     print("break")

                            # break

                            if (
                                i.itemcode == "PHS04"
                                or i.itemcode == "PHS004"
                                or i.itemcode == "PH0010"
                            ) and i.invoiceno != "":
                                print("fdfdfi", i.itemcode, i.invoiceno)
                                date = i.lastupdate
                                quantity = i.quantity
                                invoiceno = i.invoiceno
                                visitno_id = i.visitno_id
                                print(i.invoiceno)
                                my_invoice_dic = {
                                    "invoiceno": invoiceno,
                                    "visitno_id": visitno_id,
                                    "quantity": quantity,
                                }
                                print(my_invoice_dic)
                                res["invoice_no"].append(my_invoice_dic)
                            else:
                                res = None
                                return JsonResponse(
                                    {
                                        "message": "Please patient must first make a payment"
                                    },
                                    status=400,
                                )

                            if "receipt_no" in res:
                                del res["receipt_no"]
                            res["patient_type"] = "OUT-PATIENT"
                            final_res.append(res)
                            print(i.invoiceno, i.quantity, date)
                    else:
                        res = None
                        return JsonResponse(
                            {"message": "Please first register for a visit"}, status=400
                        )
                #             print({"invoice": res["invoice_no"]})
                # elif Extrabills.objects.filter(visitno=f"{single_visit_no}").exists():
                #     #     # Extrabills.objects.filter(
                #     #     #     visitno=f"{res['visit_no']}").exists()
                #     print("it is working")
                #     for i in Extrabills.objects.filter(visitno=f"{res['visit_no']}"):
                #         # if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
                #         print(i.extrabillno)

                #         res['extra_bill_no'] = i.extrabillno
                #         if 'receipt_no' in res:
                #             del res['receipt_no']

                #         if 'invoice_no' in res:
                #             del res['invoice_no']

                #         admission_no = Admissions.objects.get(
                #             visitno=f"{res['visit_no']}").admissionno
                #         res['admission_no'] = admission_no
                #         res["patient_type"] = "IN-PATIENT"
                #         print({"admission": res["admission_no"]})

                # print({"receipt": res["receipt_no"]})

                # elif Items.objects.filter(visitno=f"{res['visit_no']}").exists():
                #     for i in Items.objects.filter(visitno=f"{res['visit_no']}"):
                #         if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
                #             res['invoice_no'] = i.invoiceno
                #             if 'receipt_no' in res:
                #                 del res['receipt_no']
                #             res["patient_type"] = "OUT-PATIENT"
                #             print(res)

                #             print({"invoice": res["invoice_no"]})

                except:
                    print("it is not working")
                    messages.add_message(
                        request, messages.ERROR, "Please first register for a visit"
                    )
                    return render(request, "Patient/add_physio_session.html")
        if len(final_res) > 0:
            print(final_res[-1])
        # print(res)
        # if Extrabills.objects.filter(visitno=f"{res['visit_no']}").exists():
        #     # Extrabills.objects.filter(
        #     #     visitno=f"{res['visit_no']}").exists()
        #     print("it is working")
        #     for i in Extrabills.objects.filter(visitno=f"{res['visit_no']}"):
        #         # if i.itemcode == "PHS04" or i.itemcode == "PHS004" or i.itemcode == "PH0010":
        #         print(i.extrabillno)

        #         res['extra_bill_no'] = i.extrabillno
        #         if 'receipt_no' in res:
        #             del res['receipt_no']

        #         if 'invoice_no' in res:
        #             del res['invoice_no']

        #         admission_no = Admissions.objects.get(
        #             visitno=f"{res['visit_no']}").admissionno
        #         res['admission_no'] = admission_no
        #         res["patient_type"] = "IN-PATIENT"
        #         print({"admission": res["admission_no"]})
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


def patient_profile(request, pk):
    p = Patient.objects.get(patient_no=pk).pk
    p = get_object_or_404(Patient, pk=p)
    physio_admission = p.patient_physio_admission.all()

    date_string = str(p.created_at.date())
    context = {
        "physiosession_admin": [],
        "patient": p,
        "date_string": date_string,
    }
    data = {
        "admission_no": "",
        "payement_info": [],
        "physiosession_attended": [],
        "number_of_session_left": "",
    }
    # for admission in physio_admission:
    #     physiso = PhysioSession.objects.filter(admission_no=admission)
    #     print(physiso)
    #     for p in physiso:
    print(physio_admission)
    for admission in physio_admission:
        admissions_no = admission.admission_no
        receipt_admission = admission.receipt_physiosessionadmission.all()
        print(admissions_no)
        data["admission_no"] = admissions_no
        physisosession_attended = (
            PhysioSession.objects.filter(admission_no=admission)
            .order_by("-created_at")
            .filter(admission_no__discharge=False)
        )
        if physisosession_attended:
            count_of_attended = physisosession_attended.count()
            count_of_quantity_paid = sum(
                receipt.quantity_of_session for receipt in receipt_admission
            )

            number_of_session_left = int(count_of_quantity_paid) - int(
                count_of_attended
            )
            data["number_of_session_left"] = number_of_session_left
            data["physiosession_attended"].append(physisosession_attended)
            for receipt in receipt_admission:
                receipt_number = receipt.receipt_number
                quantity_of_session = receipt.quantity_of_session
                payment_date = receipt.payment_date
                my_dic = {
                    "receipt_number": receipt_number,
                    "quantity_of_session": quantity_of_session,
                    "payment_date": payment_date,
                }
                data["payement_info"].append(my_dic)
            context["physiosession_admin"].append(data)
        if (
            PhysioSession.objects.filter(admission_no=admission)
            .order_by("-created_at")
            .filter(admission_no__discharge=True)
        ):
            physisosession_attended = (
                PhysioSession.objects.filter(admission_no=admission)
                .order_by("-created_at")
                .filter(admission_no__discharge=True)
            )
            count_of_attended = physisosession_attended.count()
            # data["number_of_session_left"] = number_of_session_left
            data["closed_admission_physiosession_attended"] = [physisosession_attended]
            for receipt in receipt_admission:
                receipt_number = receipt.receipt_number
                quantity_of_session = receipt.quantity_of_session
                payment_date = receipt.payment_date
                my_dic = {
                    "receipt_number": receipt_number,
                    "quantity_of_session": quantity_of_session,
                    "payment_date": payment_date,
                }
                data["closed_admission_payement_info"] = [my_dic]
                print(my_dic)
            context["closed_admission_physiosession_admin"] = [data]
        if PhysioSession.objects.filter(admission_no=admission).order_by(
            "-created_at"
        ).filter(admission_no__discharge=False) and PhysioSession.objects.filter(
            admission_no=admission
        ).order_by(
            "-created_at"
        ).filter(
            admission_no__discharge=False
        ):
            context["no_physiosession_admission"] = "No physiosession admision"
    # print(context)
    if request.method == "POST":
        print(request.POST)
        data = request.POST
        date = data.get("data", None)
        receipt = data.get("receipt", None)
        admission_no = data.get("admission_no", None)
        print(admission_no, date, receipt)

        if receipt:
            if Receipt.objects.filter(receipt_number=receipt).exists():
                messages.add_message(
                    request, messages.ERROR, f"Receipt NO is allready registerd"
                )
                return render(request, "patient/patient_profile.html", context)

            payement_detail = get_object_or_404(Paymentdetails, receiptno=receipt)

            visit_no = payement_detail.visitno.visitno
            print(visit_no)
            if payement_detail.visitno.paydate.strftime("%Y-%m-%d") == date:
                quantity_of_session_payed = payement_detail.quantity
                print(quantity_of_session_payed)
                physiosession_admission = PhysioSessionAdmission.objects.get(
                    patient__patient_no=pk
                )
                new_quantity_of_sessions = int(
                    physiosession_admission.quantity_of_sessions
                ) + int(quantity_of_session_payed)

                print(new_quantity_of_sessions)

                receipt_obj = Receipt.objects.create(
                    physiosessionadmission=physiosession_admission,
                    receipt_number=receipt,
                    visit_no=visit_no,
                    payment_date=date,
                    quantity_of_session=quantity_of_session_payed,
                )

                # receipt_obj.save()
                physiosession_admission.quantity_of_sessions = new_quantity_of_sessions
                physiosession_admission.save()

                messages.add_message(request, messages.SUCCESS, f"Updated Successfully")
                return render(request, "patient/patient_profile.html", context)

            else:
                messages.add_message(
                    request, messages.ERROR, f"Please Select the right date"
                )
                return render(request, "patient/patient_profile.html", context)
        elif admission_no:
            admission_no = PhysioSessionAdmission.objects.get(admission_no=admission_no)
            patient = (
                admission_no.patient.surname + " " + admission_no.patient.first_name
            )
            admission_no.discharge = True
            admission_no.save()
            print(patient)
            messages.add_message(
                request,
                messages.SUCCESS,
                f"Addmission for {patient} has been Closed Successfully",
            )
            print(admission_no)

    return render(request, "patient/patient_profile.html", context)


def get_patient_admission_no(request, pk):
    # if request.method == "POST":
    p = Patient.objects.get(patient_no=pk).pk
    p = get_object_or_404(Patient, pk=p)
    physio_admission = p.patient_physio_admission.all()
    

    for admission_no_obj in physio_admission:
        admission_no = admission_no_obj.admission_no
        physio_session_admission_no = PhysioSessionAdmission.objects.filter(
            admission_no=admission_no
        ).filter(discharge=False)

        if physio_session_admission_no:
            break
    physio_admission_no = physio_session_admission_no[0].admission_no

    #! GETING ALL RECIEPTS ASSOCIATED WITH PHYSIO SESSION ADMISSION
    receipt_admission = physio_session_admission_no[
        0
    ].receipt_physiosessionadmission.all()
    print(receipt_admission)
    physisosession_attended = PhysioSession.objects.filter(
        admission_no__admission_no=physio_admission_no
    )

    count_of_attended = physisosession_attended.count()
    count_of_quantity_paid = sum(
        receipt.quantity_of_session for receipt in receipt_admission
    )

    number_of_session_left = int(count_of_quantity_paid) - int(count_of_attended)
    if number_of_session_left > 0:
        return JsonResponse(
            {
                "physio_admission_no": f"{physio_admission_no}",
                "sessions_left": number_of_session_left,
            }
        )

    return JsonResponse({"physio_admission_no": f"{physio_admission_no}"})


def update_patient_payement(request, pk):
    if request.method == "POST":
        patient = get_object_or_404(Patient, pk=pk)
        patient_no = patient.patient_no

        messages.add_message(request, messages.SUCCESS, f"Payment")
    return render(request, "patient/patient_profile.html")


#!  =------------------------------------------- physio----------------------


def physio_session(request):
    # form_back_date = BackDate()
    physioSessionAdmissionForm = PhysioSessionAdmissionForm()
    if request.method == "POST":
        print(request.POST)

        data = request.POST
        if data.get("patient_pin", None) == None:
            messages.add_message(
                request, messages.ERROR, "Please first search for patientd"
            )
            return render(
                request,
                "Patient/physio_session.html",
                {"form": physioSessionAdmissionForm},
            )

        patient_pin = data["patient_pin"]
        more_notes = data["more_notes"]
        therapies = data.getlist("therapy")
        patient_pin = data["patient_pin"]

        active_admmissio_no = PhysioSessionAdmission.objects.get(
            patient__patient_no=patient_pin, discharge=False
        )
        print(therapies)
        physio_session = PhysioSession()
        physio_session.therapist = request.user
        physio_session.more_notes = more_notes
        physio_session.save(patient_no=patient_pin)  # Save the physio_session object

        # Set the therapy field after saving the physio_session object
        # physio_session.therapy.set(therapies)
        # Add therapies to the physio_session using a for loop
        for therapy_id in therapies:
            therapy = Therapy.objects.get(id=therapy_id)
            physio_session.therapy.add(therapy)
        physio_session.save()
        # print(active_admission_no)

    return render(
        request, "Patient/physio_session.html", {"form": physioSessionAdmissionForm}
    )


def physio_session_search(request):
    #! if request.is_ajax and request.method == "POST":
    #! checkin if request is ajax
    if request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        name = request.POST.get("name").capitalize()
        res = None
        qs = Patient.objects.filter(patient_no__icontains=name)
        data = []

        if len(qs) > 0 and len(name) > 0:
            for i in qs:
                item = {
                    # "pk": i.patientid,
                    "pin_no": i.patient_no,
                    "name": i.first_name,
                    "surname": i.surname,
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
    # return render(request, "Patient/physio_session.html", {"form": physioSessionAdmissionForm})


def get_patient_physio(request, pk):
    pk = f"P{pk}"
    p = get_object_or_404(Patient, patient_no=pk)
    # my= Patient.objects.filter(patient_no=pk).select_related("patient")
    # print(my)

    print([admission.quantity_of_sessions for admission in p.patient_physio_admission.all()])
    res = {
        "pk": "",
        "surname": p.surname,
        "firstname": p.first_name,
        "pin_no": p.patient_no,
        "quantity": [
            admission.quantity_of_sessions
            for admission in p.patient_physio_admission.all()
        ],
        "gender": p.gender,
        "diagnosis": [
            admission.diagnosis.name for admission in p.patient_physio_admission.all()
        ][0],
        "patient_type": "",
        "receipt_no": [],
        "invoice_no": [],
        "extra_billno": "",
        "admission_no": "",
        "admission_date": "",
        "patient_type": "",
    }
    quantity = res["quantity"][0]
    print(quantity)

    if int(quantity) == 0:
        return JsonResponse(
            {"message": "Please Patient must first pay for a session"}, status=400
        )
    return JsonResponse({"data": res}, status=200)


def physio_session_table(request):
    physiosession = (
        PhysioSession.objects.all().order_by("-id").select_related("admission_no")
    )
    print(physiosession)
    physio_session_list = []
    for p in physiosession:
        data = {
            "admission_no": p.admission_no.admission_no,
            "patient_no": p.admission_no.patient.patient_no,
            "physiosession_no": p.physiosession_no,
            "diagnosis": p.admission_no.diagnosis,
            "therapy": p.therapy.all(),
            "patient_type": p.admission_no.patient_type,
            "therapist": p.therapist,
            "ward": p.admission_no.ward,
            "created_at": p.created_at,
        }

        if str(str(data["ward"]).capitalize()) == "None":
            data["ward"] = "Out patient donot have wards"
        physio_session_list.append(data)
        print(data)
    return render(
        request,
        "Patient/physio_session_table.html",
        {"physiosession": physio_session_list},
    )


# ? <--------------------ward-------------------------------->
def add_ward(request):
    wardform = WardForm()
    if request.method == "POST":
        name = request.POST.get("name")
        if Ward.objects.filter(name=name).exists():
            messages.add_message(request, messages.ERROR, "Ward is already registered")
            return render(request, "ward/add_ward.html")

        wardform = WardForm(request.POST)
        if wardform.is_valid():
            wardform.save()
            messages.add_message(
                request, messages.SUCCESS, f"Ward {name} added successfully"
            )
            return redirect("ward-table")
    return render(request, "ward/add_ward.html", {"form": wardform})


def ward_table(request):
    ward = Ward.objects.all()

    # df = pd.read_csv('ward.csv')
    # df_ward = df["Ward"].to_list()
    # for x in df_ward:
    #     ward1 = Ward.objects.create(name=x)
    #     ward1.save()
    #     messages.add_message(request, messages.SUCCESS,
    #  f"Ward {x} added successfully")
    return render(request, "ward/ward_table.html", {"wards": ward})


def check_ward(request):
    ward = request.POST.get("name")
    name_split = ward.split(" ")
    first_name = str(name_split[0]).capitalize()
    last_name = str(name_split[1]).capitalize()
    full_name = f"{first_name} {last_name}"
    # when u add .exists it returns true or false
    if Ward.objects.filter(name=full_name).exists():
        print("true")
        return HttpResponse(
            '<div style="color:red;"> This Ward is already registered</div>'
        )
    else:
        return HttpResponse('<div style="color:green;"> This is Ward name is Ok </div>')


# ? <--------------------------------doctors-------------------------------------->
def add_doctor(request):
    doctorform = DoctorForm()
    if request.method == "POST":
        name = request.POST.get("name")
        doctorform = DoctorForm(request.POST)
        if doctorform.is_valid():
            doctorform.save()
            print("cleaned data", doctorform.cleaned_data)

            messages.add_message(
                request, messages.SUCCESS, f"Doctor {name} added successfully"
            )
            return redirect("doctor-table")

        else:
            messages.add_message(
                request, messages.ERROR, "Doctor is already registered"
            )
            return redirect("add-doctor")
    return render(request, "doctor/add_doctor.html", {"form": doctorform})


def doctor_table(request):
    doctor = Doctor.objects.all().order_by("name")

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

    return render(request, "doctor/doctor_table.html", {"doctors": doctor})


def check_doctor(request):
    doctor = request.POST.get("name")
    name_split = doctor.split(" ")
    first_name = str(name_split[0]).capitalize()
    last_name = str(name_split[1]).capitalize()
    full_name = f"{first_name} {last_name}"
    print(full_name)
    # when u add .exists it returns true or false
    if Doctor.objects.filter(name=full_name).exists():
        print("true")
        return HttpResponse(
            '<div style="color:red;"> This Doctor is already registered</div>'
        )
    else:
        return HttpResponse('<div style="color:green;"> This is Doctor is Ok </div>')


# ? <--------------------------------Diagonsis-------------------------------------->


def add_diagnosis(request):
    diagnosisForm = DiagnosisForm()
    if request.method == "POST":
        name = request.POST.get("name")
        diagnosisform = DiagnosisForm(request.POST)
        if diagnosisform.is_valid():
            diagnosisform.save()
            messages.add_message(
                request, messages.SUCCESS, f"Diagnosis {name} added successfully"
            )
            return redirect("diagnosis-table")

        else:
            messages.add_message(
                request, messages.ERROR, "Diagnosis is already registered"
            )
            return redirect("add-diagnosis")
    return render(request, "Diagnosis/add_diagnosis.html", {"form": diagnosisForm})


def diagnosis_table(request):
    # fetch diagnosis basicing on  all the diagnosis order by  alphabetically
    diagnosis = Diagnosis.objects.all().order_by("name")
    # df = pd.read_csv('diagnosis.csv')
    # df_diagnosis = df["Diagnosis"].to_list()
    # for x in df_diagnosis:
    #     diagnosis1 = Diagnosis.objects.create(name=x)
    #     diagnosis1.save()
    #     messages.add_message(request, messages.SUCCESS,
    #                          f"Diagnosis {x} added successfully")
    return render(request, "Diagnosis/diagnosis_table.html", {"diagnosiss": diagnosis})


# <---------------------------------Therapy--------------------------->


def add_therapy(request):
    therapyForm = TherapyForm()
    if request.method == "POST":
        name = request.POST.get("name")
        therapyform = TherapyForm(request.POST)
        if therapyform.is_valid():
            therapyform.save()
            messages.add_message(
                request, messages.SUCCESS, f"Therapy {name} added successfully"
            )
            return redirect("therapy-table")

        else:
            messages.add_message(
                request, messages.ERROR, "Therapy is already registered"
            )
            return redirect("add-therapy")
    return render(request, "Therapy/add_therapy.html", {"form": therapyForm})


def therapy_table(request):
    therapy = Therapy.objects.all().order_by("name")

    # df_therapy = pd.read_csv('therapy.csv')
    # df_therapy = df_therapy.drop_duplicates()
    # df_therapy = df_therapy['Therapy'].to_list()
    # for x in  df_therapy:
    #     therapy_create = Therapy.objects.create(
    #         name=x,
    #         )
    #     therapy_create.save()
    #     messages.add_message(request, messages.SUCCESS, f"Therapy added successfully")

    return render(request, "Therapy/therapy_table.html", {"therapys": therapy})


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


def export_all_phsysioSessions(request):
    response = HttpResponse(content_type="application/ms-excel")
    response["Content-Disposition"] = 'attachment; filename="physio.xls"'
    wb = xlwt.Workbook(encoding="utf-8")
    ws = wb.add_sheet("Physio")
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = [
        "Patient No",
        "Receipt NO",
        "Surname",
        "First name",
        "Full Name",
        "Doctor",
        "Therapy",
        "Ward",
        "Diagnosis",
        "Date",
        # "Physiotherapist",
    ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    list = (
        PhysioSessionAdmission.objects.all()
        .values_list(
            "date_of_visit",
            "patient_no",
            "receipt_no",
            "patient_surname",
            "patient_name",
        )
        .annotate(
            full_name=Concat(
                F("patient_surname"),
                Value(" "),
                F("patient_name"),
                output_field=CharField(),
            ),
            doctor=F("doctor__name"),
            therapy=F("therapy__name"),
            ward=F("ward__name"),
            diagnosis=F("diagnosis__name"),
        )
    )

    # getting date from the tuple and formating it to "Tuesday, April 25, 2023"
    rows = []
    for item in list:
        date = item[0].strftime("%A, %B %d, %Y")
        rows.append(item[1:] + (date,))

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response


# ? 404 error


def page_not_found(request, exception):
    # Additional logic or data retrieval if needed
    return render(request, "_partials/404.html")
