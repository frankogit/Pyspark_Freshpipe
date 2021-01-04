import findspark
findspark.init('/usr/local/spark-3.0.1-bin-hadoop3.2')

from utils import functionFranko
from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType,StringType
from pyspark.sql.functions import udf,round,col
import logging
import traceback
import sys
from cryptography.fernet import Fernet

class HelloFresh: 
    
    """ Main class for get complete HelloFresh Test  """
    
    def __init__(self, app_id,bucket=None,s3_json_file=None):
        
        #Constructor
        self.app_id = app_id
        self.bucket = bucket
        self.s3_json_file = s3_json_file
        
        #Set initial load, it means from s3 download the file and place in local
        if bucket:
            self.initial_load = functionFranko.get_json_from_s3 ( self.bucket , self.s3_json_file )
            
    
    def main_execution(self):
        
        """ Main function that generate the difficult and average """
        
        # Since this is a pyspark docker container(jupyter), sc is already added otherwise add sc here

        #Logging configuration
        logging.basicConfig(filename='logs/frankoHelloFresh.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        logging.disable(logging.DEBUG)
        
        # Stablish sparksession
        
        try:
                         
            spark = SparkSession \
                .builder \
                .appName("Test exam Franko Ortiz") \
                .config("spark.some.config.option", "HelloFresh") \
                .getOrCreate()        
            
            logging.info('SparkSession created ' )
                         
        except:
            
            logging.error(str(traceback.format_exc()))
            sys.exit()
            
        try:
                                                 
            # Read the file generated
            df = spark.read.json("inputFranko.json")

            logging.info('Input json file loaded' )
            
            # Instance from UDF
            getUniformTime_int = udf(lambda z: functionFranko.get_standard_time(z), IntegerType())
            getDifficLevel_str = udf(lambda z: functionFranko.get_difficult_level(z), StringType())

            # Ignore and missing in order to avoid breaks
            spark.sql("set spark.sql.files.ignoreCorruptFiles=true")
            spark.sql("set spark.sql.files.ignoreMissingFiles=true")

            # Create a temporary View
            df.createOrReplaceTempView("recipes")
            
            logging.info('PySpark SQL temp table created' )

            # Filter Beef and transform cooktime and preptime to minutes
            helloDF = spark.sql("SELECT name , cookTime , prepTime FROM recipes WHERE upper(ingredients) LIKE '%BEEF%'")
            helloDF = helloDF.withColumn('cccookTime',getUniformTime_int('cookTime')) \
                             .withColumn('ccprepTime',getUniformTime_int('prepTime'))
            helloDF = helloDF.withColumn('total_cook_time', col('cccookTime')+col('ccprepTime'))
            helloDF = helloDF.withColumn('DifficLevel',getDifficLevel_str('total_cook_time'))

            logging.info('Pyspark Dataframe - calculated total times and difficulty completed' )
            
            # From helloFresh dataframe calculate the average per difficult
            outputDF = helloDF.groupBy('DifficLevel') \
                                .avg('total_cook_time') \
                                .withColumnRenamed('avg(total_cook_time)','total_cook_time')                    

            # Only round and rename the columns as required in github
            outputDF = outputDF.select("DifficLevel", round(col('total_cook_time'))) \
                                .withColumnRenamed('round(total_cook_time, 0)','total_cook_time')
            
            logging.info('Prepared final Pyspark Dataframe ouput' )
            
            # Save the ouput to csv
            outputDF.toPandas().to_csv('output/outputFranko.csv',index=False)
            
            logging.info('Output file completed - ending application' )
            
            try :
                
                file = open('key.key', 'rb')  # Open the file as wb to read bytes
                key = file.read()  # The key will be type bytes
                file.close()
                
                input_file = 'output/outputFranko.csv'
                output_file = 'output/encrypted/outputFranko.csv.encrypted'

                with open(input_file, 'rb') as f:
                    data = f.read()  # Read the bytes of the input file

                fernet = Fernet(key)
                encrypted = fernet.encrypt(data)

                with open(output_file, 'wb') as f:
                    f.write(encrypted)  # Write the encrypted bytes to the output file
                    
                logging.info('Additional Encryption completed in ouput/encrypted folder' )
            
            except:           
            
                logging.error(str(traceback.format_exc()))
            
        except:           
            
            logging.error(str(traceback.format_exc()))

