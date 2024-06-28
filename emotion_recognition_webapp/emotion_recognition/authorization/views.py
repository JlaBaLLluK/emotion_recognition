import logging

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View

from auth_user.models import AuthUser
from authorization.forms import AuthorizationForm

logger = logging.getLogger('app')


class AuthorizationView(View):
    template_name = 'authorization/authorization.html'

    def get(self, request):
        return render(request, self.template_name, {'form': AuthorizationForm})

    def post(self, request):
        form = AuthorizationForm(data=request.POST)
        if not form.is_valid():
            logger.error('Attempt to login with wrong credentials.')
            return render(request, self.template_name, {'form': form})

        login(request, AuthUser.objects.get(username=form.cleaned_data.get('username')))
        logger.info(f'User {form.cleaned_data.get('username')} logged in successful')
        return redirect('homepage')
