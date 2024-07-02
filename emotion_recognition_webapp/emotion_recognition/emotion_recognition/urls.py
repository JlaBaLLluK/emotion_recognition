from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

from emotion_recognition import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction.urls')),
    path('registration/', include('registration.urls')),
    path('login/', include('authorization.urls')),
    path('logout/', login_required(LogoutView.as_view()), name='logout'),
    path('profile/', include('user_profile.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
