import os
import csv
import random

dataset_folder = 'dataset'

focal_lengths = [24, 35, 50, 85, 105]
lighting_temperatures = [3200, 4300, 5600, 6500]
apertures = [1.4, 2.0, 2.8, 4.0, 5.6]
focus_distances = [0.5, 1.0, 1.5, 2.0, 3.0]
shot_types = ['Close-up', 'Medium shot', 'Wide shot', 'Extreme close-up', 'Over-the-shoulder', 'Point-of-view']
isos = [100, 200, 400, 800, 1600]
int_ext = ['INT', 'EXT']
camera_models = [
    'ARRI Alexa', 'RED Epic', 'Sony Venice', 'Canon C300', 'Blackmagic URSA Mini',
    'Panasonic Lumix GH5', 'Fujifilm X-T3', 'Nikon Z6', 'Canon EOS R', 'Sony A7S III',
    'RED Komodo', 'ARRI Amira', 'Sony FX6', 'Panavision Millennium DXL2', 'Canon EOS C70'
]
composition_techniques = ['Rule of thirds', 'Leading lines', 'Frame within a frame', 'Symmetry', 'Golden ratio']
filters_used = ['None', 'ND Filter', 'Polarizer', 'UV Filter', 'Gradient Filter']
lenses = [
    'Canon EF 24-70mm f/2.8L II USM', 'Nikon AF-S Nikkor 50mm f/1.4G', 'Sigma 35mm f/1.4 DG HSM Art',
    'Zeiss Otus 85mm f/1.4', 'Sony FE 24-70mm f/2.8 GM', 'Tamron SP 70-200mm f/2.8 Di VC USD G2',
    'Fujifilm XF 56mm f/1.2 R', 'Panasonic Lumix G X Vario 12-35mm f/2.8 II ASPH', 'Tokina AT-X 16-28mm f/2.8 Pro FX',
    'Leica Summilux-C 29mm T1.4'
]

file_names = [f for f in os.listdir(dataset_folder) if os.path.isfile(os.path.join(dataset_folder, f))]

csv_file_path = 'movie_shots_data.csv'

with open(csv_file_path, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([
        'File Name', 'Focal Length', 'Lighting Temperature', 'Aperture', 
        'Focus Distance', 'Shot Type', 'ISO', 'INT/EXT', 
        'Camera Model', 'Composition Techniques', 'Filter Used', 'Lens'
    ])

    for file_name in file_names:
        focal_length = random.choice(focal_lengths)
        lighting_temperature = random.choice(lighting_temperatures)
        aperture = random.choice(apertures)
        focus_distance = random.choice(focus_distances)
        shot_type = random.choice(shot_types)
        iso = random.choice(isos)
        scene_type = random.choice(int_ext)
        camera_model = random.choice(camera_models)
        composition_technique = random.choice(composition_techniques)
        filter_used = random.choice(filters_used)
        lens = random.choice(lenses)
        
        csv_writer.writerow([
            file_name, focal_length, lighting_temperature, aperture, 
            focus_distance, shot_type, iso, scene_type, camera_model, 
            composition_technique, filter_used, lens
        ])

print(f'Mock data CSV file has been created at {csv_file_path}')