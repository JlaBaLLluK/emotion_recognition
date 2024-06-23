from django.urls import path

from prediction.views import ChooseFileView

urlpatterns = [
    path('', ChooseFileView.as_view(), name='homepage')
]
