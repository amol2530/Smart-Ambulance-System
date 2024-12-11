from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.navbar,name='navbar'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('help/', views.help, name='help'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_registration/', views.user_registration, name='user_registration'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_contact/', views.user_contact, name='user_contact'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_changepassword/', views.user_changepassword, name='user_changepassword'),
    path('user_searchambulance/', views.user_searchambulance, name='user_searchambulance'),
    path('search/',views.search,name='search'),
    # path('user_bookambulance/', views.user_bookambulance, name='user_bookambulance'),
    path('<int:id>/', views.user_bookambulance, name='user_bookambulance'),
    # path('report/', views.report, name="report"),

    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('admin_contact/', views.admin_contact, name='admin_contact'),
    path('view_user/',views.view_user, name='view_user'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('hospital_ambulance/',views.hospital_ambulance,name='hospital_ambulance'),
    path('views_booking_detailes/',views.views_booking_detailes,name='views_booking_detailes'),
    # path('check_patient/',views.check_patient,name='check_patient'),
    path('ambulance_type/',views.ambulance_type, name='ambulance_type'),
    path('views_booking_detailes/', views.views_booking_detailes, name='views_booking_detailes'),
    path('hospital', views.hospital, name='hospital'),
    path('hospital_login', views.hospital_login, name='hospital_login'),
    path('hospital_registration', views.hospital_registration, name='hospital_registration'),
    path('map', views.map, name='map'),
    # path('prediction/', views.prediction, name="prediction"),
    # path('', views.index, name="index"),
    path('ambulance/', views.ambulance, name="ambulance"),
    path('ambulance_update<int:id>/', views.ambulance_update, name="ambulance_update"),



]