import pandas as pd
import os


def clean_time(in_filepath):
    data = pd.read_csv(in_filepath)
    data.rename(columns={"time":"old_time"},
                inplace=True)

    # Converting the time to a more readable format.
    for index, entry in data.iterrows():
        date, time = entry["old_time"].split()
        year, month, day = date.split("-")

        if time.endswith(":00.000") is True:
            time = time.replace(":00.000", "")
        data.at[index, "time"] = time
        data.at[index, "year"] = year
        data.at[index, "month"] = month
        data.at[index, "day"] = day

    data = data.drop(columns="old_time")
    data.to_csv(in_filepath)


def run():
    in_filepath = './data/dataset_mood_smartphone.csv'
    folderpath = "./patientData/"
    for path in os.listdir(folderpath):
        clean_time(folderpath+path)


if __name__ == "__main__":
    run()