from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('contact_us.urls')),
    path('',include('About.urls')),
    path('',include('contactus_crm.urls')),
    path('',include('career.urls')),
    path('',include('career_crm.urls')),
    path('',include('services.urls')),
    path('',include('home.urls')),
    path('',include('courses.urls')),
    path('',include('courses_crm.urls')),
    path('',include('crm_admin.urls')),
    path('',include('course_contact.urls')),
    path('',include('courses_details.urls')),
    path('',include('apply_now_carrer.urls')),
    path('',include('apply_now_carrrer_crm.urls')),
]
