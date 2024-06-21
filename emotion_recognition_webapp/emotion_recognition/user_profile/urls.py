from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic import TemplateView

from user_profile.views import EditProfileDataView, DeleteProfileView

urlpatterns = [
    path('', login_required(TemplateView.as_view(template_name='user_profile/user_profile.html')), name='user_profile'),
    path('edit-profile-data/', login_required(EditProfileDataView.as_view()), name='edit_profile_data'),
    path('delete-profile/', login_required(DeleteProfileView.as_view()), name='delete_profile'),
    path('delete-profile/deleted-successfully/',
         TemplateView.as_view(template_name='user_profile/deleted_successfully.html'), name='deleted-successfully')
]
