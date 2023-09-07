import unittest
from unittest.mock import Mock, patch
from cloud_processor import CloudProcessor

class TestCloudProcessor(unittest.TestCase):

    def test_process_payment_successful(self):
        password = "ULI100IJ" # mot de passe fictif a envoyé au test
        external_gateway_mock = Mock() # passerelle du cloud externe
        external_gateway_mock.save_password.return_value = True # simuler une sauvegarde reussie
        cloud_processor = CloudProcessor(external_gateway_mock) # créer l'instance avec la passerelle 
        result = cloud_processor.save_password(password) 

        external_gateway_mock.save_password.assert_called_once_with(password) # Vérifier que cloud_processor a bien appelé la passerelle externe avec le bon mdp

        # Si True, la passerelle du cloud externe a bien enregistré le mdp
        self.assertTrue(result)

    def test_process_payment_successful(self):
        password = "ULI100IJ" # mot de passe fictif a envoyé au test
        external_gateway_mock = Mock() # passerelle du cloud externe
        external_gateway_mock.save_password.return_value = False # simuler une sauvegarde reussie
        cloud_processor = CloudProcessor(external_gateway_mock) # créer l'instance avec la passerelle 
        result = cloud_processor.save_password(password) 

        external_gateway_mock.save_password.assert_called_once_with(password) # Vérifier que cloud_processor a bien appelé la passerelle externe avec le bon mdp

        # Si False, la passerelle du cloud externe retourne bien un false
        self.assertFalse(result)

  
if __name__ == '__main__':
    unittest.main()
