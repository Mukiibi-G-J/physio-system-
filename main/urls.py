from django.urls import path
from . import views


urlpatterns = [
    path(
        "back_date_registration/",
        views.back_date_registration,
        name="back_date_registration",
    ),
    path("patient-registration/search/", views.search_results, name="search"),
    path(
        "patient-registration/get_patient/<int:pk>/",
        views.get_patient,
        name="get-patient",
    ),
    path("in-patient-registration/search/", views.search_results),
    path(
        "in-patient-registration/get_in_patient/<int:pk>/",
        views.get_in_patient,
        name="get-in-patient",
    ),
    path("patient_profile/<str:pk>", views.patient_profile, name="patient_profile"),
    
    path("physio-session/get_patient_physio/<int:pk>", views.get_patient_physio),
    path("physio-session/", views.physio_session, name="physio-session"),
    path("physio-session/search/", views.physio_session_search, name="physio-session-search"),
    
    path("logout/", views.logout_user, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    # path('book-device/','views.book_device' , name='book-device'),
    path("ward-report/", views.ward_reports, name="ward-report"),
    path("register/", views.register_user, name="register"),
    path("login/", views.login_user, name="login"),
    path("add-patient/", views.patient, name="add-patient"),
    path("add-ward/", views.add_ward, name="add-ward"),
    path("ward-table/", views.ward_table, name="ward-table"),
    path(
        "patient-registration/", views.patient_registration, name="patient-registration"
    ),
    path(
        "in-patient-registration/",
        views.inpatient_registration,
        name="in-patient-registration",
    ),
    path(
        "back-date-registration/",
        views.back_date_registration,
        name="back-date-registration",
    ),
    path(
        "physio-session-table", views.physio_session_table, name="physio-session-table"
    ),
    path("patient-table/", views.patient_table, name="patient-table"),
    path("add-doctor/", views.add_doctor, name="add-doctor"),
    path("doctor-table/", views.doctor_table, name="doctor-table"),
    path("add-therapy/", views.add_therapy, name="add-therapy"),
    path("therapy-table", views.therapy_table, name="therapy-table"),
    path("add-diagnosis/", views.add_diagnosis, name="add-diagnosis"),
    path("diagnosis-table/", views.diagnosis_table, name="diagnosis-table"),
    path(
        "export_all_phsysioSessions",
        views.export_all_phsysioSessions,
        name="export_all_phsysioSessions",
    ),
]


htmx_urlpatterns = [
    path("check_phone/", views.check_phone, name="check-phone"),
    path("check_password/", views.check_password, name="check-password"),
    path("check_time/", views.check_time, name="check-time"),
    path("check_phone_2/", views.check_phone_2, name="check-phone-2"),
    path("current_date/", views.current_date, name="current-date"),
    path("check_ward/", views.check_ward, name="check-ward"),
    path("check_doctor/", views.check_doctor, name="check-doctor"),
    path("day_report/", views.day_report, name="day-report"),
]


urlpatterns += htmx_urlpatterns
