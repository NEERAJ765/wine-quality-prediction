import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('trained_model.sav','rb'))

def wine_pred(input_data):
##  input_data = (7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if(prediction[0] == 1):
        return "good quality wine"
    else:
        return "bad quality wine"
    
    
def main():
    st.title('Wine Quality Prediction')  
    # input data 
    fixed_acidity = st.text_input('Fixed Acidity percentage (0-20)%')
    volatile_acidity = st.text_input('Volatile Acidity percentage (0-10)%')
    citric_acid = st.text_input('Citric Acid percentage (0.0-1.0)%')
    residual_sugar = st.text_input('Residual Sugar percentage (0-10)%')
    chlorides = st.text_input('Chlorides percentage (0.00-1.00)%')
    free_sulfur_dioxide = st.text_input('Free Sulfur Dioxide percentage (0-20)%')
    total_sulfur_dioxide = st.text_input('Total Sulfur Dioxide percentage (0-100)%')
    density = st.text_input('Density percentage (0.000-1.000)%')
    ph = st.text_input('pH value (3.00-4.00)%')
    sulphates = st.text_input('Sulphates percentage (0.00-1.00)%')
    alcohol = st.text_input('Alcohol percentage (8.0-12.0)%')   
    
    # prediction
    quality = ''
    
    #creating a button for prediction
    if st.button('Wine Quality Result : '):
        quality = wine_pred([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, ph, sulphates, alcohol])
        
    st.success(quality)
    
    
if __name__ == '__main__':
    main()
            