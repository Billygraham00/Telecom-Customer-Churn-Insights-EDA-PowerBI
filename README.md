<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Customer Churn Exploratory Data Analysis (EDA)</h1>

<p>
This project performs a comprehensive Exploratory Data Analysis (EDA) on a telecom
customer churn dataset. The analysis focuses on understanding customer behavior,
service usage patterns, billing preferences, and demographic factors that influence
customer churn.
</p>

<hr>

<h2>Project Objectives</h2>
<ul>
    <li>Analyze customer churn patterns across demographics</li>
    <li>Understand service usage behavior and preferences</li>
    <li>Study billing, contract, and payment trends</li>
    <li>Identify key indicators contributing to customer churn</li>
</ul>

<hr>

<h2>Technologies Used</h2>
<ul>
    <li>Python programming language</li>
    <li>Pandas and NumPy for data manipulation</li>
    <li>Matplotlib and Seaborn for data visualization</li>
    <li>PyCharm / Jupyter / Google Colab for development and execution</li>
    <li>CSV dataset format (Customer_Churn_Updated.csv)</li>
</ul>

<hr>

<h2>Project Structure</h2>
<ul>
    <li><b>eda.py</b> – Object-Oriented EDA implementation</li>
    <li><b>Customer_Churn_Updated.csv</b> – Input dataset</li>
    <li><b>log_code.py</b> – Logging configuration</li>
    <li><b>Generated PNG files</b> – Saved visualizations</li>
</ul>

<hr>

<h2>Implementation Highlights</h2>
<ul>
    <li>Object-Oriented Programming using a dedicated EDA class</li>
    <li>Centralized execution through a single <code>run_complete_eda()</code> method</li>
    <li>Try-except blocks for robust error handling</li>
    <li>Logging of execution flow and runtime issues</li>
    <li>Automated saving of all visualization outputs</li>
</ul>

<hr>

<h2>Data Cleaning Steps</h2>
<ul>
    <li>Converted <b>TotalCharges</b> column from text to numeric format</li>
    <li>Handled missing values by replacing them with zero</li>
    <li>Validated dataset consistency before analysis</li>
</ul>

<hr>

<h2>Visual Analysis Performed</h2>
<ul>
    <li>Churn distribution analysis</li>
    <li>Churn by gender and senior citizen status</li>
    <li>Service usage patterns (Internet, Phone, Multiple Lines)</li>
    <li>Internet service analysis by SIM operator and gender</li>
    <li>Contract and billing behavior analysis</li>
    <li>Payment method impact on churn</li>
    <li>Quarterly tenure analysis by SIM and churn</li>
    <li>Average monthly charges comparison</li>
    <li>Regional and demographic distribution analysis</li>
</ul>

<hr>


<h2>Output</h2>
<p>
All visualizations are generated automatically and saved as image files
in the project directory for further analysis and reporting.
</p>

<hr>

<h2>Conclusion</h2>
<p>
This EDA provides meaningful insights into customer churn behavior and
can be used as a foundation for predictive modeling and retention strategies.
</p>

</body>
</html>
