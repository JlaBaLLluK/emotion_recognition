import logging

from django.shortcuts import render, redirect
from django.views import View

from registration.forms import RegistrationForm

logger = logging.getLogger('app')


class RegistrationView(View):
    template_name = 'registration/registration.html'

    def get(self, request):
        return render(request, self.template_name, {'form': RegistrationForm})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            logger.error('Error during registration')
            return render(request, self.template_name, {'form': form})

        form.save()
        logger.info('New user registered successfully.')
        return redirect('authorization')
