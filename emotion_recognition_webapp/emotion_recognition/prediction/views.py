from django.http import FileResponse
from django.shortcuts import render, redirect
from django.views import View
from keras.src.saving import load_model
import numpy as np
import logging
import cv2

from prediction.forms import ChooseFileForm
from prediction.models import Prediction

logger = logging.getLogger('app')


class ChooseFileView(View):
    template_name = 'prediction/index.html'

    def get(self, request):
        return render(request, self.template_name, {'form': ChooseFileForm})

    def post(self, request):
        if not request.user.is_authenticated:
            logger.error("User isn't authenticated")
            return redirect('authorization')

        form = ChooseFileForm(data=request.POST, files=request.FILES)
        if not form.is_valid():
            logger.error(f"User {request.user.pk} uploaded wrong file.")
            return render(request, self.template_name, {'form': form})

        prediction = form.save()
        logger.info(f"User {request.user.pk} uploaded correct file.")
        return redirect('predict_emotions', prediction.id)


def predict_emotion(prediction):
    img = cv2.imread(prediction.source_file.path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error while load image!")
        return

    if img.shape[0] != 48 or img.shape[1] != 48:
        img = cv2.resize(img, (48, 48))

    img = img.astype('float32')
    img = np.repeat(img[..., np.newaxis], 3, axis=-1)
    img = np.expand_dims(img, axis=0)
    model = load_model('model.keras')
    predictions = model.predict(img)
    predicted_classes = np.argmax(predictions, axis=1)
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
        if prediction.result == '':
            predicted_classes = predict_emotion(prediction)
            predicted_class = self.emotions_labels[predicted_classes[0]]
            request.user.operations_done += 1
            request.user.save()
            prediction.result = predicted_class
            prediction.user = request.user
            prediction.save()
            logger.info(f"Done prediction for user {request.user}")
        else:
            logger.info(f"Prediction for user {request.user} was already done")
        return render(request, self.template_name, {
            'prediction': prediction,
        })
