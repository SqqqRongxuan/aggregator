from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView,View
from client import models


class home(TemplateView):
    template_name = 'flight-list.html'

class flightGrid(View):
    def get(self,request):
        return render(request, 'flight-grid.html')

class flightSingle(View):
    def get(self,request):
        passenger_list = models.passenger.objects.all()
        context = {'passenger_list': passenger_list}
        return render(request, 'flight-single.html', context=context)

class flightBooking(View):
    def get(self,request):
        return render(request, 'flight-booking.html')

class flightSearch(View):
    def get(self, request):
        return render(request, 'flight-search-result.html')

class myProfile(View):
    def get(self,request):
        return render(request, 'profile.html')

class myBooking(View):
    def get(self,request):
        return render(request, 'profile-booking.html')

class logout(View):
    def get(self, request):
        return render(request, 'login.html')

class login(View):
    def get(self, request):
        return render(request, 'login.html')

class register(View):
    def get(self, request):
        return render(request, 'register.html')

class bookingConfirm(View):
    def get(self, request):
        bookingConfirmOrder = models.invoice.objects.get(status='UNPAID')
        context = {'bookingConfirmOrder': bookingConfirmOrder}
        return render(request, 'booking-confirm.html', context=context)

class passengerAdd(View):
    def get(self,request):
        return render(request, 'passenger-add.html')

    def post(self,request):
        passenger = models.passenger()
        passenger.name = request.POST.get('name')
        passenger.gender = request.POST.get('gender')
        passenger.nationality = request.POST.get('nationality')
        passenger.passport = request.POST.get('passport')
        passenger.save()
        return render(request, 'flight-single.html')



