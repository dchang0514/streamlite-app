import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Set the app title 
st.title('AutoMarket - Find Your Dream Car') 

# Add a welcome message 
st.header('Quality Used Cars at Unbeatable Prices!') 

# Load Data
df = pd.read_csv('./vehicles_us.csv')

# Explore Data and Handle missing values
# handling model_year missing value and convert type to integer
df['model_year'] = df['model_year'].fillna(0)
df['model_year'] = df['model_year'].astype(int)

# handle cylinder missing vakue
mode_value = df['cylinders'].mode()[0]
df['cylinders'] = df['cylinders'].fillna(mode_value)
df['cylinders'] = df['cylinders'].astype(int)

# handle odometer missing value
df['odometer'] = df['odometer'].fillna(0)

# handle paint_color missing value
df['paint_color'] = df['paint_color'].fillna('custom')

# handle is_4wd missing value
df['is_4wd'] = df['is_4wd'].fillna(0.0)
df['is_4wd'] = df['is_4wd'].astype(int)

# convert date_posted to date_time value
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Enrich data - split the 'model' column into two columns
df_split = df['model'].str.split(' ', expand=True)
df_split = df_split.fillna('')
df['brand'] = df_split[0]
df['model'] = df_split[1]

# adjust the column order
brand_column = df.pop('brand') 
df.insert(2, 'brand', brand_column)

# Sidebar controls for Histogram
st.sidebar.title("Histogram Controls")
select_columns = ['type', 'brand', 'price', 'days_listed', 'model_year']
column = st.sidebar.selectbox("Select Column", select_columns)  # Column to plot
bins = st.sidebar.slider("Number of Bins", 5, 50, 20)  # Number of bins
category_filter = st.sidebar.multiselect("Filter by Brand", df[column].unique(), default=df[column].unique())

# Filter data based on sidebar selection
filtered_data = df[df[column].isin(category_filter)]

# Create histogram
fig = px.histogram(filtered_data, x=column, nbins=bins, title="Histogram")
fig.update_layout(bargap=0.1)  # Adjust bar gap if desired

# Display plot
st.plotly_chart(fig)

# Raw data display option
show_histogram = st.sidebar.checkbox("Show Histogram Data")
if show_histogram:
    st.write(filtered_data)

# Streamlit sidebar to filter and control plot parameters
st.sidebar.title("Scatter Plot Controls")
x_axis = st.sidebar.selectbox("Choose X-axis:", df.columns)
y_axis = st.sidebar.selectbox("Choose Y-axis:", df.columns)
size = st.sidebar.slider("Marker Size:", 10, 200, 50)

# Create scatter plot
fig = px.scatter(
    df, x=x_axis, y=y_axis,
    size='price', color='brand',
    title="Interactive Scatter Plot",
    labels={'x': x_axis, 'y': y_axis},
    size_max=size
)

# Display plot
st.plotly_chart(fig)

# Raw data display option
show_scatter = st.sidebar.checkbox("Show Scatter Plot Data")
if show_scatter:
    st.write(df)