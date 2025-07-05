# Flight Data Analysis Project

This is a beginner project for exploring and cleaning flight data using Python and pandas.

## 📁 Project Structure

- `data/raw/flights.csv`: The original dataset.
- `data/processed/flights_clean.csv`: The cleaned dataset, saved after processing.
- `notebooks/Flight Data Exploration.ipynb`: Jupyter Notebook containing the data cleaning, exploration, and analysis.

## 📄 Dataset Description

The dataset contains flight information such as:

- Dates
- Departure and arrival times
- Airlines
- Delays
- Other flight-related details

The raw data is loaded from `data/raw/`, cleaned in the notebook, and then saved to `data/processed/`.

## 🚀 How to Run

1. Open `notebooks/Flight Data Exploration.ipynb`in Jupyter or VS Code.
2. Run the notebook cells to clean and analyze the data.
3. The cleaned data will be saved automatically to `data/processed/flights_clean.csv`.

## ✅ Requirements

- Python 3.x
- pandas
- jupyter

You can install them using:

```bash
pip install pandas jupyter
