from flask import Flask, request, jsonify
import os
import base64
import io
from PIL import Image
from werkzeug.utils import secure_filename
from module import predict_shot_attributes
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join('uploads', filename))
        result = predict_shot_attributes(filename)
        os.remove(os.path.join('uploads', filename))
        return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
