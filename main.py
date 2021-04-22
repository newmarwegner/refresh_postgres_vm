import psycopg2
from decouple import config

# function to connect with a database postgresql
def con_postgres(dbname='postgres', user='postgres'):

    return psycopg2.connect(f"dbname={config('dbname')} user={config('user')} host={config('host')} "
                            f"password={config('password')} port={config('port')}")

# function to refresh materialized views
# needs  .env file with materialized views separated by quote
def refresh_vm():
    views_to_refresh = config('vm_to_refresh').split(",")
    conn = con_postgres()
    cur = conn.cursor()
    
    for vm in views_to_refresh:
        sql = f"refresh materialized view concurrently {vm};"
        cur.execute(sql)
        conn.commit()
                            
    conn.close()
    
    return

if __name__ == '__main__':
    refresh_vm()
    print('Materialized views refreshed!')
