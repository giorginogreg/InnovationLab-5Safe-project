import cv2
import numpy as np

# Carica la rete YOLOv3
net = cv2.dnn.readNet('./PyYAT-master/models/yolov3.weights', './PyYAT-master/models/yolov3.cfg')

# Carica i nomi delle classi
with open('./PyYAT-master/models/coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Imposta i parametri di rilevamento
confThreshold = 0.5
nmsThreshold = 0.4

# Apri il video
cap = cv2.VideoCapture('Train.avi')

# Cicla attraverso i frame del video
frame_num = 0
while True:
    # Leggi il frame dal video
    ret, frame = cap.read()
    if not ret:
        break

    # Prepara l'input per la rete YOLOv3
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    # Passa l'input alla rete YOLOv3 per il rilevamento degli oggetti
    net.setInput(blob)
    detections = net.forward()

    # Apri il file di output per il frame corrente
    out_file = open(f'output_{frame_num}.txt', 'w')

    # Cicla attraverso le rilevazioni
    for detection in detections:
        # Estrae l'informazione sulla classe e sulla confidenza
        scores = detection[5:]
        classId = np.argmax(scores)
        confidence = scores[classId]

        # Ignora le rilevazioni con una confidenza inferiore alla soglia
        if confidence > confThreshold:
            # Calcola le coordinate della bounding box
            bbox = detection[0:4] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
            bbox = bbox.astype(int)

            # Estrae le coordinate x, y, larghezza e altezza della bounding box
            x, y, width, height = bbox

            # Calcola le coordinate del centro e la larghezza e l'altezza della bounding box
            center_x = x + width / 2
            center_y = y + height / 2
            bbox_width = width / frame.shape[1]
            bbox_height = height / frame.shape[0]

            # Scrive l'etichetta in formato YOLO nel file di output
            label = f"{classId} {center_x} {center_y} {bbox_width} {bbox_height}"
            out_file.write(label + '\n')

    # Chiude il file di output per il frame corrente e incrementa il contatore del frame
    out_file.close()
    frame_num += 1


# Rilascia le risorse
cap.release()
cv2.destroyAllWindows()