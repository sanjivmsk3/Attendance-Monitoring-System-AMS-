from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from app.models import *
from datetime import datetime, timedelta

# Create your views here.


class Home(View):
    def get(self, request):
        if request.user.is_staff:
            return redirect('hrdash')
        elif request.user.is_active:
            return redirect('empdash')
        else:
            return render(request, 'home.html')


    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = authenticate(username=username, password=password)
        except:
            #msg username or password not exists
            return redirect('home')

        if user is not None:
            login(request, user)
            if request.user.is_staff is True:
                #msg logged in HR
                return redirect('hrdash')
            elif request.user.is_active is True:
                # msg logged in employee
                return redirect('empdash')
            else:
                logout(request)
                # msg logout
                return redirect('home')
        else:
            # msg username or password not exists
            return redirect('home')

class LogOut(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        #msg
        return redirect('home')

class EmpDashboard(LoginRequiredMixin, View):
    def get(self, request):
        da = datetime.now().date()

        context = {
            "clocking": ClockInOut.objects.filter(user=request.user, clock_in__date=da),
            "clockouting": ClockInOut.objects.filter(user=request.user, clock_out__date=da, clock_in__date=da),
            "clock": ClockInOut.objects.filter(user=request.user, clock_out__date=da)
        }
        return render(request, 'emp_dash.html', context)


class ClockIn(LoginRequiredMixin ,View):
    def post(self, request):
        c = ClockInOut()
        c.user = request.user
        c.clock_in = datetime.now()
        c.save()
        return redirect('empdash')

class ClockOut(LoginRequiredMixin ,View):
    def post(self, request):
        da = datetime.now().date()
        c = ClockInOut.objects.get(user=request.user, clock_in__date=da)
        c.clock_out = datetime.now()
        f = c.clock_out.hour
        d = f - 1
        a = datetime(c.clock_out.year, c.clock_out.month, c.clock_out.day, d, c.clock_out.minute, c.clock_out.second)
        b = datetime(c.clock_in.year, c.clock_in.month, c.clock_in.day, c.clock_in.hour, c.clock_in.minute, c.clock_in.second)
        c.total_hour = a - b
        print(a - b)
        c.save()
        return redirect('empdash')

class HrDashboard(LoginRequiredMixin, View):
    def get(self, request):
        if request.user.is_staff:
            context = {
                'allEmp': User.objects.filter(is_staff=False)
            }
            return render(request, 'hr_dash.html',context)
        else:
            logout(request)
            return redirect('home')

class EmpGenReport(LoginRequiredMixin, View):
    def get(self, request, id):
        if request.user.is_staff:
            context = {
                "clock": ClockInOut.objects.filter(user_id=id),
                'users': User.objects.get(id=id)
            }
            return render(request, 'report.html',context)
        else:
            logout(request)
            return redirect('home')