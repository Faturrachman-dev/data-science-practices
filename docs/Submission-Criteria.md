Okay, let's break down this project submission and the criteria you need to meet. This will be a comprehensive guide to help you complete the "Salinan\_dari\_Proyek\_Analisis\_Data.ipynb" file while adhering to the given guidelines.

**Project Analysis and Submission Guide**

This guide will help you understand the requirements for your data analysis project submission, based on the provided criteria and the template notebook.

**I. Understanding the Requirements**

You are required to perform a data analysis project using one of the provided datasets, adhering to the following criteria:

*   **Kriteria 1: Dataset Selection**
    *   Choose **one** of these datasets:
        *   Bike Sharing Dataset
        *   E-Commerce Public Dataset
        *   Air Quality Dataset
*   **Kriteria 2: Complete Data Analysis Process**
    *   You must complete all steps of the data analysis process, from defining questions to drawing conclusions.
        *   **Minimum 2 Business Questions:** These questions must be effective according to the "Mendefinisikan Pertanyaan Untuk Explorasi Data" material.
        *   **Minimum 2 Visualizations:** Create at least two visualizations to answer your business questions.
*   **Kriteria 3: Organized Notebook**
    *   Use the provided template notebook (`Salinan_dari_Proyek_Analisis_Data.ipynb`).
    *   Document each step of the analysis using markdown/text cells to explain your process.
*   **Kriteria 4: Streamlit Dashboard**
    *   Create a simple interactive dashboard using Streamlit to showcase your analysis results.
    *   Ensure the dashboard runs correctly locally.

**II. Notebook Structure and Content**

Your notebook should follow the provided template with the following sections:

1.  **Project Header:**
    *   Your name, email, and Dicoding ID.
    *   Name of the dataset you chose.
2.  **Business Questions:**
    *   List the two business questions you will explore.
3.  **Import Libraries:**
    *   Import all necessary libraries (Pandas, NumPy, Matplotlib, Seaborn, Streamlit, etc.).
4.  **Data Wrangling:**
    *   **Gathering Data:**
        *   Load your chosen dataset.
        *   Write code to read the data into a Pandas DataFrame.
        *   **Insight:** Describe the dataset and its features.
    *   **Assessing Data:**
        *   Use methods like `info()`, `describe()`, `isnull()`, `duplicated()`, etc., to assess data quality.
        *   Identify data types, missing values, duplicates, outliers, and inconsistencies.
        *   **Insight:** Summarize the data quality issues found.
    *   **Cleaning Data:**
        *   Apply appropriate cleaning techniques (drop, fill, correct, etc.) to fix data issues.
        *   **Insight:** Describe how you handled data quality issues.
5.  **Exploratory Data Analysis (EDA):**
    *   **Explore:**
        *   Use descriptive statistics (`describe()`, `value_counts()`, etc.) and data grouping (`groupby()`, `pivot_table()`) to analyze and explore your data.
        *   Create different exploration steps based on the questions you intend to answer.
        *   **Insight:** Describe any patterns or trends found.
6.  **Visualization & Explanatory Analysis:**
    *   Use Matplotlib and Seaborn to create visualizations to answer each of your business questions.
    *   Add appropriate titles, labels, and legends to your charts.
    *   Include markdown/text cells to explain your visualizations and the insights they provide.
        *   **Pertanyaan 1:** Visualize to answer question 1.
        *   **Pertanyaan 2:** Visualize to answer question 2.
        *   **Insight:** Describe the insights from each visualization.
7.  **Advanced Analysis (Optional):**
    *   Include any advanced techniques that you choose to implement such as:
        *   RFM Analysis (Recency, Frequency, Monetary).
        *   Geospatial Analysis.
        *   Clustering (Manual Grouping, Binning).
    *   Remember that this must be relevant to the dataset and the business questions you have defined.
8.  **Conclusion:**
    *   Summarize the answers to your business questions based on your analysis and visualizations.
        *   **Conclusion:** Answer for question 1.
        *   **Conclusion:** Answer for question 2.

**III. Implementing Each Step**

Let's go through each section with code examples and explanations. (Note, I will not write executable code with the dataset because I don't have the data, but I will show you the proper functions to use).

**1. Project Header**

```markdown
# Proyek Analisis Data: Bike Sharing Dataset
- **Nama:** Faturrachman
- **Email:** faturrachman6773@gmail.com
- **ID Dicoding:** Faturrachman
```

**2. Business Questions**

```markdown
## Menentukan Pertanyaan Bisnis

- Pertanyaan 1: What are the peak hours for bike rentals and how do they vary across weekdays and weekends?
- Pertanyaan 2: How do weather conditions affect the number of bike rentals?
```

**3. Import Libraries**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st # If you want to use streamlit
from io import StringIO # If you want to use StringIO
```

**4. Data Wrangling**

   **a. Gathering Data**

```python
# Example for Bike Sharing dataset (replace 'your_dataset.csv' with your actual file)
df = pd.read_csv("your_dataset.csv")
print(df.head()) # Print head of the dataframe to see if it loaded properly
```

   **Insight:** Describe the dataset, its source, and the features present.

   **b. Assessing Data**

```python
# Inspect the data
print(df.info()) # Check data types and non-null values
print(df.describe()) # Get statistical summary
print(df.isnull().sum()) # Count missing values
print(df.duplicated().sum()) # Count duplicate rows
```

   **Insight:** Note data types, missing values, outliers, and inconsistencies.

   **c. Cleaning Data**

```python
# Example: Handling missing values (replace 'column_name' with the column with missing values)
df['column_name'].fillna(df['column_name'].mean(), inplace=True)

# Example: Handling duplicates
df.drop_duplicates(inplace=True)

# Example: Convert columns to appropriate data type
df['date'] = pd.to_datetime(df['date'])
```

   **Insight:** Document the cleaning steps and why you chose them.

**5. Exploratory Data Analysis (EDA)**

   **a. Explore...**

```python
# Example: Exploring peak hours
peak_hours = df.groupby(df['date'].dt.hour)['rental_count'].mean()
print("Peak hours for bike rentals:")
print(peak_hours)

# Example: Exploring how weather condition affects rental count
weather_rental = df.groupby('weather_condition')['rental_count'].mean()
print("Bike rentals by weather condition:")
print(weather_rental)
```

   **Insight:** Describe the patterns and trends you observed.

**6. Visualization & Explanatory Analysis**

   **a. Pertanyaan 1:**

```python
# Example: Visualizing peak hours
plt.figure(figsize=(10, 6))
plt.plot(peak_hours.index, peak_hours.values, marker='o')
plt.title('Average Bike Rentals by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Rental Count')
plt.grid(True)
plt.show()
```

   **b. Pertanyaan 2:**

```python
# Example: Visualizing the effect of weather on rentals
plt.figure(figsize=(10, 6))
sns.barplot(x=weather_rental.index, y=weather_rental.values)
plt.title('Average Bike Rentals by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Average Rental Count')
plt.show()
```

   **Insight:** Describe what each visualization shows and how it helps answer the questions.

**7. Analisis Lanjutan (Opsional)**

```python
# Example: RFM Analysis (you'll need to adapt this to your specific dataset and columns)
# Assuming your data contains customer_id, and date_time
# Convert date_time to datetime object
df['date_time'] = pd.to_datetime(df['date_time'])
current_date = df['date_time'].max()
rfm_df = df.groupby("customer_id").agg(
    recency = ('date_time', lambda x: (current_date - x.max()).days),
    frequency = ('date_time','count'),
    monetary = ('total_price','sum'),
    )
print(rfm_df.head())
```

**8. Conclusion**

```markdown
## Conclusion

- Conclution pertanyaan 1: Peak hours for bike rentals are typically during morning and evening commute times, with less activity during the day.
- Conclution pertanyaan 2: Bike rentals are higher during clear weather and lower during rainy or snowy conditions.
```

**IV. Creating a Streamlit Dashboard**

Create a new Python file (e.g., `streamlit_app.py`) and include the code to build your dashboard using Streamlit. Here's an example, remember to adapt this to your dataset and visualizations:

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming you have a DataFrame called 'df' from your analysis
# Load data here and do necessary preprocessing

# Streamlit App
st.title("Bike Rental Analysis Dashboard")

# Question 1 Visualization
st.header("Average Bike Rentals by Hour of Day")
st.pyplot(plt.figure(figsize=(10, 6))) # Assuming you named your chart's figure as plt.figure
plt.plot(peak_hours.index, peak_hours.values, marker='o')
plt.title('Average Bike Rentals by Hour of Day')
plt.xlabel('Hour of Day')
plt.ylabel('Average Rental Count')
plt.grid(True)

# Question 2 Visualization
st.header("Average Bike Rentals by Weather Condition")
st.pyplot(plt.figure(figsize=(10, 6))) # Assuming you named your chart's figure as plt.figure
sns.barplot(x=weather_rental.index, y=weather_rental.values)
plt.title('Average Bike Rentals by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Average Rental Count')

# Additional Analysis
st.header("RFM Analysis")
st.write(rfm_df.head())

st.header("Conclusion:")
st.write("- Peak hours for bike rentals are typically during morning and evening commute times, with less activity during the day.")
st.write("- Bike rentals are higher during clear weather and lower during rainy or snowy conditions.")

```

To run this app, use the command: `streamlit run streamlit_app.py`

**V. Grading Criteria**

*   **Rating 1:** All requirements met, but evidence of cheating/plagiarism.
*   **Rating 2:** All requirements met, but no recommended suggestions implemented.
*   **Rating 3:** All requirements met and at least 1 suggestion implemented.
*   **Rating 4:** All requirements met and at least 3 suggestions implemented.
*   **Rating 5:** All requirements met and all the suggestions are implemented.
*   **Recommendations:**
    *   Document each step using markdown/text cells.
    *   Create good visualizations using design principles and integrity.
    *   Deploy your dashboard to Streamlit Cloud.
    *   Implement advanced analysis (RFM, geospatial, clustering).

**VI. Key Takeaways and Tips**

*   **Understand the Data:** Spend time exploring and understanding your chosen dataset.
*   **Clear Questions:** Formulate specific, measurable, action-oriented, relevant, and time-bound questions.
*   **Document Thoroughly:** Explain each step of your analysis in your notebook.
*   **Effective Visualizations:** Apply the principles of effective data visualization to create clear and compelling charts.
*   **Streamlit Dashboard:** Design your dashboard to be user-friendly and interactive.
*   **Advanced Analysis:** Choose advanced techniques that are appropriate for your data and questions.
*   **Run Your App Locally:** Make sure that your dashboard works in local.

By following this comprehensive guide, you'll be well-equipped to create a successful data analysis project and meet all the required criteria for your submission. Remember to adapt the code examples to your specific dataset and business questions. Good luck!
