from django.urls import path
from app.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('logout', LogOut.as_view(), name='logout'),
    path('employee-dashboard', EmpDashboard.as_view(), name='empdash'),
    path('clock-in', ClockIn.as_view(), name='clockin'),
    path('clock-out', ClockOut.as_view(), name='clockout'),
    path('hr-dashboard', HrDashboard.as_view(), name='hrdash'),
    path('report/<int:id>', EmpGenReport.as_view(), name='report')
]