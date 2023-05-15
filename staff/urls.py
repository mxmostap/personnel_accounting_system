from django.contrib.auth.views import LogoutView
from django.urls import path, include

from staff import views
from staff.views import home

urlpatterns = [
    path('', home, name='home'),
    path('registration', views.registration, name='registration'),
    path('authorization', views.authorization, name='authorization'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout')
]
