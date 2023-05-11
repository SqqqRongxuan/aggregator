from django.urls import path
from .views import home,flightSingle,flightBooking,logout,\
    myBooking,myProfile,flightSearch,\
    register,login,passengerAdd,bookingConfirm

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('flightSingle/',flightSingle.as_view(),name='flightSingle'),
    path('flightBooking/',flightBooking.as_view(),name='flightBooking'),
    path('flightSearch/',flightSearch.as_view(),name='flightSearch'),
    path('myProfile/', myProfile.as_view(), name='myProfile'),
    path('myBooking/', myBooking.as_view(), name='myBooking'),
    path('logout/', logout.as_view(), name='logout'),
    path('login/', login.as_view(), name='login'),
    path('register/', register.as_view(), name='register'),
    path('passengerAdd/', passengerAdd.as_view(), name='passengerAdd'),
    path('bookingConfirm/', bookingConfirm.as_view(), name='bookingConfirm'),
]