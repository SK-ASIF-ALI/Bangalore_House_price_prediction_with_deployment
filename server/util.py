import json
import numpy as np
import pickle
__locations=None
__data_columns=None
__model=None


def get_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)




def getlocation():
    return __locations

def load_save_data():
    print("loading saved artifacts...start")
    global  __data_columns
    global __locations

    with open("./artifacts/Columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    global __model
    if __model is None:
        with open('./artifacts/bangalore_house_price_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")



if __name__ == '__main__':
    load_save_data()
    print(getlocation())
    print(get_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_price('kalhalli',1000, 3, 3))