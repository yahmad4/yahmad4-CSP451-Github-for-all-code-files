from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        # Connect to PostgreSQL
        conn = psycopg2.connect(
            host="52.138.60.29",      # Replace with your database VM's public IP
            database="mydb",          # Database name
            user="flaskuser",         # Database user
            password="P@ssw0rd1234"   # Database password
        )
        cursor = conn.cursor()

        # Query the database
        cursor.execute("SELECT content FROM messages LIMIT 1;")
        message = cursor.fetchone()[0]

        # Close the connection
        conn.close()
        return f"Hello World - {message}"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
