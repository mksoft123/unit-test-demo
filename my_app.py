from app.routes import app
import os

if __name__ == "__main__":
    host = os.getenv('HOST', '0.0.0.0')  # Default to '0.0.0.0' if not set
    app.run(host=host, port=8089, debug=True)
