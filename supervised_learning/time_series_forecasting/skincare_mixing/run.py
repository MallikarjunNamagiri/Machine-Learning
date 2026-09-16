
import os
from dotenv import load_dotenv

import src.app as app

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()  

    data_path = os.getenv("data_path")

    df = app.load_data(data_path)
    print("shape of the data:", df.shape)
    print("first 5 rows of the data:\n", df.head())