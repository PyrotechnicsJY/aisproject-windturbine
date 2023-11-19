import streamlit as st
import numpy as np
import pandas as pd
from streamlit.logger import get_logger
 
rng = np.random.default_rng(12345)
tab1,tab2  = st.tabs(["Charts","Data Table"])
with tab1:
  
  st.title('Windfarm Monitoring Software')
  st.header('Air Temperature ')

  timearray = np.arange(0.0,100,1.0,dtype=float)

  muAt, sigmaAt = 0, 15
  dfAirTemp = pd.DataFrame(
  { 
    'Time in Minutes':timearray,
    'Heat in Farenheit': np.random.default_rng().normal(muAt, sigmaAt, 100) +100
  }
  )
  st.line_chart(dfAirTemp,x="Time in Minutes",y="Heat in Farenheit",color=["#E66446"],) 
  
  st.button("Start Heating pad")
  st.write("Please select a temperature for the heating pads")
  st.slider("Temperature in Farenheit",min_value=0,max_value=165,step=5,)
  

  st.header("Blade RPM")

  dfBladeRPM = pd.DataFrame(
    {
    'Time in Minutes':timearray,
    'Revolutions of Turbine Blades':np.random.default_rng().normal(0, 1.25, 100) +16,
    }
  )  
  st.line_chart(dfBladeRPM,x="Time in Minutes", y="Revolutions of Turbine Blades",color=["#8179F5"])
  
with tab2:
  st.header("Tables")
  col1, col2, col3 = st.columns(3)
  
  
  st.dataframe(dfAirTemp,width=750,hide_index=True,)
  st.dataframe(dfBladeRPM,width=750,hide_index=True,)  
