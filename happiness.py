import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to load data
def load_data():
    df_2017 = pd.read_csv('2017.csv')
    df_2018 = pd.read_csv('2018.csv')
    df_2019 = pd.read_csv('2019.csv')
    return df_2017, df_2018, df_2019

df_2017, df_2018, df_2019 = load_data()

# Title
st.title("World Happiness Dashboard")

# Select the year
year = st.selectbox("Select the Year", ('2017', '2018', '2019'))

# Depending on the year selected, load the respective dataframe
if year == '2017':
    df = df_2017
    df.rename(columns={'Happiness.Rank': 'Rank', 'Happiness.Score': 'Score', 'Economy..GDP.per.Capita.': 'GDP per Capita',
                       'Health..Life.Expectancy.': 'Life Expectancy', 'Trust..Government.Corruption.': 'Corruption'}, inplace=True)
    country_col = 'Country'
elif year == '2018':
    df = df_2018
    df.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'Score': 'Score', 
                       'GDP per capita': 'GDP per Capita', 'Healthy life expectancy': 'Life Expectancy', 
                       'Perceptions of corruption': 'Corruption'}, inplace=True)
    country_col = 'Country'
else:
    df = df_2019
    df.rename(columns={'Overall rank': 'Rank', 'Country or region': 'Country', 'Score': 'Score', 
                       'GDP per capita': 'GDP per Capita', 'Healthy life expectancy': 'Life Expectancy', 
                       'Perceptions of corruption': 'Corruption'}, inplace=True)
    country_col = 'Country'

# Sidebar filters for GDP, Life Expectancy, and Freedom
st.sidebar.header("Filter Options")
min_gdp = st.sidebar.slider("Minimum GDP per Capita", float(df['GDP per Capita'].min()), float(df['GDP per Capita'].max()), float(df['GDP per Capita'].min()))
max_gdp = st.sidebar.slider("Maximum GDP per Capita", float(df['GDP per Capita'].min()), float(df['GDP per Capita'].max()), float(df['GDP per Capita'].max()))

min_life_expectancy = st.sidebar.slider("Minimum Life Expectancy", float(df['Life Expectancy'].min()), float(df['Life Expectancy'].max()), float(df['Life Expectancy'].min()))
max_life_expectancy = st.sidebar.slider("Maximum Life Expectancy", float(df['Life Expectancy'].min()), float(df['Life Expectancy'].max()), float(df['Life Expectancy'].max()))

# Filter the dataframe based on the sidebar inputs
df_filtered = df[(df['GDP per Capita'] >= min_gdp) & (df['GDP per Capita'] <= max_gdp) & 
                 (df['Life Expectancy'] >= min_life_expectancy) & (df['Life Expectancy'] <= max_life_expectancy)]

# Display the filtered data
st.write("Filtered Data", df_filtered)

# Visualization Options
st.subheader("Visualize Happiness Scores by Country")
viz_type = st.selectbox("Select Visualization Type", ("Bar Plot", "Scatter Plot"))

if viz_type == "Bar Plot":
    # Limit the number of countries displayed
    num_countries = st.slider("Number of Countries to Display", min_value=10, max_value=len(df_filtered), value=20)
    
    # Sort and limit the data to the top N countries
    df_filtered = df_filtered.sort_values(by='Score', ascending=False).head(num_countries)
    
    # Bar plot of happiness scores by country
    fig, ax = plt.subplots(figsize=(12, 8))  # Increase the figure size
    sns.barplot(x='Score', y=country_col, data=df_filtered, ax=ax, palette='viridis')
    
    # Rotate Y-axis labels for better readability
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, ha="right")
    ax.set_title(f'Happiness Scores by Country in {year}')
    
    st.pyplot(fig)


elif viz_type == "Scatter Plot":
    # Scatter plot with GDP per capita on X-axis and happiness score on Y-axis
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x='GDP per Capita', y='Score', hue=country_col, size='Life Expectancy', data=df_filtered, ax=ax, palette='coolwarm')
    ax.set_title(f'Happiness Score vs. GDP per Capita in {year}')
    st.pyplot(fig)

# Show statistical correlation matrix
if st.checkbox("Show Correlation Matrix"):
    st.subheader("Correlation Matrix")
    correlation_matrix = df_filtered.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)