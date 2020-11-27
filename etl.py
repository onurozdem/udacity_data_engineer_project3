import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    i = 0
    for query in copy_table_queries:
        print("ilk{}".format(i))
        cur.execute(query)
        conn.commit()
        i +=1


def insert_tables(cur, conn):
    i = 0
    for query in insert_table_queries:
        print(i)
        cur.execute(query)
        conn.commit()
        i += 1


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()