# Project: Data Warehouse
This repository was created as part of my training on Udacity. For detailed information, you can check the https://www.udacity.com/course/data-engineer-nanodegree--nd027 link.

## Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

In this project, loading data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables. So, it will be S3 to Redshift staging and Redshift staging to Redshift tables etl. 

## Project Datasets
This project working with two datasets that reside in S3. Here are the S3 links for each:

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data
Log data json path: s3://udacity-dend/log_json_path.json

## ETL Pipeline
Scripts were created and added to the sql_queries.py file to create table, insert data, delete table and copy data.

By using the queries in this file in the create_table.py file, it is possible to create tables. For this, create_table.py file must be run before ETL processes. 

After the tables are created, the table will be ready for data entry. 

In this project, the data is located on S3 buckets. There are user activity logs on the app. Run sequentially in etl process, loading data from S3 to staging tables on Redshift and then loading data from staging tables to analytics tables on Redshift.


# Project Template
To get started with the project, you can find files at repository's main branch. You can clone or download the project template files from the repository, if you'd like to develop your project locally.

Alternatively, you can download the template files in the Resources tab in the classroom and work on this project on your local computer.

The project template includes four files:

  * `create_table.py` is where you'll create your fact and dimension tables for the star schema in Redshift.
  * `etl.py` is where you'll load data from S3 into staging tables on Redshift and then process that data into your analytics tables on Redshift.
  * `sql_queries.py` is where you'll define you SQL statements, which will be imported into the two other files above.
  * `README.md` is where you'll provide discussion on your process and decisions for this ETL pipeline.


## Project Running
* Firstly, you must run create tables:
  > python create_tables.py

* If you didn't get any error, you can start etl process:
  > python etl.py

After, all these steps, you complete first ETL process. If you want to continuosly or scheduled running this ETL process, you can use Cron Job or Airflow methods. 

**NOTE: You will not be able to run test.ipynb and etl.py until you have run create_tables.py at least once to create the sparkify keyspace, which these other files connect to.**


### Cron Job:
https://en.wikipedia.org/wiki/Cron

### Airflow Scheduling:
https://airflow.apache.org/docs/1.10.1/scheduler.html#:~:text=The%20Airflow%20scheduler%20monitors%20all,whether%20they%20can%20be%20triggered.
https://airflow.apache.org/docs/stable/scheduler.html

 

