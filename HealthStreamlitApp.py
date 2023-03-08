import streamlit as st
import pandas as pd
from PIL import Image
import streamlit as st
import numpy as np
import pickle
import os 



st.title('Chronic Kidney Disease Prediction')

#adds image 
image = Image.open('./image/fnalkidney-comp_1087848275.png')
st.image(image, caption='Sunrise by the mountains')

st.write('''Chronic kidney disease (CKD) is when the kidneys are damaged and cannot correctly filter waste and excess fluids from the blood. 
About 37 million people in the United States have Chronic Kidney Disease (CKD). Early detection and diagnosis of CKD are essential to
preventing its progression to kidney failure. Machine learning models can assist in predicting CKD. This project is the user interface for 
a previous project of mine that uses National Center for Health Statistics (NCHS) data. Variables such as age, gender, medical history, and laboratory
test results will be used. By identifying patterns in the data, models can predict a patient's risk of developing CKD, allowing for early intervention and management.''')


#load data
#loaded_model = pickle.load(open('Trained_DT_model.sav', 'rb'))
 
def main():
    gender=st.selectbox('What is your gender?',[0,1])
    age=st.number_input('What is your age?',0,100)
    race=st.selectbox('What is your race/ethnicity?',[1,2])
    education=st.selectbox('What is your education level?',[1,2])
    married=st.selectbox('What is your maritial status?',[1,2])
    income=st.selectbox('What is your income?',[1,2])
    
    diagnosis=''
    

 # Create button to run model
if st.button("CKD Risk Result"):
    input_data = [[age]]  # Add more demographic variables...
    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)
    st.write("The predicted kidney disease status is", prediction)
    
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()
    
    

#create sidebar
st.sidebar.title("About CKD App")


with st.sidebar:
    st.write("""
            Please see your doctor for an accurate risk prediction. This tool is for learning purposes.  
            
            Please note that this tool is a work in progress. Contact me [here](mailto:ahobby@healthdatasciencenewsletter) or consider checking out [GitHub](https://github.com/AndreaHobby/CKD-Prediction/blob/main/Predicting%20Chronic%20Kidney%20Disease.ipynb) repository with any suggestions or questions.     
        """)




