import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """ 
    This function, start copy table queries for source data copy to staging table.
        
    Args:
        cur (int): Cursor of AWS Redshift Cluster
        conn (str): Conenction of AWS Redshift Cluster
    """
    i = 0
    for query in copy_table_queries:
        print("ilk{}".format(i))
        cur.execute(query)
        conn.commit()
        i +=1


def insert_tables(cur, conn):
    """ 
    This function, start insert table queries for insert data to main target tables.
    Data will moving from stagin table to main tables
    
    Args:
        cur (int): Cursor of AWS Redshift Cluster
        conn (str): Conenction of AWS Redshift Cluster
    """
    i = 0
    for query in insert_table_queries:
        print(i)
        cur.execute(query)
        conn.commit()
        i += 1


def main():
    """ 
    This function, orchestrate all stages of ETL for moving data from source to main target tables.
    Firstly, move data to staging table. Then, data will insert to main target tables.
    Data will distribute to related table in star schema. 
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
