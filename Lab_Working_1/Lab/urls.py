from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from Pathology import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.home, name='home'),
     path('register/', views.register, name='register'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
     path('patient/', views.patient_details_view, name='patient'),
     path('image_upload/', views.image_upload_view, name='image_upload'),
     path('image_upload/<test_name>', views.image_upload_view, name='test_name'),
     path('report/', views.report_view, name='report'),
     path('location/', views.location_view, name='location'),
     path('test/', views.test_in_pathology, name='test'),
     path('final_report/', views.final_reports_view, name='final_report'),
     #path('blood_test/', views.blood_test_view, name='blood_test'),
     #path('urine_test/', views.urine_test_view, name='urine_test'),
     path('add_test/', views.test_view, name='add_test'),
     path('about_us/', views.about_us, name='about_us'),
     path('contact_us/', views.contact_us, name='contact_us'),
     #path('new/', views.new_view, name = 'new'),
     # path('name/', views.name_view, name='name')

]
