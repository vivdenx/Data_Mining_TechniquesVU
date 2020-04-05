import pandas as pd
import numpy as np


def read():
    data = pd.read_csv('./data/dataset_mood_smartphone.csv')
    patients = np.unique(list(data.id))
    for i in patients:
        patient_data = data.loc[data.id == i]
        filename = ".patientData/patient" + i + ".csv"
        patient_data.to_csv(filename)
        logging.info(f'Patient data written to {filename}.')

if __name__ == '__main__':
    read()
