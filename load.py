import pandas as pd
import numpy as np


def read():
    data = pd.read_csv(open('./data/dataset_mood_smartphone.csv'))
    patients = np.unique(list(data.id))
    for i in patients:
        patient_data = data.loc[data.id == i]
        patient_data.to_csv("./patientData/patient" + i + ".csv")


if __name__ == '__main__':
    read()
