from django.shortcuts import render, redirect
from django.views import View

from user_profile.forms import EditProfileDataForm


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
            return render(request, self.template_name, {'form': form})

        form.save()
        return redirect('user_profile')
