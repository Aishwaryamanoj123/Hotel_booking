from django.urls import path
from . import views
from.views import *


urlpatterns = [
    path('',views.home, name='home'),
    path('index/',views.index, name='index'),
    path('about/',views.about, name='about'),
    path('service/',views.service, name='service'),
    path('room/',views.room, name='room'),
    path('booking/',views.booking, name='booking'),
    path('team/',views.ourteam, name='team'),
    path('test/',views.testimonial, name='test'),
    path('contact/',views.contact, name='contact'),
    path('base/', views.base, name='base'),
    path('signup/', views.signup, name= 'signup'),
    path('login/', views.user_login, name= 'login'),
    path('logout/',views.logout_view, name='logout'),
    path('adminhome/', views.admin, name='admin'),
    path('add_room/', views.add_room , name='add_room'),
    path('view_room/', views.view_room, name='view_room'),

    path('updateroom/<int:id>',update_room, name ='update_room'),
    path('delete_room/<int:id>',delete_room, name='delete_room'),
    
    path('view_customer/',views.view_customer,name='view_customer'),
    path('view_booking/',views.view_booking, name='view_booking'),
    path('delete_customer/<int:id>',delete_customer,name ='delete_customer'),

    path('user_home/',views.user_home , name='user_home'),
    path('book/<int:id>',book, name='book'),
    path('save_booking/' , views.save_booking , name ='save_booking'),
    path('view_user_booking/' , views.view_userBooking, name='view_user_booking'),
    path('cancel_booking/<int:id>', cancel_booking, name='cancel_booking'),
    path('details/', views.person_details, name='person_detail'),
    path('update_details/', views.update_details, name='update_details')

   ]