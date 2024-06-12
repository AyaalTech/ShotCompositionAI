from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('shotanalyser.h5')

img_path = 'test.jpg'
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

predictions = model.predict(img_array)

class_names = ['Rule Of Thirds', 'Leading Lines', 'Symmetrical']

predicted_class_index = np.argmax(predictions)
predicted_class_name = class_names[predicted_class_index]

print("Predicted class: ", predicted_class_name)