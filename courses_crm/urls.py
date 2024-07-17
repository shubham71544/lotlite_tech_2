from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from About import views
from .views import *

urlpatterns = [
    # path('courses_crm/addcourses', coursesData, name="coursesData"),
    path('courses_crm/addcoursesData', course_form,name="AddcoursesData"),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
