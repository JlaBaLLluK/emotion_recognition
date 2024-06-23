from django.shortcuts import render
from django.views import View

from prediction.forms import ChooseFileForm


class ChooseFileView(View):
    template_name = 'prediction/index.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ChooseFileForm})

    def post(self, request):
        form = ChooseFileForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, self.template_name, {'form': form})

        print(f"{form.cleaned_data.get('file').name}")
        return
