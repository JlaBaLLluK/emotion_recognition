from django.urls import path

from authorization.views import *

urlpatterns = [
    path('', AuthorizationView.as_view(), name='authorization')
]
