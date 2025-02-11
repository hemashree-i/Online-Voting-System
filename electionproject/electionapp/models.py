from django.db import models
from datetime import datetime, timezone

class UserRegisterModel(models.Model):
    catchchoice = [
        ('LocalMember', 'LocalMember'),
        ('CounsilMember', 'CounsilMember'),
        ('SuperMember', 'SuperMember'),
        ('President', 'President'),
    ]

    choice=[
        ('Verified','Verified')
    ]
    uid = models.IntegerField()
    username = models.CharField(max_length=200)
    privilege = models.CharField(max_length=80,choices=catchchoice,null=False,blank=False)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    district = models.CharField(max_length=100)
    localbody = models.CharField(max_length=100)
    ward = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    confirmpassword = models.CharField(max_length=20)
    # verify_user=models.BooleanField(default=False)
    verify_user=models.CharField(max_length=100,choices=choice)

    def __str__(self):
        return self.username


class UserLoginModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    

class VoterAddModel(models.Model):
    serialno = models.IntegerField()
    name = models.CharField(max_length=200)
    guardian = models.CharField(max_length=200)
    houseno = models.CharField(max_length=20)
    housename = models.CharField(max_length=80)
    genderage = models.CharField(max_length=40)
    idcard = models.IntegerField()
    district = models.CharField(max_length=80)
    localbody = models.CharField(max_length=80)
    ward = models.CharField(max_length=80)

    def __str__(self):
        return self.name
 

class ProbabilityModel(models.Model):
    catchchoice = [
        ('YES', 'YES'),
        ('MAYBE', 'MAYBE'),
        ('NO', 'NO'),
    ]
    probability = models.CharField(max_length=20)


class DistrictModel(models.Model):
    District = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.District


class LocalbodyModel(models.Model):
    Localbody_name = models.CharField(max_length=200, null=True, blank=True)
    District_id = models.ForeignKey(DistrictModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Localbody_name


class WardModel(models.Model):
    Ward_name = models.CharField(max_length=200, null=True, blank=True)
    District_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    Localbody_id = models.ForeignKey(LocalbodyModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ward_name


class PollingstationModel(models.Model):
    Pollingstation_name = models.CharField(max_length=200, null=True, blank=True)
    Ward_id = models.ForeignKey(WardModel,on_delete=models.CASCADE)
    District_id = models.ForeignKey(DistrictModel, on_delete=models.CASCADE)
    Localbody_id = models.ForeignKey(LocalbodyModel,on_delete=models.CASCADE)
    def __str__(self):
        return self.Pollingstation_name


class ExcelModel(models.Model):
    serialno = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    guardiansname = models.CharField(max_length=200,null=True,blank=True)
    houseno =  models.CharField(max_length=200,null=True,blank=True)
    housename = models.CharField(max_length=200,null=True,blank=True)
    genderage = models.CharField(max_length=200,null=True,blank=True)
    idno =  models.CharField(max_length=200,null=True,blank=True)

    District_name = models.CharField(max_length=200,null=True,blank=True)
    Localbody_name = models.CharField(max_length=200,null=True,blank=True)
    Ward_name = models.CharField(max_length=200,null=True,blank=True)
    Pollingstation_name = models.CharField(max_length=200,null=True,blank=True)

    # District_id = models.ForeignKey(DistrictModel,on_delete=models.CASCADE)
    # Localbody_id = models.ForeignKey(LocalbodyModel,on_delete=models.CASCADE)
    # Ward_id = models.ForeignKey(WardModel,on_delete=models.CASCADE)
    # Pollingstation_id = models.ForeignKey(PollingstationModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class AddSocialModel(models.Model):
    phone = models.IntegerField(null=True,blank=True)
    gmail = models.CharField(max_length=100,null=True,blank=True)
    instagram = models.CharField(max_length=100,null=True,blank=True)
    linkedin = models.CharField(max_length=100,null=True,blank=True)
    facebook = models.CharField(max_length=100,null=True,blank=True)
    catchchoice = [
        ('YES', 'YES'),
        ('MAYBE', 'MAYBE'),
        ('NO', 'NO'),
    ]
    probability = models.CharField(max_length=20, choices=catchchoice)
    ExcelModel_id =models.CharField(max_length=20,null=True,blank=True)
    userid = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.probability


class CommentModel(models.Model):
    PROBABILITY_CHOICE = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    catchchoice=[
        ('Verified','Verified'),
        ('NotVerified','NotVerified')
    ]
    choice = models.CharField(max_length=10, choices=PROBABILITY_CHOICE)
    comments = models.CharField(max_length=500)
    serialno = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    guardiansname = models.CharField(max_length=200, null=True, blank=True)
    houseno = models.CharField(max_length=200, null=True, blank=True)
    housename = models.CharField(max_length=200, null=True, blank=True)
    genderage = models.CharField(max_length=200, null=True, blank=True)
    idno = models.CharField(max_length=200, null=True, blank=True)
    userassigned = models.CharField(max_length=200, null=True, blank=True)
    Pollingstation_id = models.CharField(max_length=200, null=True, blank=True)
    verify_user=models.CharField(max_length=100,choices=catchchoice)

    def __str__(self):
        return self.comments
    

class SuperMemberModel(models.Model):
    comment = models.CharField(max_length=500,null=True,blank=True)
    verified = models.BooleanField(default=False)
    cathchoice = (
        ('YES','YES'),
        ('NO','NO')
    )
    choice = models.CharField(max_length=50,choices=cathchoice)
    assigned = models.CharField(max_length=50,null=True,blank=False)
    name= models.CharField(max_length=200, null=True, blank=True)
    idno=models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.choice
    

class PresidentModel(models.Model):
    choice=(
        ('OnProgress','OnProgress'),
        ('Completed','Completed')
    )
    comment = models.CharField(max_length=500,null=True,blank=True)
    assigned = models.CharField(max_length=50,null=True,blank=False)
    name= models.CharField(max_length=200, null=True, blank=True)
    idno=models.CharField(max_length=200, null=True, blank=True)
    assignedto = models.CharField(max_length=50,null=True,blank=False)
    date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=200,choices=choice)

    def __str__(self):
        return self.name
    

class AdminModel(models.Model):
    verify_user=models.BooleanField(default=False)
    problems_reply=models.CharField(max_length=500,null=True,blank=True)
    userregister_id=models.ForeignKey(UserRegisterModel,on_delete=models.CASCADE)

class ReportIssueModel(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=200,null=True,blank=True)
    privilege=models.CharField(max_length=200,null=True,blank=True)
    issue=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.username

class IssueReplyModel(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=200,null=True,blank=True)
    datereceived=models.DateTimeField(null=True,blank=True)
    issue=models.CharField(max_length=500,null=True,blank=True)
    reply=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.username

class SuggestionModel(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=200,null=True,blank=True)
    privilege=models.CharField(max_length=200,null=True,blank=True)
    datereceived=models.DateTimeField(null=True,blank=True)
    suggestion=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.username
    
class SuggestionReplyModel(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=200,null=True,blank=True)
    issue=models.CharField(max_length=500,null=True,blank=True)
    reply=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return self.username

class AssignTaskModel(models.Model):
    choice=(
        ('OnProgress','OnProgress'),
        ('Completed','Completed')
    )
    username=models.CharField(max_length=200,null=True,blank=True)
    userid=models.CharField(max_length=200,null=True,blank=True)
    task=models.CharField(max_length=500,null=True,blank=True)
    assignedto=models.CharField(max_length=500,null=True,blank=True)
    date=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=200,choices=choice)
    
    def __str__(self):
        return self.username





    


