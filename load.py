import pandas as pd
import numpy as np  



def read():
    data = pd.read_csv(open('./dataset_mood_smartphone.csv'))
    for i in range(1,34):
    	patientNo = str(i)
    	patient = "AS14." + patientNo.zfill(2)
    	patient_data = data.loc[data.id==patient]
    	patient_data.to_csv("./patientData/patient" + patientNo + ".csv")
        

if __name__ == '__main__':
	read()
