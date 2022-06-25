# Patent Data Analysis

This project focuses on analyzing the patent information retrieved from the patentsview API. The PatentsView API is intended to inspire the exploration and enhanced understanding of US intellectual property (IP) and innovation systems.

The base endpoint url for the patent API is given as follows.

Patentsview (https://patentsview.org/apis/api-endpoints/patents)
This API version does not require any API key and has the following query parameters embedded to the url.

q - query paramters (Ex: patent_inv_country : "US")
f - JSON response fields (Ex: [patent_number", "patent_title", "patent_date"])
s - sort the results (Ex: "patent_number":"asc")
o - result options (Ex: "per_page": 10000)

Data Files:

* patent_details.json - Patent details retrieved from the API.

* PatentDataAnalysis.ipynb is the jupyter notebook containing the data analysis and visualization of patent data.

* PatentDataAnalysis.html is the html version of the jupyter notebook and is available in the reports folder.

* patent_barchart.py is the python file containing streamlit visualizations.


In case you don't have all of the necessary packages installed, here is a code you can run in jupyter notebook.

```
$ conda install -c plotly plotly=4.14.3
$ pip install streamlit
$ conda install -c anaconda ipywidgets
```

To run streamlit from anaconda prompt, run the following command from the project notebooks folder.

streamlit run patent_barchart.py
