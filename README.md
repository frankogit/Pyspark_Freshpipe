# HelloFresh Data Engineering Test - Franko Ortiz

## Solution Overview

I used this tree directory:

```bash
├── utils
│   └── functionFranko.py
├── ouput
│   ├── outputFranko.csv
│   └── encrypted
│	├── outputFranko.csv.encrypted
│       └── outputFranko_decrypted.csv
├── logs   
│   └── frankoHelloFresh.log
├── execution_file.py
├── frankoHelloFresh.py
├── test_functionFranko.py
├── inputFranko.json
├── requirements.txt
├── key.key
└── README.md
```

I considered functions for: get the minutes from strings, categorize the minutes(hard,easy,medium), and get the files from S3 they are in `utils\functionFranko.py`. 
The output are in output folder(including encrypted ouput), logs resides in his folder and I implemented a class `frankoHelloFresh.py` for intance an object and 
call functions that contain pyspark.
Ways to execute is running `execution_file.py` or `test_functionFranko.py` in order to do test units. The input file `inputFranko.json` can be donwloaded 
by running the `execution_file.py` or can run with a already downloaded file if no have aws credentials, Finally `requirements.txt` contains libraries to install 
and `key.key` is a key that I generate for hide content if you prefer.

## Up environment

I love use docker
>docker run -d --name pyspark -e "TZ=America/Lima" -p 3000:8888 jupyter/pyspark-notebook

Go in container
>docker exec -it --user root pyspark /bin/bash

Get the project
>Git clone franko_branch_example

Install requirements
>pip install -r requirements.txt

Add aws secret keys and access keys if you prefer:
>nano ~/.aws/credentials

Based in your hadoop conf, edit line 2 of file `frankoHelloFresh.py`
>findspark.init('YOUR_HADDOP_PATH')

# Running application

This program will create an object and intance it. If you have aws credentials open python file and uncomment for get the file from S3, If not  is OK.
>python execution_file.py

![Image of execution](/img/runmainprogram.png)

Run tests, if have If you have aws credentials open python file and uncomment for test the file from S3, If not  is OK.
>python test_functionFranko.py

![Image of execution](/img/testunits.png)

Check logs
>tail -f -n 7 logs/frankoHelloFresh.log

![Image of execution](/img/hellologs.png)

Check content ouput
>cat output/outputFranko.csv

![Image of ouput](/img/ouput.png)

Check content ouput encrypted, decrypted is provided in the same folder
>cat output/encrypted/outputFranko.csv.encrypted

![Image of ouput encrypted](/img/encrypted.png)

## Requirements - List Check
- Well structured, object-oriented, documented and maintainable code **-I created a class is readbale and easy to change**
- Unit tests to test the different components **-I included unit test**
- Errors handling **-I included error debug application and show errors**
- Documentation **-By the moment I have commented code and .md file**
- Solution is deployable and we can run it **-I' using docker container - microservices, if prefer move to your standlone/yarn spark**

## Bonus points - List Check
- Config handling **-I used aws credentials in a file, also key file. If is need to connect DB config handling/service account is good**
- Logging and alerting **-I included logs if have some prometheus or Elasticsearch can set alerts can monitor the log**
- Consider scaling of your application **-If the File higher increases we can consider chunk the file, Since Spark is a memory solution**
- Consider scaling of your application **-Also check the cost of the application process and get execution plan helps to apply improves**
- Consider scaling of your application **-Another alternative is use threads in some cases, i used in java for big one time loads**
- CI/CD explained **-Code is in repo, we are using versioning, dependencies are handle. When i think in microservices i remember Kafka apps**
- Performance tuning explained **-I used the mininum required dataframes & sparkSQL, practices like cache compressed, parallel partitions, hints in sparkSQL can improve performance**
- We love clean and maintainable code **-I hope I have achieved it :)**
- We appreciate good combination of Software and Data Engineering **-Nice & thanks, i want to meet you !**

Good Luck!
