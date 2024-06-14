import numpy as np
import pandas as pd
from keras import Input, Model
from keras.src.applications.resnet import ResNet50
from keras.src.layers import Flatten, Dense
from keras.src.legacy.preprocessing.image import ImageDataGenerator
from keras.src.optimizers import Adam


emotions_labels = {
    0: 'Angry',
    1: 'Disgust',
    2: 'Fear',
    3: 'Happy',
    4: 'Sad',
    5: 'Surprise',
    6: 'Neutral'
}


def load_data(path, is_train):
    data = pd.read_csv(path)
    pixels = data['pixels'].apply(lambda image_pixels: np.fromstring(image_pixels, sep=' ').reshape(48, 48, 1))
    if is_train:
        emotions = data['emotion']
        return np.array(pixels.tolist()), np.array(emotions.tolist())

    return np.array(pixels.tolist())


def main():
    # load train and test data
    train_images_pixels, train_emotions = load_data('../data/train.csv', True)
    test_images_pixels = load_data('../data/test.csv', False)
    train_images_pixels = np.repeat(train_images_pixels, 3, axis=-1)
    test_images_pixels = np.repeat(test_images_pixels, 3, axis=-1)
    # augmentation
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    datagen.fit(train_images_pixels)
    # get base model
    input_shape = (48, 48, 3)
    inputs = Input(shape=input_shape)
    base_model = ResNet50(weights='imagenet', include_top=False, input_tensor=inputs)
    x = Flatten()(base_model.output)
    x = Dense(128, activation='relu')(x)
    output = Dense(7, activation='softmax')(x)
    model = Model(inputs=inputs, outputs=output)
    model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.load_weights('model.weights.h5')
    # model.fit(datagen.flow(train_images_pixels, train_emotions, batch_size=128), epochs=10, validation_data=None)
    # model.save_weights('model.weights.h5')
    predictions = model.predict(test_images_pixels)
    predicted_classes = np.argmax(predictions, axis=1)
    for i in range(100):
        print(f'Test case {i + 1}: {emotions_labels[predicted_classes[i]]}, label number: {predicted_classes[i]}')


if __name__ == '__main__':
    main()
