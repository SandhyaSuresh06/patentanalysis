#Import necessary libraries
import json
from IPython.display import Image
import pandas as pd
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

patent_details_text = open('output/patent_details.json').read()

patent_details = json.loads(patent_details_text)
print(type(patent_details))

patent_details_df = pd.DataFrame(patent_details['patents'])
print(patent_details_df.info())

cat_inventor_city = patent_details_df.groupby(['patent_firstnamed_inventor_city'])['patent_number'].count().sort_values(ascending=False).head(10)
cat_inventor_city_df = cat_inventor_city.to_frame()
cat_inventor_city_df.reset_index(inplace = True)
cat_inventor_city_df.rename(columns={"patent_firstnamed_inventor_city": "city", "patent_number": "no_of_patents"}, inplace = True)
cat_inventor_city_df.set_index(keys = 'city', inplace = True)

st.bar_chart(cat_inventor_city_df)

