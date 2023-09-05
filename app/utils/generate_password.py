import random
import string
import hashlib


def generate_password(length, use_digits=False, use_symbols=False):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def hash_password(password, hash_algorithm):
    if hash_algorithm == "sha256":
        hasher = hashlib.sha256()
    elif hash_algorithm == "md5":
        hasher = hashlib.md5()
    else:
        raise ValueError("Hash algorithm not supported")

    hasher.update(password.encode('utf-8'))
    hashed_password = hasher.hexdigest()
    return hashed_password


if __name__ == "__main__":
    length = int(input("Entrez la longueur du mot de passe : "))
    use_digits = input("Inclure des chiffres ? (Oui/Non) : ").strip().lower() == "oui"
    use_symbols = input("Inclure des symboles ? (Oui/Non) : ").strip().lower() == "oui"

    password = generate_password(length, use_digits, use_symbols)
    print("Mot de passe généré :", password)

    hash_choice = input("Voulez-vous hasher le mot de passe ? (Oui/Non) : ").strip().lower()
    if hash_choice == "oui":
        hash_algorithm = input("Choisissez l'algorithme de hashage (sha256/md5) : ").strip().lower()
        hashed_password = hash_password(password, hash_algorithm)
        print("Mot de passe hashé :", hashed_password)
