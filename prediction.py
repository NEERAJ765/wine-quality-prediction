import numpy as np;
import pickle

loaded_model = pickle.load(open('C:/Users/kunan/OneDrive/Desktop/cse/VS CODE/ml/projects/wine-quality/trained_model.sav','rb'))

input_data = (7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4)
input_data_as_numpy_array = np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if(prediction[0] == 1):
    print("good quality wine")
else:
    print("bad quality wine")