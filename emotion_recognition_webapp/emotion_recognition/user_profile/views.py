import logging

from django.shortcuts import render, redirect
from django.views import View

from user_profile.forms import EditProfileDataForm, DeleteProfileForm

logger = logging.getLogger('app')


class EditProfileDataView(View):
    template_name = 'user_profile/edit_profile_data.html'

    def get(self, request):
        form = EditProfileDataForm(initial={
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name
        })
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EditProfileDataForm(request.POST, instance=request.user)
        if not form.is_valid():
            logger.error(f"User {request.user.pk} couldn't change account data.")
            return render(request, self.template_name, {'form': form})

        form.save()
        logger.info(f"User {request.user.pk} changed account data.")
        return redirect('user_profile')


class DeleteProfileView(View):
    template_name = 'user_profile/delete_profile.html'

    def get(self, request):
        return render(request, self.template_name, {'form': DeleteProfileForm(user=request.user)})

    def post(self, request):
        form = DeleteProfileForm(request.POST, user=request.user)
        if not form.is_valid():
            logger.error(f"User {request.user.pk} couldn't delete account.")
            return render(request, self.template_name, {'form': form})

        user = request.user
        logger.info(f"User {request.user.pk} deleted account.")
        user.delete()
        return redirect('deleted-successfully')


class PredictionHistoryView(View):
    template_name = 'user_profile/prediction_history.html'

    def get(self, request):
        predictions = request.user.predictions.all()
        logger.info(f"User {request.user.pk} checked predictions history.")
        return render(request, self.template_name, {
            'predictions': predictions
        })
