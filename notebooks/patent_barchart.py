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

#List of response fields
response_fields_list = [ "patent_firstnamed_assignee_city", "patent_firstnamed_assignee_country",
                        "patent_firstnamed_assignee_id", "patent_firstnamed_assignee_latitude", 
                        "patent_firstnamed_assignee_longitude","patent_firstnamed_assignee_state", 
                        "patent_firstnamed_inventor_city", "patent_firstnamed_inventor_country",
                        "patent_firstnamed_inventor_id", "patent_firstnamed_inventor_latitude", 
                        "patent_firstnamed_inventor_longitude", "patent_firstnamed_inventor_state",
                        "patent_num_cited_by_us_patents", "patent_number", "patent_title", 
                        "patent_type", "patent_year", "patent_date"]
#Filters for the results
patent_inv_country = "US"
patent_assignee_country = "US"


# Form the final url
base_url = 'https://api.patentsview.org/patents/query?q={"_gte":{'
parameter_1 = f'"patent_firstnamed_inventor_country":"{patent_inv_country}"'
parameter_2 = f'"patent_firstnamed_assignee_country":"{patent_assignee_country}"'
response_fields = '}}&f=['

url = base_url + parameter_1 + "," + parameter_2 + response_fields
final_url = url

for i in range(0, len(response_fields_list)):
    final_url = final_url + '"' + response_fields_list[i] + '",'
    #print(final_url)
final_url = final_url[:-1:]
final_url = final_url + ']' + '&o={"per_page": 10000} &s=[{"patent_number":"asc"}]'

print(final_url)

payload={}

response = requests.request("GET", final_url, data=payload)

#print(response.text)

patent_details_text = response.text

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

