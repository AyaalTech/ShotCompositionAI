# Import necessary libraries
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPooling2D, Flatten, Dropout
import matplotlib.pyplot as plt
from PIL import Image

# Load the metadata
data = pd.read_csv('movie_shots_data.csv')

# Display the first few rows of the data
data.head()

# Check for missing values
data.isnull().sum()

# Encode categorical variables
label_encoders = {}
for column in ['Shot Type', 'INT/EXT', 'Camera Model', 'Composition Techniques', 'Filter Used', 'Lens']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Normalize numerical features
scaler = StandardScaler()
numerical_features = ['Focal Length', 'Lighting Temperature', 'Aperture', 'Focus Distance', 'ISO']
data[numerical_features] = scaler.fit_transform(data[numerical_features])

# Prepare the data for multi-output prediction
y = {
    'Focal_Length': data['Focal Length'],
    'Lighting_Temperature': data['Lighting Temperature'],
    'Aperture': data['Aperture'],
    'Focus_Distance': data['Focus Distance'],
    'ISO': data['ISO'],
    'Shot_Type': to_categorical(data['Shot Type']),
    'INT_EXT': to_categorical(data['INT/EXT']),
    'Camera_Model': to_categorical(data['Camera Model']),
    'Composition_Techniques': to_categorical(data['Composition Techniques']),
    'Filter_Used': to_categorical(data['Filter Used']),
    'Lens': to_categorical(data['Lens']),
}

# Load and preprocess images
def load_and_preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((128, 128))
    img = np.array(img)
    if img.shape == (128, 128, 3):
        return img / 255.0
    else:
        return None

# Create a list of image arrays corresponding to the file names
image_folder = 'dataset'
image_data = []
valid_indices = []

for index, row in data.iterrows():
    image_path = os.path.join(image_folder, row['File Name'])
    image = load_and_preprocess_image(image_path)
    if image is not None:
        image_data.append(image)
        valid_indices.append(index)

image_data = np.array(image_data)

# Filter y to only include valid indices
y_filtered = {key: value[valid_indices] for key, value in y.items()}

# Split the image data and labels into training and testing sets
X_img_train, X_img_test = train_test_split(image_data, test_size=0.2, random_state=42)

# Split the labels into training and testing sets
y_train_dict = {}
y_test_dict = {}
for key in y_filtered.keys():
    y_train_dict[key], y_test_dict[key] = train_test_split(y_filtered[key], test_size=0.2, random_state=42)

# Define the multi-output model
input_img = Input(shape=(128, 128, 3))
x = Conv2D(32, (3, 3), activation='relu')(input_img)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(64, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Conv2D(128, (3, 3), activation='relu')(x)
x = MaxPooling2D((2, 2))(x)
x = Flatten()(x)
x = Dense(512, activation='relu')(x)
x = Dropout(0.5)(x)

# Define outputs
output_focal_length = Dense(1, name='Focal_Length')(x)
output_lighting_temp = Dense(1, name='Lighting_Temperature')(x)
output_aperture = Dense(1, name='Aperture')(x)
output_focus_distance = Dense(1, name='Focus_Distance')(x)
output_iso = Dense(1, name='ISO')(x)
output_shot_type = Dense(len(label_encoders['Shot Type'].classes_), activation='softmax', name='Shot_Type')(x)
output_int_ext = Dense(len(label_encoders['INT/EXT'].classes_), activation='softmax', name='INT_EXT')(x)
output_camera_model = Dense(len(label_encoders['Camera Model'].classes_), activation='softmax', name='Camera_Model')(x)
output_composition_techniques = Dense(len(label_encoders['Composition Techniques'].classes_), activation='softmax', name='Composition_Techniques')(x)
output_filter_used = Dense(len(label_encoders['Filter Used'].classes_), activation='softmax', name='Filter_Used')(x)
output_lens = Dense(len(label_encoders['Lens'].classes_), activation='softmax', name='Lens')(x)

# Combine inputs and outputs into a model
model = Model(inputs=input_img, outputs=[
    output_focal_length, output_lighting_temp, output_aperture, output_focus_distance,
    output_iso, output_shot_type, output_int_ext, output_camera_model,
    output_composition_techniques, output_filter_used, output_lens
])

# Compile the model
model.compile(optimizer='adam', loss={
    'Focal_Length': 'mse', 'Lighting_Temperature': 'mse', 'Aperture': 'mse',
    'Focus_Distance': 'mse', 'ISO': 'mse', 'Shot_Type': 'categorical_crossentropy',
    'INT_EXT': 'categorical_crossentropy', 'Camera_Model': 'categorical_crossentropy',
    'Composition_Techniques': 'categorical_crossentropy', 'Filter_Used': 'categorical_crossentropy',
    'Lens': 'categorical_crossentropy'
}, metrics={
    'Focal_Length': 'mse', 'Lighting_Temperature': 'mse', 'Aperture': 'mse',
    'Focus_Distance': 'mse', 'ISO': 'mse', 'Shot_Type': 'accuracy',
    'INT_EXT': 'accuracy', 'Camera_Model': 'accuracy',
    'Composition_Techniques': 'accuracy', 'Filter_Used': 'accuracy',
    'Lens': 'accuracy'
})

# Train the model
history = model.fit(X_img_train, {
    'Focal_Length': y_train_dict['Focal_Length'], 'Lighting_Temperature': y_train_dict['Lighting_Temperature'],
    'Aperture': y_train_dict['Aperture'], 'Focus_Distance': y_train_dict['Focus_Distance'],
    'ISO': y_train_dict['ISO'], 'Shot_Type': y_train_dict['Shot_Type'],
    'INT_EXT': y_train_dict['INT_EXT'], 'Camera_Model': y_train_dict['Camera_Model'],
    'Composition_Techniques': y_train_dict['Composition_Techniques'], 'Filter_Used': y_train_dict['Filter_Used'],
    'Lens': y_train_dict['Lens']
}, epochs=10, validation_data=(X_img_test, {
    'Focal_Length': y_test_dict['Focal_Length'], 'Lighting_Temperature': y_test_dict['Lighting_Temperature'],
    'Aperture': y_test_dict['Aperture'], 'Focus_Distance': y_test_dict['Focus_Distance'],
    'ISO': y_test_dict['ISO'], 'Shot_Type': y_test_dict['Shot_Type'],
    'INT_EXT': y_test_dict['INT_EXT'], 'Camera_Model': y_test_dict['Camera_Model'],
    'Composition_Techniques': y_test_dict['Composition_Techniques'], 'Filter_Used': y_test_dict['Filter_Used'],
    'Lens': y_test_dict['Lens']
}))

# Save the model
model.save('multi_output_model.keras')

# Plot the training history
plt.figure(figsize=(12, 8))
for output_name in y_train_dict.keys():
    if f'{output_name}_accuracy' in history.history:
        plt.plot(history.history[f'{output_name}_accuracy'], label=f'{output_name} accuracy')
    if f'val_{output_name}_accuracy' in history.history:
        plt.plot(history.history[f'val_{output_name}_accuracy'], label=f'val_{output_name} accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Evaluate the model on the test data
test_loss, test_metrics = model.evaluate(X_img_test, {
    'Focal_Length': y_test_dict['Focal_Length'], 'Lighting_Temperature': y_test_dict['Lighting_Temperature'],
    'Aperture': y_test_dict['Aperture'], 'Focus_Distance': y_test_dict['Focus_Distance'],
    'ISO': y_test_dict['ISO'], 'Shot_Type': y_test_dict['Shot_Type'],
    'INT_EXT': y_test_dict['INT_EXT'], 'Camera_Model': y_test_dict['Camera_Model'],
    'Composition_Techniques': y_test_dict['Composition_Techniques'], 'Filter_Used': y_test_dict['Filter_Used'],
    'Lens': y_test_dict['Lens']
}, verbose=2)
print('\nTest metrics:', test_metrics)
