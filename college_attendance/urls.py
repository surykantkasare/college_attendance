from django.contrib import admin
from django.urls import path,re_path
from student.views import view_home,view_data,view_record,view_demo,view_student_reg
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^demo',view_demo),
    re_path(r'^data',view_data,name="data_page"),
    re_path(r'^register',view_student_reg,name="student_reg"),
    re_path(r'',view_home,name="home_page"),
]
