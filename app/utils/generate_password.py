import random
import string
import hashlib
import re

def generate_password(taille, use_digits=False, use_symbols=False):
    if not (isinstance(taille, int) and 8 <= taille <= 50): # longueur entre 8 et 50
        raise ValueError("La longueur doit être un entier entre 8 et 50 inclus.")

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_digits:
        characters += random.choice(string.digits)
    if use_symbols: 
        characters += random.choice(string.punctuation)
    password = ''.join(random.choice(characters) for _ in range(taille)) # Générer le reste du mot de passe

    password_list = list(password) # Mélanger les caractères
    random.shuffle(password_list)
    return ''.join(password_list)


def hash_password(password, hash_algorithm):
    if hash_algorithm == "sha256":
        hasher = hashlib.sha256()
    elif hash_algorithm == "md5":
        hasher = hashlib.md5()
    else:
        raise ValueError("Algorithme de Hash non prit en compte")

    hasher.update(password.encode('utf-8'))
    hashed_password = hasher.hexdigest()
    return hashed_password

def check_complexity_password(password):
    complexity = "faible"  # par défaut
    
    if len(password) >= 15:
        complexity = "moyen"
    
    if any(char.isdigit() for char in password):
        complexity = "moyen"
    
    if any(char.isupper() for char in password):
        complexity = "moyen"
    
    if len(password) >= 30:
        complexity = "fort"

    include_symbols = re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)
    if len(include_symbols) >= 3:
        complexity = "fort"
    
    if sum(char.isdigit() for char in password) > 2 and len(include_symbols) > 2:
        complexity = "fort"
    
    return complexity

if __name__ == "__main__":
    taille = int(input("Entrez la longueur du mot de passe : "))
    use_digits = input("Inclure des chiffres ? (Oui/Non) : ").strip().lower() == "oui"
    use_symbols = input("Inclure des symboles ? (Oui/Non) : ").strip().lower() == "oui"

    password = generate_password(taille, use_digits, use_symbols)
    print("Mot de passe généré :", password)

    hash_choice = input("Voulez-vous hasher le mot de passe ? (Oui/Non) : ").strip().lower()
    if hash_choice == "oui":
        hash_algorithm = input("Choisissez l'algorithme de hashage (sha256/md5) : ").strip().lower()
        hashed_password = hash_password(password, hash_algorithm)
        print("Mot de passe hashé :", hashed_password)