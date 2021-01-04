import frankoHelloFresh as fhf
from utils import functionFranko

###########################################################
###############  Callable Functions anc Classes created ###
###############  Owner   : Franko Ortiz
###############  Release : 12-2020
###########################################################

###############  If you have access & secret keys for use Boto S3 uncomment it, and setup you own credentials in ~/.aws/credentials and run :
#y = fhf.HelloFresh("HelloFresh_16-12-20","dwh-test-resources",  "recipes.json")


############### Otherwise no problem, only run using json already downloaded
y = fhf.HelloFresh("HelloFresh_17-12-20")

############## Now with the object instanced , run the object method
y.main_execution()

############## Additionally I created, a normal csv file and one encrypted file for security on public clouds
var_dec = functionFranko.decryptFranko('output/encrypted/outputFranko.csv.encrypted','key.key')
