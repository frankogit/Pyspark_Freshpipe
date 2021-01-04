import unittest
from utils import functionFranko
import warnings
from cryptography.fernet import Fernet, InvalidToken

class TestHelloFresh(unittest.TestCase):
    '''
    # Uncommenct if have ~/.aws/credentials already set ( Boto )
    def test_get_json_from_s3(self):    # For a correct load from S3

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        #using a correct bucket and file, if return > 0 is OK
        self.assertTrue( functionFranko.get_json_from_s3 ( p_bucket="dwh-test-resources", p_json_file="recipes.json" ) >0 )


        #using a wrong bucket and file, if return = 0 is OK
        self.assertFalse( functionFranko.get_json_from_s3 ( p_bucket="oltp-test-resources", p_json_file="recipes2020.json" ) >0 )
    '''
    def test_get_difficult_level(self):    # For categorize the difficulty

        # using a value, expect a correct category
        self.assertEqual( functionFranko.get_difficult_level ( 180 ) , 'hard')

        # using a worng type, expect a rise error
        self.assertRaises( TypeError, functionFranko.get_difficult_level ,  'Some string' )

    def test_get_standard_time(self):    # For get a correct minute from cook and prep times

        # Using a value from json, get the time in minutes
        self.assertEqual( functionFranko.get_standard_time ( '2H30M' ) , 150)

        # using a worng type, expect a rise error
        self.assertRaises( TypeError, functionFranko.get_standard_time ,  17122020 )

if __name__ =='__main__':

    unittest.main(argv=['first-arg-is-ignored'], exit=False)