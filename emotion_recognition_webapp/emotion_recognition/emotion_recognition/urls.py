from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='homepage'),
    path('registration/', include('registration.urls')),
    path('login/', include('authorization.urls')),
    path('logout/', LogoutView.as_view(), name='logout')
]