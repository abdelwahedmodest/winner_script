import cv2
from gtts import gTTS
from moviepy.editor import VideoFileClip
import dlib
import numpy as np

# Étape 1: Reconnaissance Faciale
# Utilisation de Dlib pour détecter le visage et extraire les points fiduciaires

# Initialiser le détecteur de visages de Dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


# Charger l'image ou la vidéo
image_path = "me.jpg"  # Remplacez par le chemin de votre image ou vidéo
img = cv2.imread(image_path)

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Détecter les visages dans l'image
faces = detector(gray)

# Parcourir tous les visages détectés
for face in faces:
    # Obtenir les points fiduciaires du visage
    landmarks = predictor(gray, face)

    # Afficher les points fiduciaires sur l'image
    for n in range(0, 68):
        x = landmarks.part(n).x
        y = landmarks.part(n).y
        cv2.circle(img, (x, y), 1, (0, 255, 0), -1)

# Afficher l'image avec les points fiduciaires
cv2.imshow("Image avec points fiduciaires", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
