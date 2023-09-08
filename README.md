# secure-password-python

## Tests Unitaires

Les tests unitaires sont ségmenté en deux classes:

- `class TestGeneratePassword(unittest.TestCase)`

Liste des Fonctions de cette classe.

`test_generate_password_with_digits_and_symbols`

`test_generate_password_include_digits_only`

`test_generate_password_include_symbols_only`

`test_generate_password_without_digits_and_symbols`

`test_generate_password_invalid_length`

&nbsp;

- `class TestHashPassword(unittest.TestCase)`

Liste des Fonctions de la classe:

`test_hash_password_sha256`

`test_hash_password_md5`

`test_hash_password_invalid_algorithm`

&nbsp;

### Problèmes rencontrés

Dans l'écriture des tests unitaires, nous avons été confronté à divers problèmes.  
Nos tests ont échoués car notre algorithme de génération de mots de passe ne fonctionnait pas correctement.  
Pour resoud

&nbsp;

| N°  | Problèmes | Resolution | Observation |
| --- | --- | --- | --- |
| 1   | Nos tests ont échoués car notre algorithme de génération  <br>  <br>de mots de passe ne fonctionnait pas correctement. | Changement d'algorithme en s'assurant de prendre en compte la présence d'au moins un chiffre ou symbole lorsque ceux-ci sont spécifié. |     |
| 2   | On  | Selenium | Étape 2: Accéder à la page web |
| 3   | `test_generate_password_without_digits_and_symbols:` | selenium, Test Unitaire | Étape 3: Accéder à la page web |

## Tests fonctionnels

| Nom du cas de test | Objectif | Préconditions/requirements | ID et nom de l’étape | L’action attendue de l’utilisateur | L’action système attendue | Données de tests | Critères de réussite | Statut de test |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Affichage du formulaire | Vérifier l'affichage du formulaire | Selenium | Étape 1: Accéder à la page web | Accéder à l'URL du formulaire | Afficher le formulaire à l'écran | `taille: 5,`  <br>  <br>`CheckBox:"include_numbers", Hash_algorithm:"md5"` | Le formulaire s'affiche correctement | Success |
| Champ Longueur requis | Vérifier le message d'erreur sans entrer de longueur de mot de passe | Selenium | Étape 2: Accéder à la page web | Ne rien entrer dans le champ de longueur du mot de passe | Afficher un message d'erreur indiquant que le champ est requis | `taille: 18, CheckBox: "include_numbers", Hash_algorithm:""` | Le message d'erreur s'affiche correctement | Success |
| Générer sans options | `test_generate_password_without_digits_and_symbols:` | selenium, Test Unitaire | Étape 3: Accéder à la page web | Entrer une longueur de mot de passe valide | Cliquer sur le bouton "Générer" | `taille: 8,`  <br>  <br>`use_digits: False, use_symbols: False` | Le mot de passe est généré correctement | Success |
| Générer avec chiffres | `test_generate_password_include_digits_only:` | Test Unitaire | Étape 4: Accéder à la page web | Entrer une longueur de mot de passe valide | Cocher la case "Inclure des chiffres" | `taille: 8,`  <br>  <br>`use_digits: False, use_symbols: False` | Le mot de passe contient des chiffres | Success |
| Générer avec symboles sans chiffres | `test_generate_password_include_symbols_only` | Test unitaire | Étape 5: Accéder à la page web | Entrer une longueur de mot de passe valide | Cocher la case "Inclure des symboles" | `taille: 8,`  <br>  <br>`use_digits: False, use_symbols: True` | Le mot de passe contient des symboles | Success |
| Générer avec chiffres et symboles | `test_generate_password_with_digits_and_symbols:` | Test Unitaire | Étape 6: Accéder à la page web | Entrer une longueur de mot de passe valide | Cocher les cases "Inclure des chiffres" et "Inclure des symboles" | `taille: 8,`  <br>  <br>`use_digits: True, use_symbols: True` | Le mot de passe contient des chiffres et des symboles | Success |
| Longueur invalide | `test_generate_password_invalid_length:` | Selenium, Test unitaire | Étape 7: Accéder à la page web | Entrer une longueur de mot de passe invalide (par exemple, -5) | Afficher un message d'erreur indiquant que la longueur doit être un nombre positif | `taille: 4,`  <br>  <br>`use_digits: False, use_symbols: False` | Le message d'erreur s'affiche correctement | Success |
| Générer avec toutes les options | `test_generate_password_with_digits_and_symbols:` | Test unitaire | Étape 8: Accéder à la page web | Entrer une longueur de mot de passe valide | Cocher les cases "Inclure des chiffres" et "Inclure des symboles" | `taille: 8,`  <br>  <br>`use_digits: True, use_symbols: True` | Le mot de passe contient des chiffres et des symboles | success |
| Cas de test pour SHA-256 | `test_hash_password_sha256:` | Test Unitaire, Selenium | Étape 9: Appeler la fonction hash\_password | Entrer un mot de passe correct | Calculer le hachage SHA-256 du mot de passe | `password: "SAOK4D?Z", hashAlgorithm: "sha256"` | Le hachage SHA-256 est calculé correctement | success |
| Cas de test pour MD5 | `test_hash_password_md5:` | Test Unitaire, Selenium | Étape 10: Appeler la fonction hash\_password | Entrer un mot de passe correct | Calculer le hachage MD5 du mot de passe | `password: "SAOK4D?Z", hashAlgorithm: "md5"` | Le hachage MD5 est calculé correctement | Success |
| Cas de test pour algorithme non pris en charge | `test_hash_password_invalid_algorithm:` | Test Unitaire, selenium | Étape 11: Appeler la fonction hash\_password | Entrer un mot de passe correct | Lever une exception ValueError | `password: "SAOK4D?Z", hashAlgorithm: ""` | Une exception ValueError est levée | Success |

&nbsp;