from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import user_passes_test

Food = ''
urlpatterns = [
    path('', login_required(views.page1), name='Home'),
    path('signup/',views.signup, name='signup'),
    path('signin/',views.signin, name='signin'), 
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.page1, name='home'),


]
