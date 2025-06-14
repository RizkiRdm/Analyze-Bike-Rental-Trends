# Pedal Power Predictor: Decoding Bike Rental Trends

---

## Project Overview: Unlocking Bike-Sharing Insights

This project delves into a comprehensive analysis of bike-sharing rental data to uncover key insights and answer critical business questions. By leveraging robust data analysis techniques, we aim to understand the dynamics of bike rental patterns and provide actionable conclusions.

**Key questions explored in this analysis include:**

* **Weather Impact:** How do various weather conditions influence the number of bike rentals?
* **Weekend vs. Weekday Trends:** What is the percentage increase in bike rentals on weekends compared to weekdays?
* **Peak Usage Identification:** Can we precisely identify the peak hours for bike rentals each day?
* **Annual Trends:** How did bike rental trends evolve from 2011 to 2012?

---

## Data

The dataset used for this project comprises two distinct files, offering a holistic view of the bike-sharing system:

* `day.csv`: Contains daily bike rental data, including total rentals, weather conditions, and holiday indicators.
* `hour.csv`: Provides detailed hourly bike rental information.

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
```
