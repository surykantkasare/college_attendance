from django.shortcuts import render
from .models import Student,Admission,FeedBack,Marks

# Home page 
def view_home(request):
    return render(request,'home.html')
def view_data(request):
    stud_record = Student.objects.all()
    return render(request,'data.html',{'Students':stud_record})

def view_demo(request):
    return render(request,'table.html')

def view_record(request):

    stud_record = Student.objects.all()
    Marks_record = Marks.objects.all()
    return render(request,'record.html',{'stud12':stud_record,'Marks12':Marks_record})

def view_student_reg(request):
    return render(request,'index.html')