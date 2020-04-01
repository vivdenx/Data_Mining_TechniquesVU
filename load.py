import pandas as pd
import numpy as np  



def read():
    data = pd.read_csv(open('./dataset_mood_smartphone.csv'))
    print(data)


if __name__ == '__main__':
	read()
