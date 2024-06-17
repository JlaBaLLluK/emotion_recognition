from keras.src.saving import load_model
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

emotions_labels = {
    0: 'Angry',
    1: 'Disgust',
    2: 'Fear',
    3: 'Happy',
    4: 'Sad',
    5: 'Surprise',
    6: 'Neutral'
}


def load_test_data(path):
    data = pd.read_csv(path)
    pixels = data['pixels'].apply(lambda image_pixels: np.fromstring(image_pixels, sep=' ').reshape(48, 48, 1))
    emotions = data['emotion']
    return np.array(pixels.tolist()), np.array(emotions.to_list())


def main():
    test_images_pixels, true_classes = load_test_data('../data/fer2013/fer2013.csv')
    test_images_pixels = np.repeat(test_images_pixels, 3, axis=-1)
    model = load_model('model.keras')
    predictions = model.predict(test_images_pixels)
    predicted_classes = np.argmax(predictions, axis=1)
    for i in range(len(predicted_classes)):
        print(f'Test case {i + 1}: {emotions_labels[predicted_classes[i]]}, label number: {predicted_classes[i]}')

    accuracy = accuracy_score(true_classes, predicted_classes)
    print(f'Accuracy: {accuracy}')


if __name__ == '__main__':
    main()
