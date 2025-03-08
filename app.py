import streamlit as st
import pandas as pd
import numpy as np
st.title ("HELLO BRO")
df = pd.DataFrame({
'first_column' : [2,34,45,343],
'second column':[3,3,342,232],
})
st.write("Here is an example data frame")
st.write(df)
abc = pd.DataFrame(
    np.random.randn(20,4),columns=['a','b','c','d']
)
st.line_chart(abc)