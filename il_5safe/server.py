from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__,
            static_folder='models/yolov5/runs/detect',
            static_url_path='',
            )
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    # Salva l'immagine caricata
    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save(image_path)

    # Esegui lo script di rilevamento degli oggetti
    subprocess.call(
        ['python', 'models/yolov5/detect.py', '--source', image_path, '--name', 'uploaded_image', '--exist-ok'])

    # Restituisci il risultato
    result_file = '/uploaded_image/' + image_path
    return jsonify({'result': result_file})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")