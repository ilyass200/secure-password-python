import random
import string
import hashlib


def generate_password(taille, use_digits=False, use_symbols=False):
    # Vérifier que la longueur est un entier compris entre 8 et 50
    if not (isinstance(taille, int) and 8 <= taille <= 50):
        raise ValueError("La longueur doit être un entier entre 8 et 50 inclus.")

    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    # Si l'utilisateur veut un chiffre, ajouter un chiffre aléatoire au mot de passe
    if use_digits:
        characters += random.choice(string.digits)
    # Si l'utilisateur veut un caractère de ponctuation, ajouter un caractère de ponctuation aléatoire
    if use_symbols:
        characters += random.choice(string.punctuation)
    # Générer le reste du mot de passe
    password = ''.join(random.choice(characters) for _ in range(taille))

    # Mélanger les caractères pour garantir l'aléatoire
    password_list = list(password)
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