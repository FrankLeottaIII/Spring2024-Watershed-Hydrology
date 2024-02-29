# Author: Frank R. Leotta
# Date: 2/28/2024

#Discription:   This is the second part of the streamlit  app, a more interactive version after you get the pet.

import streamlit as st
import pandas as pd

def oct_ET():
    # st.header(" please enter the PET value for october")
    oct_et = st.number_input("Enter the PET value for october", key="oct_et")
    # st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index", key="lai")
    # st.header("Please enter the precipitation for october")
    p = st.number_input("Enter the precipitation for october", key="p")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*oct_et + 0.04*p + 3.53*lai
    st.write("The ET for october is", ET)
    # et = str(ET)
    # st.header("The ET for october is", et),st.write("mm")
    # st.header(et)
    return ET


#To fix this error, please pass a unique `key` argument to
#`st.number_input`. fixed below
def nov_ET():

    nov_et = st.number_input("Enter the PET value for november", key="nov_et")
    lai1 = st.number_input("Enter the leaf area index", key="lai1")

    p1 = st.number_input("Enter the precipitation for november", key="p1")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*nov_et + 0.04*p1 + 3.53*lai1
    st.header("The ET for november is", ET)
    return ET


def dec_ET():
    st.header(" please enter the PET value for december")
    dec_et = st.number_input("Enter the PET value for december", key="dec_et")
    st.header(" Please enter the leaf area index here")
    lai2 = st.number_input("Enter the leaf area index", key="lai2")
    st.header("Please enter the precipitation for december")
    p2 = st.number_input("Enter the precipitation for december", key="p2")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*dec_et + 0.04*p2 + 3.53*lai2
    st.write("The ET for december is", ET)
    return ET

def jan_ET():
    # st.header(" please enter the PET value for january")
    jan_et = st.number_input("Enter the PET value for january", key="jan_et")
    # st.header(" Please enter the leaf area index here")
    lai_jan = st.number_input("Enter the leaf area index", key="lai_jan")
    st.header("Please enter the precipitation for january")
    p_jan = st.number_input("Enter the precipitation for january", key="p_jan")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*jan_et + 0.04*p_jan + 3.53*lai_jan
    st.write("The ET for january is", ET)
    return ET

def feb_ET():
    st.header(" please enter the PET value for february")
    feb_et = st.number_input("Enter the PET value for february")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for february")
    p = st.number_input("Enter the precipitation for february")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*feb_et + 0.04*p + 3.53*lai
    st.write("The ET for february is", ET)
    return ET

def mar_ET():
    st.header(" please enter the PET value for march")
    mar_et = st.number_input("Enter the PET value for march")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for march")
    p = st.number_input("Enter the precipitation for march")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*mar_et + 0.04*p + 3.53*lai
    st.write("The ET for march is", ET)
    return ET

def apr_ET():
    st.header(" please enter the PET value for april")
    apr_et = st.number_input("Enter the PET value for april")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for april")
    p = st.number_input("Enter the precipitation for april")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*apr_et + 0.04*p + 3.53*lai
    st.write("The ET for april is", ET)
    return ET

def may_ET():
    st.header(" please enter the PET value for may")
    may_et = st.number_input("Enter the PET value for may")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for may")
    p = st.number_input("Enter the precipitation for may")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*may_et + 0.04*p + 3.53*lai
    st.write("The ET for may is", ET)
    return ET

def jun_ET():
    st.header(" please enter the PET value for june")
    jun_et = st.number_input("Enter the PET value for june")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for june")
    p = st.number_input("Enter the precipitation for june")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*jun_et + 0.04*p + 3.53*lai
    st.write("The ET for june is", ET)
    return ET

def jul_ET():
    st.header(" please enter the PET value for july")
    jul_et = st.number_input("Enter the PET value for july")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for july")
    p = st.number_input("Enter the precipitation for july")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*jul_et + 0.04*p + 3.53*lai
    st.write("The ET for july is", ET)
    return ET

def aug_ET():
    st.header(" please enter the PET value for august")
    aug_et = st.number_input("Enter the PET value for august")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for august")
    p = st.number_input("Enter the precipitation for august")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*aug_et + 0.04*p + 3.53*lai
    st.write("The ET for august is", ET)
    return ET

def sep_ET():
    st.header(" please enter the PET value for september")
    sep_et = st.number_input("Enter the PET value for september")
    st.header(" Please enter the leaf area index here")
    lai = st.number_input("Enter the leaf area index")
    st.header("Please enter the precipitation for september")
    p = st.number_input("Enter the precipitation for september")
    #ET = 0.10 +0.64*PET + 0.04* P+3.53*LAi
    #pet = the potential evapotranspiration estimated by hamon method
    #P = the monthly precipitation(mm)
    #LAI = the leaf area index
    ET = 0.10 + 0.64*sep_et + 0.04*p + 3.53*lai
    st.write("The ET for september is", ET)
    return ET

def ET():
    oct_ET()
    nov_ET()
    dec_ET()
    jan_ET()
    feb_ET()
    mar_ET()
    apr_ET()
    may_ET()
    jun_ET()
    jul_ET()
    aug_ET()
    sep_ET()



def app():
    st.title("Find your Evapotranspiration for your forest!!!")
    st.header("This only applies to the forests catagorized as evergreen needleleaf trees\n(think pine trees, not rainforests)")
    oct_ET()
    nov_ET()
    dec_ET()
    jan_ET()
    feb_ET()
    mar_ET()
    apr_ET()
    may_ET()
    jun_ET()
    jul_ET()
    aug_ET()
    sep_ET()
if __name__ == "__main__":
    app()