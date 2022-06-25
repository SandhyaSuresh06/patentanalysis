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

#Load patent data from the patent_details.json file
patent_details = json.loads(patent_details_text)
print(type(patent_details))

#Create data frame
patent_details_df = pd.DataFrame(patent_details['patents'])

#Drop rows with NaN values
patent_details_df.dropna(inplace = True)
print(patent_details_df.info())

#Using groupby the number of patents by assignee city is retrieved and the results are stored in `cat_assignee_city_df` dataframe
cat_inventor_city = patent_details_df.groupby(['patent_firstnamed_inventor_city'])['patent_number'].count().sort_values(ascending=False).head(10)
cat_inventor_city_df = cat_inventor_city.to_frame()
cat_inventor_city_df.reset_index(inplace = True)
cat_inventor_city_df.rename(columns={"patent_firstnamed_inventor_city": "city", "patent_number": "no_of_patents"}, inplace = True)
cat_inventor_city_df.set_index(keys = 'city', inplace = True)

#Using groupby the number of patents by inventor city is retrieved and the results are stored in `cat_inventor_city_df` dataframe
cat_assignee_city = patent_details_df.groupby(['patent_firstnamed_assignee_city'])['patent_number'].count().sort_values(ascending=False).head(10)
cat_assignee_city_df = cat_assignee_city.to_frame()
cat_assignee_city_df.reset_index(inplace = True)
cat_assignee_city_df.rename(columns={"patent_firstnamed_assignee_city": "assignee_city", "patent_number": "no_of_patents"}, inplace = True)
cat_assignee_city_df.set_index(keys = 'assignee_city', inplace = True)

st.title('Patent Dashboard')
st.markdown('The dashboard will visualize the patent data retrieved from the patent API')

st.markdown('## **Patent data**')
st.dataframe(patent_details_df)

#Create Bar charts for visualizing the top assignee cities and top inventor cities using Streamlit
st.markdown('## **Patents by inventor city**')
st.bar_chart(cat_inventor_city_df)
st.markdown('## **Patents by assignee city**')
st.bar_chart(cat_assignee_city_df)

