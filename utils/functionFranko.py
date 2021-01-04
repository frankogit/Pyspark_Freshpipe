import boto3
import os
from botocore.exceptions import NoCredentialsError
import json
import re
from cryptography.fernet import Fernet, InvalidToken

def get_standard_time(cook_prep_time):

    """ Purpose is convert from string like 3H20M or 1H or 30M to an integer(minutes) """

    resultTime=0

    if type(cook_prep_time) not in [str]:

        raise TypeError('Param should be string')

    try:
        
        #Hellofresh format data to a List (minutes) using regular expression
        reFindTime = re.findall(r'\d+H|\d+M',cook_prep_time)

        #from the list created clean and get the values for convert to minutes
        if(reFindTime):
            if len(reFindTime)>1:
                resultTime= int( reFindTime[0][0:-1] )*60 + int( reFindTime[1][0:-1] )

            elif reFindTime[0][-1:]=='H':    
                resultTime = int(reFindTime[0][0:-1])*60

            else:
                resultTime = int(reFindTime[0][0:-1])
    except:

        resultTime=0

    return resultTime


def get_difficult_level(lvl_minute):

    """ Get difficult level from a integer(minute) """

    if type(lvl_minute) not in [int]:            
        raise TypeError('Param should be an integer')

    #Apply rules in the test
    try:

        if lvl_minute < 30:
            return 'easy'
        elif (lvl_minute >= 30 and lvl_minute <=60):
            return 'medium'
        else:
            return 'hard'

    except:

        return 'error'

def get_json_from_s3(p_bucket,p_json_file):

	try:

		""" using aws secret and access key, get the the json file from S3"""
        
		to_json_file = []
        
		#get the file from s3, the convert to udf-8
		os.environ['AWS_PROFILE'] = "default"
		s3 = boto3.resource('s3')
		obj = s3.Object(p_bucket, p_json_file)
		body = obj.get()['Body'].read().decode("utf-8").split('\n')

		#convert from list of string To string of json
		for l in body:

			try:
				to_json_file.append(json.loads(l))
			except:
				None

		#move list json to json file
		with open('inputFranko.json', 'w') as jsonfile:
			json.dump(to_json_file, jsonfile)


		return len(to_json_file)
		
	except:

		return 0


def decryptFranko(filename,key):

    """ Function to decrypt content file, if need to  move to public clouds """

    file = open(key, 'rb')  # Open the file as wb to read bytes
    key = file.read()  # The key will be type bytes
    file.close()

    input_file = filename
    output_file = 'output/encrypted/outputFranko_decrypted.csv'

    with open(input_file, 'rb') as f:
        data = f.read()  # Read the bytes of the encrypted file

    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(data)

        with open(output_file, 'wb') as f:
            f.write(decrypted)  # Write the decrypted bytes to the output file

        return True
    
    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")
        
        return False

