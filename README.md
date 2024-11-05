# Web-based Exploration Data Analysis 

This project develops a web-based application to allow users to proform Exploration Data Analysis to a used car sales dataset by using Pandas, streamlit and Plotly platforms. The users can interactively communicate with the 
application in order to explore different prospectives of the car sales dataset. For example, a user can select a categrory column in order to observe  the distributions across different multiple categrory values.

The current version of the application,  two interactive data plots are supported:

1. Histogram - It used to represent the distribution of a continuous 
   variables (e.g. column 'brand') It shows how frequently data points fall within certain ranges or "bins," making it an excellent choice for visualizing the underlying shape of data.

2. Scatter Plot - It is used to present relationships between two quantitative   
   variables. It visually represents data points on a Cartesian plane, with one variable on the x-axis and the other on the y-axis. 


---

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)
- [License](#license)
- [Contact](#contact)

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/dchang0514/streamlite-app.git

2. **Navigate to the project directory:**
 ```bash
   cd streamlite-app

3. **Install dependencies:**
```bash
   pip install -r requirements.txt

## Usage
```bash
   streamlit run app.py

## Features

1. Interactive Histogram - It used to represent the distribution of a continuous 
   variables (e.g. column 'brand'). The histogram provides four control boxes:
   * Select Column - Select a column of the dataset as the x-axis
   * Number of bins - Configure to certain range for containing data points
   * Filter by Column - Select certain values of the selected column as a filter
   * Show data option - an option to select display raw data of the histogram

2. Interactive Scatter Plot - It is used to present relationships between two  
   quantitative variables. The histogram provides four control boxes:
   * Select x-axis - Select a column in order to put its values on x-axis
   * Select y-axis - Select a column in order to put its values on y-axis
   * Marker Size - Select size of the marker
   * Show data option - an option to select display raw data of the scatter plot

## Configuration
No configuration

## License
This project is licensed under the MIT License.

## Contact
Maintained by **David W. Chang**. For any inquiries, feel free to reach out via email at **dchang0514@gmail.com**.