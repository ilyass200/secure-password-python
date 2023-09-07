class CloudProcessor:
    def __init__(self, external_gateway):
        self.external_gateway = external_gateway
    
    def save_password(self, password):
        try: 
            # Utilisation de la passerelle du cloud externe pour effectuer la sauvegarde
            result = self.external_gateway.save_password(password)
            if result:
                return True # Sauvegarde réussie
            else: 
                return False # Sauvegarde echouée
        except Exception as e:
            # Gérer les exceptions liées au cloud (ex: une connexion réseau perdue)
            print(f"Erreur lors du traitement de la sauvegarde du mot de passe : {str(e)}")
            return False