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

    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save('il_5safe/' + image_path)

    subprocess.call(
        [
            '/opt/poetry-venv/bin/python', 'models/yolov5/detect.py',
            '--weights', 'resources/weights/yolov5/best_model.pt',
            '--source', image_path,
            '--name', 'uploaded_image', '--exist-ok'
        ],
        cwd='/app/il_5safe',
    )

    result_file = image_path
    return jsonify({'result': 'uploaded_image/' + result_file})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")