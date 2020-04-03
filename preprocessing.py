import pandas as pd
import os


def read_data(in_filepath):
    data = pd.read_csv(in_filepath)

    # Converting the time to a more readable format.
    for index, entry in data.iterrows():
        date, time = entry["time"].split()
        year, month, day = date.split("-")
        data.at[index, 'year'] = year
        data.at[index, 'month'] = month
        data.at[index, "day"] = day
    data.to_csv(in_filepath)


def run():
    in_filepath = './data/dataset_mood_smartphone.csv'
    folderpath = "./patientData/"
    for path in os.listdir(folderpath)[:5]:
        read_data(folderpath+path)


if __name__ == "__main__":
    run()