import psycopg2

# Configuración de conexión directa
DB_HOST = "aws-0-us-east-1.pooler.supabase.com"
DB_PORT = "6543"
DB_NAME = "postgres"
DB_USER = "postgres.kcqdosjvlstitbeyeiqt"  # Este usuario sí es válido
DB_PASSWORD = "caparason5544"

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("✅ Conexión exitosa a la base de datos Supabase vía conexión directa.")
    conn.close()
except Exception as e:
    print("❌ Error al conectar a la base de datos:")
    print(e)
