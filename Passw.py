import secrets
import string
import os
from datetime import datetime

def generer_mot_de_passe(longueur=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    mot_de_passe = ''.join(secrets.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

def enregistrer_mot_de_passe(mot_de_passe, nom_service="mot_de_passe"):
    # Récupérer le chemin du bureau (compatible Windows/Mac/Linux)
    bureau = os.path.join(os.path.expanduser("~"), "Desktop")
    
    # Format du fichier
    nom_fichier = os.path.join(bureau, "mots_de_passe.txt")
    
    # Ajouter un horodatage
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(nom_fichier, "a") as fichier:
        fichier.write(f"[{now}] {nom_service}: {mot_de_passe}\n")
    
    print(f"Mot de passe enregistré dans : {nom_fichier}")

# --- Exemple d'utilisation ---
if __name__ == "__main__":
    mot_de_passe = generer_mot_de_passe(20)
    enregistrer_mot_de_passe(mot_de_passe, nom_service="CompteEmail")
