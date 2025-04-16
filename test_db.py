import psycopg2
import os

# Obtener las variables de entorno (o usar los valores que proporcionaste directamente)
DB_NAME = os.getenv("PGDATABASE", "postgres")
DB_USER = os.getenv("PGUSER", "postgres.kcqdosjvlsltibeyeiqt")
DB_PASSWORD = os.getenv("PGPASSWORD", "caparason5544")
DB_HOST = os.getenv("PGHOST", "aws-0-us-east-1.pooler.supabase.com")
DB_PORT = int(os.getenv("PGPORT", "6543"))  # Convertir a entero

def test_database_connection():
    """
    Intenta establecer una conexión con la base de datos PostgreSQL.
    Imprime un mensaje de éxito o error según el resultado.
    """
    try:
        # Establecer la conexión
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        print("Conexión a la base de datos exitosa!")

        # Opcional: Realizar una operación simple para verificar la conexión
        # Por ejemplo, ejecutar una consulta
        cur = conn.cursor()
        cur.execute("SELECT 1;")  # Una consulta muy simple
        result = cur.fetchone()
        print("Resultado de la consulta de prueba:", result)

        # Cerrar la conexión
        cur.close()
        conn.close()

    except psycopg2.Error as e:
        print(f"Error al conectar a la base de datos: {e}")

if __name__ == "__main__":
    test_database_connection()