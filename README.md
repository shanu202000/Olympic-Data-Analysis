---

# Summer Olympics Data Analysis

This project involves analyzing data from 280,000 athlete events across 29 Summer Olympics using Python. The analysis includes medal tallies, country-wise and athlete-wise statistics, and overall trends. An interactive website is built using Streamlit to visualize and explore the data.

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Analysis](#analysis)
- [Visualization](#visualization)
- [Interactive Website](#interactive-website)
- [Contributing](#contributing)
- [License](#license)

## Project Description

This project analyzes historical data of Summer Olympics from 1896 to 2016. Using Python and its libraries such as Pandas, NumPy, Seaborn, Matplotlib, and Plotly, we perform comprehensive data analysis. The key analyses include:

- Medal tally of countries
- Country-wise performance
- Athlete-wise performance
- Overall trends and insights

An interactive website is developed using Streamlit to allow users to explore the data and visualize the results.

## Installation

To run this project locally, you need to have Python installed on your system. Follow the steps below to set up the environment:

1. Clone the repository:
   ```sh
   git clone https://github.com/shanu202000/Olympic-Data-Analysis.git
   cd Olympic-Data-Analysis
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

After setting up the environment, you can start the Streamlit application by running:

```sh
streamlit run web.py
```

This will launch the interactive website where you can explore the Olympic data.

## Data

The dataset used in this project is sourced from Kaggle and contains detailed information on athlete participation data from 29 Summer Olympics. The data is preprocessed and cleaned before analysis.

## Analysis

### Medal Tally of Countries
We analyze the medal tally of different countries over the years, highlighting the top-performing nations.

### Country-wise Performance
Detailed analysis of each country's performance, including the number of medals won, popular sports, and standout athletes.

### Athlete-wise Performance
Insights into the performance of individual athletes, their achievements, and career highlights.

### Overall Trends and Insights
Exploration of overall trends in the Olympics, such as participation rates, gender distribution, and emerging sports.

## Visualization

We use various Python libraries for data visualization:
- **Seaborn** and **Matplotlib** for static plots and charts.
- **Plotly** for interactive visualizations.

These visualizations help in understanding the data and deriving meaningful insights.

## Interactive Website

The interactive website built using Streamlit allows users to:
- View and interact with visualizations.
- Filter data based on various parameters.
- Explore detailed analysis for countries and athletes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---


