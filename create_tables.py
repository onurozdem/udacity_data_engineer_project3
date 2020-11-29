import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """ 
    This function, clear all table with given drop queries on sql_queries.py. 
    
    Args:
        cur (int): Cursor of AWS Redshift Cluster
        conn (str): Conenction of AWS Redshift Cluster

    """
    try:
        for query in drop_table_queries:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        raise e

def create_tables(cur, conn):
    """ 
    This function, create all table with given drop queries on sql_queries.py.
    These tables for ETL process. If taken any error this step you musn't run etl.py 
    script.
    
    Args:
        cur (int): Cursor of AWS Redshift Cluster
        conn (str): Conenction of AWS Redshift Cluster

    """
    try:
        for query in create_table_queries:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        raise e        

def main():
    """ 
    This script create new tables for ETL process. Firstly, if tables exists delete them.
    Secondly, create new empty tables for fresh ETL process.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
