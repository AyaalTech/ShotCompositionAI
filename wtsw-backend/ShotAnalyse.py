import os
import pandas as pd
import xml.etree.ElementTree as ET
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam

def parse_xml_annotations(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []
    for image in root.findall('.//image'):
        
        filename = os.path.join('dataset', 'wide-shot', image.get('name'))
        label = image.find('.//tag').get('label')
        data.append((filename, label))
    return data

data = parse_xml_annotations('dataset/annotations.xml')
df = pd.DataFrame(data, columns=['filename', 'label'])

print(df.head())  

data = parse_xml_annotations('dataset/annotations.xml')
df = pd.DataFrame(data, columns=['filename', 'label'])

base_model = ResNet50(weights='imagenet', include_top=False)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(3, activation='softmax')(x)  
model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest')

train_generator = train_datagen.flow_from_dataframe(
    dataframe=df,
    x_col='filename',
    y_col='label',
    target_size=(224, 224),
    class_mode='categorical',
    batch_size=32)

model.fit(train_generator, steps_per_epoch=100, epochs=10)

model.save('shotanalyser.h5')  