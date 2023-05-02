# Generated by Django 4.1.3 on 2022-12-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patientid', models.IntegerField(db_column='PatientID')),
                ('patientno', models.CharField(db_column='PatientNo', max_length=20, primary_key=True, serialize=False)),
                ('referenceno', models.CharField(blank=True, db_column='ReferenceNo', max_length=20, null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=20, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=20, null=True)),
                ('middlename', models.CharField(blank=True, db_column='MiddleName', max_length=20, null=True)),
                ('birthdate', models.DateTimeField(blank=True, db_column='BirthDate', null=True)),
                ('photo', models.BinaryField(blank=True, db_column='Photo', max_length='max', null=True)),
                ('fingerprint', models.BinaryField(blank=True, db_column='Fingerprint', max_length='max', null=True)),
                ('birthplace', models.CharField(blank=True, db_column='BirthPlace', max_length=40, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, db_column='Occupation', max_length=100, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=30, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=40, null=True)),
                ('joindate', models.DateTimeField(blank=True, db_column='JoinDate', null=True)),
                ('location', models.CharField(blank=True, db_column='Location', max_length=40, null=True)),
                ('nokname', models.CharField(blank=True, db_column='NOKName', max_length=41, null=True)),
                ('nokrelationship', models.CharField(blank=True, db_column='NOKRelationship', max_length=20, null=True)),
                ('nokphone', models.CharField(blank=True, db_column='NOKPhone', max_length=30, null=True)),
                ('defaultbillno', models.CharField(blank=True, db_column='DefaultBillNo', max_length=20, null=True)),
                ('defaultmembercardno', models.CharField(blank=True, db_column='DefaultMemberCardNo', max_length=30, null=True)),
                ('defaultmainmembername', models.CharField(blank=True, db_column='DefaultMainMemberName', max_length=41, null=True)),
                ('enforcedefaultbillno', models.BooleanField(db_column='EnforceDefaultBillNo')),
                ('hidedetails', models.BooleanField(blank=True, db_column='HideDetails', null=True)),
                ('employeraddress', models.CharField(blank=True, db_column='EmployerAddress', max_length=100, null=True)),
                ('referringmedicalofficer', models.CharField(blank=True, db_column='ReferringMedicalOfficer', max_length=41, null=True)),
                ('nearestdispensary', models.CharField(blank=True, db_column='NearestDispensary', max_length=30, null=True)),
                ('previousadmissions', models.CharField(blank=True, db_column='PreviousAdmissions', max_length=30, null=True)),
                ('chronicdiseases', models.CharField(blank=True, db_column='ChronicDiseases', max_length=200, null=True)),
                ('firstvisitdate', models.DateTimeField(blank=True, db_column='FirstVisitDate', null=True)),
                ('lastvisitdate', models.DateTimeField(blank=True, db_column='LastVisitDate', null=True)),
                ('combinationon', models.CharField(blank=True, db_column='CombinationOn', max_length=30, null=True)),
                ('totalvisits', models.IntegerField(blank=True, db_column='TotalVisits', null=True)),
                ('accountbalance', models.DecimalField(blank=True, db_column='AccountBalance', decimal_places=4, max_digits=19, null=True)),
                ('clientmachine', models.CharField(blank=True, db_column='ClientMachine', max_length=40, null=True)),
                ('recorddatetime', models.DateTimeField(blank=True, db_column='RecordDateTime', null=True)),
                ('nationalidno', models.CharField(blank=True, db_column='NationalIDNo', max_length=20, null=True)),
                ('xraynumbers', models.DecimalField(blank=True, db_column='XrayNumbers', decimal_places=2, max_digits=6, null=True)),
                ('policenotified', models.BooleanField(db_column='PoliceNotified')),
                ('infectiousdiseasesnotified', models.BooleanField(db_column='InfectiousDiseasesNotified')),
                ('medicalconditions', models.CharField(blank=True, db_column='MedicalConditions', max_length=2000, null=True)),
                ('provisionaldiagnosis', models.CharField(blank=True, db_column='ProvisionalDiagnosis', max_length=2000, null=True)),
                ('referringfacility', models.CharField(blank=True, db_column='ReferringFacility', max_length=41, null=True)),
                ('opdoutstanding', models.DecimalField(blank=True, db_column='OPDOutstanding', decimal_places=4, max_digits=19, null=True)),
                ('extrabilloutstanding', models.DecimalField(blank=True, db_column='ExtraBillOutstanding', decimal_places=4, max_digits=19, null=True)),
                ('lastaccountactiondate', models.DateTimeField(blank=True, db_column='LastAccountActionDate', null=True)),
                ('knowaboutservice', models.CharField(blank=True, db_column='KnowAboutService', max_length=100, null=True)),
            ],
            options={
                'db_table': 'Patients',
            },
        ),
    ]