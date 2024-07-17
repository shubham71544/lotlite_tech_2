from django.urls import path
from .views import courses_data, register_view, register, login_view, user_login,logout_view

urlpatterns = [
    path('register/', register_view, name='register_view'),
    path('register/submit/', register, name='register'),
    path('login/', login_view, name='login_view'),
    path('login/submit/', user_login, name='user_login'),
    path('courses_crm/', courses_data, name="courses_data"),
    path('logout/', logout_view, name='logout_view'),
]
