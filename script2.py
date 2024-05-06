import numpy as np
import cv2
import tensorflow as tf

# Chemin vers le modèle TensorFlow Lite
model_path = '/chemin/vers/le/mobilnet_ssd_v1_coco_quant_postprocess.tflite'

# Chargement du modèle TensorFlow Lite
interpreter = tf.lite.Interpreter(model_path=model_path)
interpreter.allocate_tensors()

# Liste des chemins vers les images à traiter
images_list = ['/chemin/vers/image1.jpg', '/chemin/vers/image2.jpg', '/chemin/vers/image3.jpg']

# Fonction pour effectuer l'inférence sur une image
def perform_inference(image_path):
    image = cv2.imread(image_path)
    image = cv2.resize(image, (300, 300))  # Redimensionner l'image selon les spécifications du modèle
    input_data = (np.float32(image) - 127.5) / 127.5  # Normalisation des valeurs de pixels
    input_data = np.expand_dims(input_data, axis=0)

    # Chargement des données d'entrée dans le modèle
    interpreter.set_tensor(input_details[0]['index'], input_data)

    # Exécution de l'inférence
    interpreter.invoke()

    # Récupération des résultats de l'inférence
    output_data = interpreter.get_tensor(output_details[0]['index'])

    # Affichage des résultats de l'inférence
    print(f"Résultats de l'inférence pour {image_path} :", output_data)

# Exécution de l'inférence pour chaque image
for image_path in images_list:
    perform_inference(image_path)
