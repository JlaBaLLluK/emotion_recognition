from django.contrib.auth.decorators import login_required
from django.urls import path
from prediction.views import *

urlpatterns = [
    path('', ChooseFileView.as_view(), name='homepage'),
    path('predict-emotions/<int:pk>/', login_required(PredictEmotionsView.as_view()), name='predict_emotions'),
]
