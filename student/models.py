from pickle import TRUE
from sre_constants import MAX_UNTIL
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

State_Choice=(
    ('AP','Andhra Pradesh'),
    ('AR','Arunachal Pradesh'),
    ('AS','Assam'),
    ('BR','Bihar'),
    ('CG','Chhattisgarh'),
    ('GA','Goa'),
    ('GJ','Gujrat'),
    ('HR','Haryana'),
    ('HP','Himachal Pradesh'),
    ('JK','Jammu and Kashmir'),
    ('JH','Jharkhand'),
    ('KA','Karnataka'),
    ('KL','Kerala'),
    ('MP','Madhya Pradesh'),
    ('MH','Mahrashtra'),
    ('MN','Manipur'),
    ('ML','Meghalaya'),
    ('MZ','Mizoram'),
    ('NL','Nagaland')
)

Branch_Choice=(
    ('CSE','Computer Science Engineering'),
    ('IT','Information Technology'),
    ('CHEM','Chemical Engineering'),
    ('PROD','Production Engineering'),
    ('MECH','Mechanical Engineering'),
    ('ELE','Electical Engineering'),
    ('INST','Instrumentation Engineering'),
    ('ENTC','Electobics and Telecommunication Engineering'),
    ('CVL','Civil Engineering'),
)

Year_Choice=(
    ('1','1st'),
    ('2','2nd'),
    ('3','3rd'),
    ('4','4th'),
)

class Student(models.Model):
    SName=models.CharField(max_length=30)
    Reg_No=models.AutoField(primary_key=TRUE)
    Address=models.CharField(max_length=60)
    Taluka=models.CharField(max_length=30)
    District=models.CharField(max_length=30)
    State=models.CharField(max_length=20,choices=State_Choice,default='AP')
    Photo=models.ImageField(upload_to='uploads')
    Pincode=models.IntegerField()
    def _str_(self):
        return self;

class Admission(models.Model):
    reg_Num=models.ForeignKey(Student,on_delete=models.PROTECT,related_name="reg_number")
    StudName=models.ForeignKey(Student,max_length=30,on_delete=models.PROTECT,related_name="student_name")
    Class=models.CharField(max_length=10)
    Branch=models.CharField(max_length=30,choices=Branch_Choice,default='CSE')
    Year=models.CharField(max_length=10)
    DateOfAddmission=models.DateField()
    Semester=models.CharField(max_length=5)

class Marks(models.Model):
    Reg_number=models.ForeignKey(Student,on_delete=models.PROTECT)
    Subject=models.CharField(max_length=50)
    Mark=models.IntegerField()
    Semester=models.CharField(max_length=5)
    Year=models.CharField(max_length=10,choices=Year_Choice,default='1')

class FeedBack(models.Model):
    Regis_No=models.ForeignKey(Marks,on_delete=models.PROTECT)
    Date=models.DateField()
    FeedBck=models.CharField(max_length=500)