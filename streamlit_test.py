import numpy as np
import streamlit as st
import pandas as pd
import time

st.write('Hello world!')


# df = pd.DataFrame({'a': [1, 2, 3], 
#		   'b': [4, 5, 6]})

# st.line_chart(df)

# map_data = pd.DataFrame(
#	np.random.randn(1000,2) / [50,50] + [37.76, -122.4],
#	columns = ['lat','lon'])

# st.map(map_data)


# x = st.slider('x')
# st.write(x, 'squared is', x * x)

st.write('Starting a long computation...')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)


