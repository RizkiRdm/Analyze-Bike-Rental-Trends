# Pedal Power Predictor: Decoding Bike Rental Trends

---
This project presents an in-depth analysis of bike-sharing rental data to uncover key patterns and demand drivers. By integrating both daily and hourly datasets, this work addresses several crucial business questions relevant for operational optimization and understanding user behavior.

## The core analytical objectives include:

- Weather Impact Assessment: Exploring how various weather conditions (temperature, humidity, wind speed, specific weather situations) significantly influence bike rental volumes, providing insights for environment-driven operational strategies.

- Weekday vs. Weekend Usage Comparison: Quantifying the percentage difference in rental numbers between weekdays and weekends, highlighting variations in usage patterns that can guide resource allocation.

- Peak Hour Identification: Precisely determining 
daily peak bike rental hours, which is critical for capacity planning and time-based marketing initiatives.

- Annual Trend Analysis: Analyzing the evolution of bike rental trends from 2011 to 2012, revealing growth or shifts in usage patterns over time.

## Methodology

The project leverages Python programming with the pandas library for robust data manipulation and integration of the day.csv and hour.csv datasets. Analytical techniques are applied to extract actionable insights. The consolidated data includes comprehensive details on environmental conditions, temporal aspects (season, year, month, hour, holiday), and rental counts (casual, registered, total).

## Results & Implications

The findings from this analysis offer a clear understanding of bike rental demand dynamics, enabling more informed decision-making regarding inventory management, pricing strategies, station placement, and promotional campaigns, particularly when adapting to diverse weather conditions and fluctuating usage patterns throughout the week and year.

---

## Libraries Used

This project utilizes a standard suite of powerful Python libraries for data manipulation, analysis, and visualization:

* **pandas**: For efficient data structuring and manipulation.
* **numpy**: For numerical operations and array handling.
* **matplotlib**: For creating static, interactive, and animated visualizations.
* **seaborn**: For producing attractive and informative statistical graphics.
* **datetime**: For handling date and time objects.

---

## How to Run This Project Locally

Follow these simple steps to set up and run this analysis on your local machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RizkiRdm/bike-sharing-analytict.git](https://github.com/RizkiRdm/bike-sharing-analytict.git)
    cd bike-sharing-analytict
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv env
    source env/bin/activate  # For Windows users: env\Scripts\activate
    ```

3.  **Install all necessary dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```

5.  **Explore the analysis:**
    Open `Proyek_Analisis_Data.ipynb` and execute each cell to view the analysis results and findings.

6.  **Run the interactive dashboard:**
    ```bash
    streamlit run dashboard/main.py
    ```
