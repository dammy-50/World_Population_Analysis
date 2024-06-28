import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
url = 'https://raw.githubusercontent.com/datasets/population/master/data/population.csv'
df = pd.read_csv(url)

# Streamlit app layout
st.title("Global Population Dashboard")

# Sidebar for user inputs
st.sidebar.header("User Input Parameters")

# Dropdown for selecting a country
country = st.sidebar.selectbox('Select Country', df['Country Name'].unique())

# Slider for selecting the year range
years = st.sidebar.slider('Select Year Range', int(df['Year'].min()), int(df['Year'].max()), (int(df['Year'].min()), int(df['Year'].max())))

# Filter the dataframe based on user inputs
filtered_df = df[(df['Country Name'] == country) & (df['Year'] >= years[0]) & (df['Year'] <= years[1])]

# Line chart for population over the years
st.subheader(f'Population of {country} Over Years')
line_fig = px.line(filtered_df, x='Year', y='Value', title=f'Population of {country} Over Years')
st.plotly_chart(line_fig)

# Bar chart for population growth over the years
st.subheader(f'Population Growth of {country}')
bar_fig = px.bar(filtered_df, x='Year', y='Value', title=f'Population Growth of {country}')
st.plotly_chart(bar_fig)

# Scatter plot for population distribution in the selected ending year
st.subheader(f'Population Distribution in {years[1]}')
scatter_df = df[df['Year'] == years[1]]
scatter_fig = px.scatter(scatter_df, x='Country Name', y='Value', size='Value', size_max=60, title=f'Population Distribution in {years[1]}')
st.plotly_chart(scatter_fig)

# Display a world map using Plotly's built-in choropleth map
st.subheader('World Map')
fig = px.choropleth(df, locations='Country Name', locationmode='country names', color='Value',
                    hover_name='Country Name', projection='natural earth',
                    title='World Population Map', template='plotly')
st.plotly_chart(fig)
