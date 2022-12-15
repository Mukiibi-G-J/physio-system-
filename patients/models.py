from django.db import models


# class Parishes(models.Model):
#     parishcode = models.CharField(db_column='ParishCode', primary_key=True, max_length=20)  # Field name made lowercase.
#     parishname = models.CharField(db_column='ParishName', max_length=41, blank=True, null=True)  # Field name made lowercase.
#     subcountycode = models.ForeignKey('Subcounties', models.DO_NOTHING, db_column='SubCountyCode', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Parishes'
#         unique_together = (('parishname', 'subcountycode'),)
        
# class Villages(models.Model):
#     villagecode = models.CharField(db_column='VillageCode', primary_key=True, max_length=20)  # Field name made lowercase.
#     villagename = models.CharField(db_column='VillageName', max_length=41, blank=True, null=True)  # Field name made lowercase.
#     parishcode = models.ForeignKey(Parishes, models.DO_NOTHING, db_column='ParishCode', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
#         db_table = 'Villages'
#         unique_together = (('villagename', 'parishcode'),)


# class Healthunits(models.Model):
#     healthunitcode = models.CharField(db_column='HealthUnitCode', primary_key=True, max_length=10)  # Field name made lowercase.
#     healthunitname = models.CharField(db_column='HealthUnitName', unique=True, max_length=41, blank=True, null=True)  # Field name made lowercase.
#     districtsid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='DistrictsID', blank=True, null=True)  # Field name made lowercase.
#     contactperson = models.CharField(db_column='ContactPerson', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
#     phone = models.CharField(db_column='Phone', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = False
        # db_table = 'HealthUnits'

# class Logins(models.Model):
#     loginid = models.CharField(db_column='LoginID', primary_key=True, max_length=20)  # Field name made lowercase.
#     firstname = models.CharField(db_column='FirstName', max_length=20)  # Field name made lowercase.
#     lastname = models.CharField(db_column='LastName', max_length=20)  # Field name made lowercase.
#     loginpassword = models.CharField(db_column='LoginPassword', max_length=200)  # Field name made lowercase.
#     loginlevel = models.SmallIntegerField(db_column='LoginLevel')  # Field name made lowercase.
#     statusid = models.ForeignKey('Lookupdata', models.DO_NOTHING, db_column='StatusID')  # Field name made lowercase.
#     changepassword = models.BooleanField(db_column='ChangePassword')  # Field name made lowercase.
#     creatorloginid = models.ForeignKey('self', models.DO_NOTHING, db_column='CreatorLoginID', blank=True, null=True)  # Field name made lowercase.
#     creatorclientmachine = models.CharField(db_column='CreatorClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
#     creatorrecorddatetime = models.DateTimeField(db_column='CreatorRecordDateTime', blank=True, null=True)  # Field name made lowercase.

#     class Meta:
        
#         db_table = 'Logins'
# class Lookupdata(models.Model):
#     lookuporder = models.AutoField(db_column='LookupOrder')  # Field name made lowercase.
#     dataid = models.CharField(db_column='DataID', primary_key=True, max_length=10)  # Field name made lowercase.
#     objectid = models.ForeignKey('Lookupobjects', models.DO_NOTHING, db_column='ObjectID')  # Field name made lowercase.
#     datades = models.CharField(db_column='DataDes', max_length=100)  # Field name made lowercase.
#     isdefault = models.CharField(db_column='IsDefault', max_length=1)  # Field name made lowercase.
#     ishidden = models.CharField(db_column='IsHidden', max_length=1)  # Field name made lowercase.

#     class Meta:
        
#         db_table = 'LookupData'
#         unique_together = (('objectid', 'datades'),)

class Patients(models.Model):
    patientid = models.IntegerField(db_column='PatientID')  # Field name made lowercase.
    patientno = models.CharField(db_column='PatientNo', primary_key=True, max_length=20)  # Field name made lowercase.
    referenceno = models.CharField(db_column='ReferenceNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    birthdate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    # genderid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='GenderID', blank=True, null=True)  # Field name made lowercase.
    photo = models.BinaryField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    fingerprint = models.BinaryField(db_column='Fingerprint', blank=True, null=True)  # Field name made lowercase.
    birthplace = models.CharField(db_column='BirthPlace', max_length=40, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    occupation = models.CharField(db_column='Occupation', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=40, blank=True, null=True)  # Field name made lowercase.
    joindate = models.DateTimeField(db_column='JoinDate', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nokname = models.CharField(db_column='NOKName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    nokrelationship = models.CharField(db_column='NOKRelationship', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nokphone = models.CharField(db_column='NOKPhone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    # defaultbillmodesid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='DefaultBillModesID', blank=True, null=True)  # Field name made lowercase.
    defaultbillno = models.CharField(db_column='DefaultBillNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    defaultmembercardno = models.CharField(db_column='DefaultMemberCardNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    defaultmainmembername = models.CharField(db_column='DefaultMainMemberName', max_length=41, blank=True, null=True)  # Field name made lowercase.
    enforcedefaultbillno = models.BooleanField(db_column='EnforceDefaultBillNo')  # Field name made lowercase.
    hidedetails = models.BooleanField(db_column='HideDetails', blank=True, null=True)  # Field name made lowercase.
    # statusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='StatusID', blank=True, null=True)  # Field name made lowercase.
    # bloodgroupid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BloodGroupID', blank=True, null=True)  # Field name made lowercase.
    # villagecode = models.ForeignKey('Villages', models.DO_NOTHING, db_column='VillageCode', blank=True, null=True)  # Field name made lowercase.
    # tribeid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='TribeID', blank=True, null=True)  # Field name made lowercase.
    # countryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CountryID', blank=True, null=True)  # Field name made lowercase.
    # maritalstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='MaritalStatusID', blank=True, null=True)  # Field name made lowercase.
    # careentrypointid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CareEntryPointID', blank=True, null=True)  # Field name made lowercase.
    # religionid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ReligionID', blank=True, null=True)  # Field name made lowercase.
    # employer = models.CharField(db_column='Employer', max_length=41, blank=True, null=True)  # Field name made lowercase.
    employeraddress = models.CharField(db_column='EmployerAddress', max_length=100, blank=True, null=True)  # Field name made lowercase.
    referringmedicalofficer = models.CharField(db_column='ReferringMedicalOfficer', max_length=41, blank=True, null=True)  # Field name made lowercase.
    nearestdispensary = models.CharField(db_column='NearestDispensary', max_length=30, blank=True, null=True)  # Field name made lowercase.
    previousadmissions = models.CharField(db_column='PreviousAdmissions', max_length=30, blank=True, null=True)  # Field name made lowercase.
    chronicdiseases = models.CharField(db_column='ChronicDiseases', max_length=200, blank=True, null=True)  # Field name made lowercase.
    firstvisitdate = models.DateTimeField(db_column='FirstVisitDate', blank=True, null=True)  # Field name made lowercase.
    lastvisitdate = models.DateTimeField(db_column='LastVisitDate', blank=True, null=True)  # Field name made lowercase.
    combinationon = models.CharField(db_column='CombinationOn', max_length=30, blank=True, null=True)  # Field name made lowercase.
    totalvisits = models.IntegerField(db_column='TotalVisits', blank=True, null=True)  # Field name made lowercase.
    accountbalance = models.DecimalField(db_column='AccountBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    # loginid = models.ForeignKey(Logins, models.DO_NOTHING, db_column='LoginID', blank=True, null=True)  # Field name made lowercase.
    clientmachine = models.CharField(db_column='ClientMachine', max_length=40, blank=True, null=True)  # Field name made lowercase.
    recorddatetime = models.DateTimeField(db_column='RecordDateTime', blank=True, null=True)  # Field name made lowercase.
    nationalidno = models.CharField(db_column='NationalIDNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    # branchid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='BranchID', blank=True, null=True)  # Field name made lowercase.
    xraynumbers = models.DecimalField(db_column='XrayNumbers', max_digits=6, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    policenotified = models.BooleanField(db_column='PoliceNotified')  # Field name made lowercase.
    infectiousdiseasesnotified = models.BooleanField(db_column='InfectiousDiseasesNotified')  # Field name made lowercase.
    medicalconditions = models.CharField(db_column='MedicalConditions', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    provisionaldiagnosis = models.CharField(db_column='ProvisionalDiagnosis', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    # communityid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='CommunityID', blank=True, null=True)  # Field name made lowercase.
    # educationlevelid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='EducationLevelID', blank=True, null=True)  # Field name made lowercase.
    referringfacility = models.CharField(db_column='ReferringFacility', max_length=41, blank=True, null=True)  # Field name made lowercase.
    # attachedtoid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AttachedToID', blank=True, null=True)  # Field name made lowercase.
    # healthunitcode = models.ForeignKey(Healthunits, models.DO_NOTHING, db_column='HealthUnitCode', blank=True, null=True)  # Field name made lowercase.
    # accountstatusid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='AccountStatusID', blank=True, null=True)  # Field name made lowercase.
    opdoutstanding = models.DecimalField(db_column='OPDOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    extrabilloutstanding = models.DecimalField(db_column='ExtraBillOutstanding', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    lastaccountactiondate = models.DateTimeField(db_column='LastAccountActionDate', blank=True, null=True)  # Field name made lowercase.
    knowaboutservice = models.CharField(db_column='KnowAboutService', max_length=100, blank=True, null=True)  # Field name made lowercase.
    # clientcategoryid = models.ForeignKey(Lookupdata, models.DO_NOTHING, db_column='ClientCategoryID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'Patients'


