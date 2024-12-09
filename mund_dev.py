import pandas as pd
import streamlit as st

st.title("muND development tool")

st.divider()
st.markdown("## Reference")

st.text_input("DOI")

with st.expander("if no DOI", expanded=False):
    st.text_input("Authors")
    st.text_input("Title")
    st.text_input("Journal")
    
    col1,col2,col3 = st.columns(3)
    with col1:
        st.text_input("Volume")
    with col2:
        st.text_input("Issue (optional)")
    with col3:
        st.text_input("pages")

st.divider()
st.markdown("## Exeprimental condition")

num_exp_cond = st.number_input("Number of experimental conditions", value=1)

facilities = ["J-PARC MLF","RCNP MuSIC","RAL-ISIS","PSI","TRIUMF"]
beamlines  = ["D1","D2","H1","H2","M1","RIKEN-Port1","RIKEN-Port4","muE4","piE1","M20","M9"]
methods    = ["Electron","Gamma","Neutron","Charged particle","Neutron","Fission fragment"]

exp_facility = []
exp_beamline = []
exp_method   = []

for id_exp_condition in range(0,num_exp_cond,1):
    col1,col2,col3 = st.columns(3)
    with col1:
        exp_facility.append(st.multiselect(
        "faclity",
        options=facilities,
        key="facility"+str(id_exp_condition)
        ))
    with col2:
        exp_beamline.append(st.multiselect(
        "beamline/area",
        options=beamlines,
        key="beamline"+str(id_exp_condition)
        ))
    with col3:
        exp_method.append(st.multiselect(
        "method",
        options=methods,
        key="method"+str(id_exp_condition)
        ))

# df = pd.DataFrame([exp_facility,exp_beamline,exp_method],columns=["faclity","beamline","method"])
df = pd.DataFrame(zip(*[exp_facility,exp_beamline,exp_method]),columns=["faclity","beamline","method"])

st.write(df)

st.divider()
st.markdown("## Data")

    
                
