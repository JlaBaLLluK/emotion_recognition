from keras.src.saving import load_model
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
import cv2

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
    pixels = np.array(pixels.tolist())
    for i in range(100):
        cv2.imwrite(f'image_{i}.png', pixels[i])
    # return np.array(pixels.tolist()), np.array(emotions.to_list())


def load_image(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print("Error while load image!")
        return

    if img.shape[0] != 48 or img.shape[1] != 48:
        img = cv2.resize(img, (48, 48))

    img = img.astype('float32')
    img = np.repeat(img[..., np.newaxis], 3, axis=-1)
    img = np.expand_dims(img, axis=0)
    return img


def main():
    test_image_pixels = load_image('../data/imgs/image_7.png')
    model = load_model('../model.keras')
    predictions = model.predict(test_image_pixels)
    predicted_classes = np.argmax(predictions, axis=1)
    for i in range(len(predicted_classes)):
        print(f'Test case {i + 1}: {emotions_labels[predicted_classes[i]]}, label number: {predicted_classes[i]}')


if __name__ == '__main__':
    main()
