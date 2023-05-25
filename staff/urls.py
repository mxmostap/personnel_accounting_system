from django.contrib.auth.views import LogoutView
from django.urls import path, include

from staff.views import home, MyLoginView, MyRegistrationView

urlpatterns = [
    path('', home, name='home'),
    path('registration', MyRegistrationView.as_view(), name='registration'),
    path('login', MyLoginView.as_view(next_page='home'), name='login'),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    # path('password_reset', MyPasswordResetView.as_view(), name='password_reset'),

    # path('', include('django.contrib.auth.urls')),
]
