from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('students', views.students, name='students'),
    path('teachers', views.teachers, name="teachers"),
    path('sub_teach', views.sub_teach, name='sub_teach'),
    path('sectiona', views.section_A, name="section_A"),

]