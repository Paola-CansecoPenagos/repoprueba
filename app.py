from src import app
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

if __name__ == '__main__':
    app.run(debug=True, port=5001)
