from django.shortcuts import render, redirect
from django.views import View

from prediction.forms import ChooseFileForm


class ChooseFileView(View):
    template_name = 'prediction/index.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ChooseFileForm})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('authorization')

        form = ChooseFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        prediction = form.save()
        return redirect('predict-emotions', prediction.id)


class PredictEmotionsView(View):

    def get(self, request, pk):
        pass
