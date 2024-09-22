# World-Happiness
This is a Streamlit-based application that allows users to visualize and explore the World Happiness data from years 2017, 2018 and 2019. The app provides interactive plots and filtering options to analyze the happiness scores of different countries based on key indicators like GDP per capita, life expectancy, and more.


## Dataset
The app uses the World Happiness Report dataset (https://www.kaggle.com/datasets/unsdsn/world-happiness), which contains:

- Country: The name of each country included in the dataset.
- Happiness Score: A measure of happiness based on various metrics.
- GDP per Capita: The economic output per person in the country.
- Life Expectancy: The average lifespan in each country.
- Other Variables: Such as Social Support, Freedom, Generosity, and more.
The dataset is available from 2015 to 2019 (here the dataset used is from 2017 to 2019), and you can select different years to visualize the data accordingly.

## Features
### Visualization:
- Bar Charts: Plot the happiness scores of countries for a specific year.
- Filter Options: Adjust filters like GDP per capita, life expectancy, and others to customize the visualization.

### Interactivity:
- Dynamic Filtering: Use sliders to filter data based on GDP, life expectancy, and other key metrics.
- Year Selection: Choose from the available dataset years (2017, 2018, 2019) to switch between different time periods.

## Setup Running the World Happiness App with Docker
1. Clone the repository : git clone https://github.com/zinebmechiche/World-Happiness
2. When you're in the root directory of the project, build the Docker image : docker build -t happiness .
3. Then, run the container for launching the app : docker run -p 8501:8501 happiness
4. To access the app: Open your browser and go to http://localhost:8501 to see the World Happiness app
