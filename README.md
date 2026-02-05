<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Customer Churn Exploratory Data Analysis (EDA) & Dashboard</h1>

<p>
This project performs a comprehensive Exploratory Data Analysis (EDA) on a telecom
customer churn dataset and presents key insights using an interactive Power BI dashboard.
The analysis focuses on understanding customer behavior, service usage patterns,
billing preferences, and demographic factors that influence customer churn.
</p>

<hr>

<h2>Project Objectives</h2>
<ul>
    <li>Analyze customer churn patterns across demographics</li>
    <li>Understand service usage behavior and preferences</li>
    <li>Study billing, contract, and payment trends</li>
    <li>Identify key indicators contributing to customer churn</li>
    <li>Present business-ready churn insights using an interactive dashboard</li>
</ul>

<hr>

<h2>Technologies Used</h2>
<ul>
    <li>Python programming language</li>
    <li>Pandas and NumPy for data manipulation</li>
    <li>Matplotlib and Seaborn for data visualization</li>
    <li>PyCharm / Jupyter / Google Colab for development and execution</li>
    <li>Power BI for interactive dashboard and business insights</li>
    <li>CSV dataset format (Customer_Churn_Updated.csv)</li>
</ul>

<hr>

<h2>Project Structure</h2>
<ul>
    <li><b>eda.py</b> – Object-Oriented EDA implementation</li>
    <li><b>Customer_Churn_Updated.csv</b> – Input dataset</li>
    <li><b>log_code.py</b> – Logging configuration</li>
    <li><b>Generated PNG files</b> – Saved Python visualizations</li>
    <li><b>powerbi/Customer_Churn_Dashboard.pbix</b> – Power BI dashboard</li>
    <li><b>powerbi/dashboard.png</b> – Dashboard screenshot</li>
    <li><b>powerbi/Customer_Churn_Dashboard_Documentation.docx</b> – Dashboard documentation</li>
</ul>

<hr>

<h2>Implementation Highlights</h2>
<ul>
    <li>Object-Oriented Programming using a dedicated EDA class</li>
    <li>Centralized execution through a single <code>run_complete_eda()</code> method</li>
    <li>Try-except blocks for robust error handling</li>
    <li>Logging of execution flow and runtime issues</li>
    <li>Automated saving of all Python visualization outputs</li>
    <li>Separation of analysis (Python) and presentation (Power BI)</li>
</ul>

<hr>

<h2>Data Cleaning Steps</h2>
<ul>
    <li>Converted <b>TotalCharges</b> column from text to numeric format</li>
    <li>Handled missing values using business logic (zero charges for zero tenure)</li>
    <li>Validated dataset consistency before analysis</li>
</ul>

<hr>

<h2>Exploratory Data Analysis (Python)</h2>
<ul>
    <li>Overall churn distribution analysis</li>
    <li>Churn by gender and senior citizen status</li>
    <li>Service usage patterns (Internet, Phone, Multiple Lines)</li>
    <li>Contract type and billing behavior analysis</li>
    <li>Payment method impact on churn</li>
    <li>Tenure-based churn analysis</li>
    <li>Monthly charges comparison between churned and retained customers</li>
</ul>

<hr>

<h2>Power BI Dashboard</h2>

<p>
The Power BI dashboard provides a summarized and business-friendly view of customer churn.
It focuses on key KPIs and major churn drivers rather than repeating detailed EDA visuals.
</p>

<h3>Key KPIs</h3>
<ul>
    <li>Total Customers</li>
    <li>Churned Customers</li>
    <li>Churn Rate (%)</li>
    <li>Average Monthly Charges</li>
    <li>Average Tenure</li>
</ul>

<h3>Core Dashboard Visuals</h3>
<ul>
    <li>Churn Rate % by Contract Type</li>
    <li>Churn Rate % by Internet Service</li>
    <li>Churn Rate % by Payment Method</li>
    <li>Churn Rate % by Customer Tenure</li>
    <li>Churn by Senior Citizen</li>
</ul>

<h3>Interactive Filters</h3>
<ul>
    <li>Contract</li>
    <li>Internet Service</li>
    <li>Gender</li>
    <li>Senior Citizen</li>
    <li>Payment Method</li>
</ul>

<p>
Note: GitHub does not preview Power BI files.  
Please download the <b>.pbix</b> file and open it using <b>Power BI Desktop</b>.
A dashboard screenshot is provided for quick reference.
</p>

<hr>

<h2>Output</h2>
<p>
Python-based visualizations are saved as image files in the project directory.
The Power BI dashboard presents summarized insights through an interactive,
single-page business dashboard.
</p>

<hr>

<h2>Conclusion</h2>
<p>
This project combines Python-based exploratory data analysis with Power BI dashboarding
to deliver both deep analytical understanding and high-level business insights.
The findings can support customer retention strategies and serve as a foundation
for future predictive modeling.
</p>

</body>
</html>
