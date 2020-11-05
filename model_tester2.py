import pickle
import numpy as np

path = 'models/slr_city-mpgvsprice.pkl'
with open(path,'rb') as f:
    model = pickle.load(f)


city_mpg = int(input('enter the city_mpg of vehicle: '))
# convert this single value in to numpy 2d array
x = np.array([[city_mpg]])
prediction = model.predict(x)
print(f'city_mpg = {city_mpg} \n=> price={prediction[0]}') 