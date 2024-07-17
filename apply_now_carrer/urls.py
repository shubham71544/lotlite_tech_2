from django.urls import path
from apply_now_carrer.views import *

urlpatterns = [
    path('apply_now/<int:job_id>/', applyNow, name='apply_now'),
    path('apply_nowData/', applyNowData),
]
