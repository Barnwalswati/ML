import pickle
import numpy as np

path = 'models/slr_hpvsprice_predictor.pkl'
with open(path,'rb') as f:
    model = pickle.load(f)


hp = int(input('enter the horsepower of vehicle: '))
# convert this single value in to numpy 2d array
x = np.array([[hp]])
prediction = model.predict(x)
print(f'hp = {hp} \n=> price={prediction[0]}')    