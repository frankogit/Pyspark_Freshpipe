# HelloFresh Data Engineering Test

Thank you for your interest in joining HelloFresh! As part of our selection process, all of our candidates must take the following test.
The test is designed to assess key competencies required in your role as a data engineer at HelloFresh.

Please submit your answers in a different branch and create a pull request. Please do not merge your own pull request.

_Note: While we love open source here at HelloFresh, please do not create a public repo with your test in! This challenge is only shared with people interviewing, and for obvious reasons we'd like it to remain this way._


# HelloFresh
At HelloFresh, our mission is to change the way people eat - forever. From our 2011 founding in Europe’s vibrant tech hub Berlin, we’ve become the global market leader in the meal kit sector and inspire millions of energized home cooks across the globe every week.
We offer our meal kit boxes full of exciting recipes and thoughtfully sourced, fresh ingredients in more than 13 countries, operating from offices in Berlin, New York City, Sydney, Toronto, London, Amsterdam and Copenhagen and shipped out more than 250 Million meals in 2019.
Data Engineering at HelloFresh
We ingest events from our Kafka Stream and store them in our DataLake on s3. 
Events are sorted by arriving date. For example `events/recipe_changes/2019/11/29`.
During events processing we heavily rely on execution day to make sure we pick proper chunk of data and keep historical results.
We use Apache Spark to work with data and store it on s3 in parquet format. Our primary programming language is Python.

# Exercise
## Overview
At HelloFresh we have a big recipes archive that was created over the last 8 years. 
It is constantly being updated either by adding new recipes or by making changes to existing ones. 
We have a service that can dump archive in JSON format to selected s3 location. 
We are interested in tracking changes to see available recipes, their cooking time and difficulty level.

## Task 1
Using Apache Spark and Python, read and pre-process rows to ensure further optimal structure and performance 
for further processing. 
Use the dataset on S3 as the input (https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json). It's fine to download it locally.

## Task 2
Using Apache Spark and Python read processed dataset from step 1 and: 
1. extract only recipes that have `beef` as one of the ingredients
2. calculate average cooking time duration per difficulty level

Total cooking time duration can be calculated by formula:
```bash
total_cook_time = cookTime + prepTime
```  

Criteria for levels based on total cook time duration:
- easy - less than 30 mins
- medium - between 30 and 60 mins
- hard - more than 60 mins.

## Deliverables
- A deployable Spark Application written in Python
- a README file with brief explanation of approach, data exploration and assumptions/considerations. 
You can use this file by adding new section or create a new one.
- a CSV file with average cooking time per difficulty level. Please add it to `output` folder.
File should have 2 columns: `difficulty,avg_total_cooking_time` and named as `report.csv`

## Requirements
- Well structured, object-oriented, documented and maintainable code
- Unit tests to test the different components
- Errors handling
- Documentation
- Solution is deployable and we can run it

## Bonus points
- Config handling
- Logging and alerting
- Consider scaling of your application
- CI/CD explained
- Performance tuning explained
- We love clean and maintainable code
- We appreciate good combination of Software and Data Engineering

Good Luck!


## Solution Overview- Franko Ortiz

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
