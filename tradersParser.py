import dotenv
import os
import pandas as pd


def parse_traders():
    dotenv.load_dotenv()
    directory = os.getenv('TRADERS_DIRECTORY_PATH')

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            data_frame = pd.read_csv(file_path)

            first_column = data_frame.iloc[:, 0].tolist()
