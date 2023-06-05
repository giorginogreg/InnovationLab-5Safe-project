import os

# Percorso della cartella in cui si trovano i file da rinominare
path = "./frames_training_dataset"

# Itera attraverso tutti i file nella cartella
for filename in os.listdir(path):
    # Verifica se il nome del file inizia con "output_"
    if filename.startswith("output_"):
        # Esegue la rinomina del file sostituendo "output_" con "frame_"
        new_filename = filename.replace("output_", "frame_00000")
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
