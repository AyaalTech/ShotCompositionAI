import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from sklearn.preprocessing import LabelEncoder, StandardScaler
import pandas as pd
import sys
import os

# Load the trained model
model = load_model('multi_output_model.keras')

# Define the label encoders
label_encoders = {
    'Shot_Type': LabelEncoder().fit(['Point-of-view', 'Over-the-shoulder', 'Wide shot', 'Medium shot', 'Extreme close-up', 'Close-up']),
    'INT_EXT': LabelEncoder().fit(['INT', 'EXT']),
    'Camera_Model': LabelEncoder().fit(['Panasonic Lumix GH5', 'Fujifilm X-T3', 'Canon EOS R', 'Canon EOS C70', 'Panavision Millennium DXL2', 'Sony FX6', 'ARRI Alexa', 'Blackmagic URSA Mini', 'Sony A7S III', 'RED Epic', 'ARRI Amira']),
    'Composition_Techniques': LabelEncoder().fit(['Rule of thirds', 'Leading lines', 'Symmetry', 'Frame within a frame', 'Golden ratio']),
    'Filter_Used': LabelEncoder().fit(['UV Filter', 'ND Filter', 'Polarizer', 'None']),
    'Lens': LabelEncoder().fit(['Canon EF 24-70mm f/2.8L II USM', 'Nikon AF-S Nikkor 50mm f/1.4G', 'Tokina AT-X 16-28mm f/2.8 Pro FX', 'Panasonic Lumix G X Vario 12-35mm f/2.8 II ASPH', 'Leica Summilux-C 29mm T1.4', 'Sigma 35mm f/1.4 DG HSM Art', 'Fujifilm XF 56mm f/1.2 R', 'Sony FE 24-70mm f/2.8 GM'])
}

# Fit the scaler using the data from the CSV
data = pd.read_csv('movie_shots_data.csv')
numerical_features = data[['Focal Length', 'Lighting Temperature', 'Aperture', 'Focus Distance', 'ISO']]
scaler = StandardScaler().fit(numerical_features)

# Preprocess the input image
def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((128, 128))
    img_array = img_to_array(img) / 255.0
    return np.expand_dims(img_array, axis=0)

# Decode the predictions
def decode_predictions(predictions):
    decoded_preds = {}
    numerical_predictions = np.array([
        predictions[0][0][0],
        predictions[1][0][0],
        predictions[2][0][0],
        predictions[3][0][0],
        predictions[4][0][0]
    ]).reshape(1, -5)
    numerical_predictions = scaler.inverse_transform(numerical_predictions)[0].tolist()  
    decoded_preds['Focal_Length'] = numerical_predictions[0]
    decoded_preds['Lighting_Temperature'] = numerical_predictions[1]
    decoded_preds['Aperture'] = numerical_predictions[2]
    decoded_preds['Focus_Distance'] = numerical_predictions[3]
    decoded_preds['ISO'] = numerical_predictions[4]

    for i, key in enumerate(['Shot_Type', 'INT_EXT', 'Camera_Model', 'Composition_Techniques', 'Filter_Used', 'Lens']):
        prediction = np.argmax(predictions[i + 5][0])
        if prediction < len(label_encoders[key].classes_):
            decoded_preds[key] = label_encoders[key].inverse_transform([prediction])[0]
        else:
            decoded_preds[key] = 'Unknown'

    return decoded_preds

# Function to predict shot attributes
def predict_shot_attributes(image_filename):
    image_path = os.path.join('uploads', image_filename)
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    decoded_predictions = decode_predictions(predictions)
    return decoded_predictions

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Predict shot attributes.')
    parser.add_argument('--image', type=str, required=True, help='Image filename')
    args = parser.parse_args()
    print(predict_shot_attributes(args.image))
