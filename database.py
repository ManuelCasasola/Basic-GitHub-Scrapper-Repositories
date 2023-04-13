import psycopg2

def save_to_database(data):
    #Conexión a la base de datos
    conn = psycopg2.connect( 
        host="localhost",
        database="GitHub",
        user="postgres",
        password="password"
    )
    
    # Create a cursor object
    cur = conn.cursor()
    
    #Creamos la tabla si no existe
    cur.execute("""
        CREATE TABLE IF NOT EXISTS github_repos (
            id SERIAL PRIMARY KEY,
            no INTEGER,
            repo TEXT,
            url TEXT
        )
    """)
    
    #Insertamos los datos en la tabla
    for row in data.itertuples():
        print(f"Inserting row: {row}")
        cur.execute("""
            INSERT INTO github_repos (no, repo, url) VALUES (%s, %s, %s)
        """, (row.No, row.Repo, row.URL))
        print(f"Row inserted")
    
    #Aseguramos los cambios y cerramos la conexión
    conn.commit()
    cur.close()
    conn.close()