import pickle
import numpy as np

path = 'models/diamond_price_DT_predictor.pkl'
with open(path,'rb') as f:
    regr_model = pickle.load(f)

paleonium = int(input('Enter the Paleonium of diamond:'))
pressure = int(input('Enter the Pressure of diamond:'))
x = np.array([[paleonium,pressure]])
prediction = regr_model.predict(x)
print(f'paleonium = {paleonium} and pressure = {pressure} \n=> price={prediction[0]}')
