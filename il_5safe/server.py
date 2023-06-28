from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS
import os

app = Flask(
    __name__,
    static_folder='models/yolov5/runs/detect',
    # root_path='/app/il_5safe',
    static_url_path='',
)

CORS(app)


@app.route('/api/predict', methods=['POST'])
def predict():
    directory = "/app/upload"

    # Check if the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)  # If it doesn't exist, create it

    image_file = request.files['image']
    image_path = '/upload/uploaded_image.jpg'
    image_file.save(image_path)

    subprocess.call(
        [
            '/opt/poetry-venv/bin/python', 'models/yolov5/detect.py',
            '--weights', 'resources/weights/yolov5/best_model.pt',
            '--source', '/app' + image_path,
            '--name', 'uploaded_image', '--exist-ok'
        ],
        cwd='/app/il_5safe',
    )

    result_file = image_path
    return jsonify({'result': result_file})


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
