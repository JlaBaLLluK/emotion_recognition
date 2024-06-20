from django.urls import path
from registration.views import *

urlpatterns = [
    path('', RegistrationView.as_view(), name='registration')
]
