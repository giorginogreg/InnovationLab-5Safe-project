from flask import Flask, request, jsonify
import subprocess
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    # Salva l'immagine caricata
    image_file = request.files['image']
    image_path = 'uploaded_image.jpg'
    image_file.save(image_path)

    # Esegui lo script di rilevamento degli oggetti
    subprocess.call(['python', 'models/yolov5/detect.py', '--source', image_path])

    # Restituisci il risultato
    result_file = 'path/del/file/di/risultato.jpg'
    return jsonify({'result': result_file})


if __name__ == '__main__':
    app.run(debug=True)
