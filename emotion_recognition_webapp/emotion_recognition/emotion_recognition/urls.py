from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction.urls')),
    path('registration/', include('registration.urls')),
    path('login/', include('authorization.urls')),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('profile/', include('user_profile.urls')),
]
