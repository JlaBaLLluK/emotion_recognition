from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views import View
from keras.src.saving import load_model
from pandas import read_csv, DataFrame
import numpy as np
import os

from prediction.forms import ChooseFileForm
from prediction.models import Prediction


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
        return redirect('predict_emotions', prediction.id)


def predict_emotions(prediction):
    data = read_csv(prediction.source_file)
    images_pixels = np.array(data['pixels'].apply(
        lambda image_pixels: np.fromstring(image_pixels, sep=' ').reshape(48, 48, 1)).tolist())
    images_pixels = np.repeat(images_pixels, 3, axis=-1)
    model = load_model('model.keras')
    predictions = model.predict(images_pixels)
    predicted_classes = np.argmax(predictions, axis=1)
    result_data = DataFrame({
        'emotion': predicted_classes,
        'pixels': data['pixels']
    })
    result_file_name = 'result_' + prediction.source_file.name.split('/')[-1]
    result_path = f'results/{result_file_name}'
    prediction.result_file.name = result_path
    prediction.save()
    os.makedirs('results', exist_ok=True)
    result_data.to_csv(result_path, index=False)
    return predicted_classes


class PredictEmotionsView(View):
    template_name = 'prediction/predict_emotions.html'
    emotions_labels = {
        0: 'angry',
        1: 'disgust',
        2: 'fear',
        3: 'happy',
        4: 'sad',
        5: 'surprise',
        6: 'neutral'
    }

    def get(self, request, pk):
        prediction = Prediction.objects.get(pk=pk)
        if prediction.result_file == '':
            predicted_classes = predict_emotions(prediction)
            prediction.user = request.user
            request.user.operations_done += 1
            request.user.save()
            prediction.save()
        else:
            data = read_csv(prediction.result_file)
            predicted_classes = data['emotion']

        predicted_classes = [self.emotions_labels[predicted_class] for predicted_class in predicted_classes]
        return render(request, self.template_name, {
            'emotions': predicted_classes,
            'prediction_pk': pk
        })


class DownloadPredictionView(View):

    @staticmethod
    def get(request, pk):
        return FileResponse(Prediction.objects.get(pk=pk).result_file, as_attachment=True)
