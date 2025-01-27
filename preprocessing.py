import pandas as pd
import os
import logging

logging.basicConfig(format='%(asctime)s - %(message)s',
                    level=logging.DEBUG)

def clean_time(in_filepath):
    """
    Cleans the time into a more readable format with different columns for
        day, month and time. Year is removed because all data was acquired
        in 2014.
        #TODO: should I split hour and minutes too?
        #TODO: should I use the number of entries a day as a variable?

    :param in_filepath: path to the file that should be cleaned.
    """
    data = pd.read_csv(in_filepath)
    data.rename(columns={"time": "old_time"},
                inplace=True)

    # Converting the time to a more readable format.
    try:
        for index, entry in data.iterrows():
            date, time = entry["old_time"].split()
            year, month, day = date.split("-")

            if time.endswith(":00.000") is True:
                time = time.replace(":00.000", "")
            data.at[index, "time"] = time
            data.at[index, "month"] = month
            data.at[index, "day"] = day

        data = data.drop(columns="old_time")
        data.to_csv(in_filepath)
        logging.info(f"File at {in_filepath} cleaned.")
    except:
        logging.info(f"File at {in_filepath} already cleaned.")


def run():
    folderpath = "./patientData/"
    for path in os.listdir(folderpath):
        clean_time(folderpath + path)


if __name__ == "__main__":
    run()
