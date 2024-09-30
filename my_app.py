from app.routes import app
import os


if __name__ == "__main__":
    app.run(host=os.getenv('host'), port=8089, debug=True)


