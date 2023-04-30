# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 23:28:53 2023

@author: RITHVIK
"""
import streamlit as st
import pickle
import database as db
import pdf
def preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,val,name ): 
    
            # Pre-processing user input
    loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))
    if sex=="male":
        sex=1 
    else: 
        sex=0
                    
    if cp=="Typical angina":
        cp=0
    elif cp=="Atypical angina":
        cp=1
    elif cp=="Non-anginal pain":
        cp=2
    elif cp=="Asymptomatic":
        cp=3
        
    if exang=="Yes":
        exang=1
    elif exang=="No":
        exang=0
            
    if fbs=="Yes":
        fbs=1
    elif fbs=="No":
        fbs=0
            
    if slope=="Upsloping: better heart rate with excercise(uncommon)":
        slope=0
    elif slope=="Flatsloping: minimal change(typical healthy heart)":
        slope=1
    elif slope=="Downsloping: signs of unhealthy heart":
        slope=2 
                
    if thal=="fixed defect: used to be defect but ok now":
        thal=2
    elif thal=="reversable defect: no proper blood movement when excercising":
        thal=3
    elif thal=="normal":
        thal=1
                
    if restecg=="Nothing to note":
        restecg=0
    elif restecg=="ST-T Wave abnormality":
        restecg=1
    elif restecg=="Possible or definite left ventricular hypertrophy":
        restecg=2
    
    heart_prediction= loaded_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])

    if (heart_prediction[0] == 1):
        heart_diagnosis = 'The person is having heart disease'
        st.warning(heart_diagnosis)
    else:
        heart_diagnosis = 'The person does not have any heart disease'
        st.success(heart_diagnosis)
    #db.insert_data(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,heart_diagnosis,name)
    val['Result']=heart_diagnosis
    db.insert_data(val,name)

    pdf.main(val)

                
def main(state,name):
    if state and name:
            #st.sidebar(f'hello {temp["name"]}')
    #name_display=temp["name"]
    #st.sidebar.title(f"Welcome {name_display}")
    
                # st.set_page_config(page_title="Heart Disease prediction")
        #st.sidebar.title(f"Welcome {name} !")
        st.title("HEART DISEASE PREDICTION")
        
        age=st.slider("Age", 0, 130, 25)
        sex = st.radio("Select Gender: ", ('male', 'female'))
        cp = st.selectbox('Chest Pain Type',("Typical angina","Atypical angina","Non-anginal pain","Asymptomatic")) 
        trestbps=st.slider('Resting Blood Sugar',1,500,185)
        chol=st.slider('Serum Cholestoral in mg/dl',1,500,185)
        fbs=st.radio("Fasting Blood Sugar higher than 120 mg/dl", ['Yes','No'])
        restecg=st.selectbox('Resting Electrocardiographic Results',("Nothing to note","ST-T Wave abnormality","Possible or definite left ventricular hypertrophy"))
        thalach=st.slider('Maximum Heart Rate Achieved',1,300,72)
        exang=st.selectbox('Exercise Induced Angina',["Yes","No"])
        oldpeak = st.number_input('ST depression induced by exercise')
        slope = st.selectbox('Heart Rate Slope',("Upsloping: better heart rate with excercise(uncommon)","Flatsloping: minimal change(typical healthy heart)","Downsloping: signs of unhealthy heart"))
        ca=st.slider('Number of Major Vessels Colored by Flourosopy',0,4,1)
        thal=st.selectbox('Thalium Stress Result',('normal','fixed defect: used to be defect but ok now','reversable defect: no proper blood movement when excercising',))
        
            # code for Prediction
        # creating a button for Prediction
        
        #val=[age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal]
        val={'age':age,'sex':sex,'cp':cp,'trestbps':trestbps,'restecg':restecg,
             "chol":chol,'fbs':fbs,'thalach':thalach,'exang':exang, 'oldpeak':oldpeak ,'slope':slope,
             'ca':ca,'thal':thal}
        st.button ("result", on_click=preprocess, args= (age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,val,name ))
      
            
            #heart_prediction = preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal )
                               
    """if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
                st.warning(heart_diagnosis)
            else:
                heart_diagnosis = 'The person does not have any heart disease'
                st.success(heart_diagnosis)
            db.insert_data(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,heart_diagnosis)
            t.main([age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal,heart_diagnosis])"""
