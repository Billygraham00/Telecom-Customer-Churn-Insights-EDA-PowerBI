<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Customer Churn Exploratory Data Analysis (EDA)</title>
    <style>
        body {
            font-family: Arial, Helvetica, sans-serif;
            line-height: 1.6;
            margin: 40px;
            background-color: #ffffff;
            color: #333;
        }
        h1, h2, h3 {
            color: #2c3e50;
        }
        code {
            background-color: #f4f4f4;
            padding: 4px 6px;
            border-radius: 4px;
            font-size: 14px;
        }
        ul {
            margin-left: 20px;
        }
        .section {
            margin-bottom: 30px;
        }
        .highlight {
            background-color: #eef6ff;
            padding: 10px;
            border-left: 4px solid #3498db;
        }
    </style>
</head>

<body>

<h1>Customer Churn Exploratory Data Analysis (EDA)</h1>

<p>
This project performs a comprehensive <strong>Exploratory Data Analysis (EDA)</strong> on a telecom customer churn dataset.
The analysis is implemented using <strong>Python with Object-Oriented Programming (OOP)</strong>,
integrated with <strong>exception handling</strong> and <strong>logging</strong> for robustness.
</p>

<hr>

<div class="section">
<h2>📌 Project Objective</h2>
<ul>
    <li>Understand customer churn behavior</li>
    <li>Analyze demographic, service, billing, and contract patterns</li>
    <li>Visualize relationships between churn and multiple customer attributes</li>
    <li>Prepare insights for churn prediction and retention strategies</li>
</ul>
</div>

<div class="section">
<h2>📂 Dataset Information</h2>
<ul>
    <li><strong>File Name:</strong> <code>Customer_Churn_Updated.csv</code></li>
    <li><strong>Type:</strong> CSV (Comma-Separated Values)</li>
    <li><strong>Domain:</strong> Telecom Customer Retention</li>
</ul>

<p class="highlight">
<b>Data Cleaning Performed:</b><br>
The <code>TotalCharges</code> column was converted from text to numeric format, and missing values were handled by replacing them with <code>0</code>.
</p>
</div>

<div class="section">
<h2>🛠 Technologies Used</h2>
<ul>
    <li>Python Programming Language</li>
    <li>Pandas & NumPy – Data manipulation and numerical analysis</li>
    <li>Matplotlib & Seaborn – Data visualization</li>
    <li>PyCharm IDE – Development and execution environment</li>
    <li>Logging Module – Execution tracking and error handling</li>
</ul>
</div>

<div class="section">
<h2>🏗 Project Structure</h2>
<ul>
    <li><code>eda.py</code> – Main EDA implementation using OOP</li>
    <li><code>log_code.py</code> – Logging configuration</li>
    <li><code>Customer_Churn_Updated.csv</code> – Dataset</li>
    <li><code>*.png</code> – Generated visualization outputs</li>
</ul>
</div>

<div class="section">
<h2>📊 Exploratory Data Analysis Overview</h2>

<p>The project includes <strong>22+ visualizations</strong>, covering:</p>

<ul>
    <li>Churn distribution analysis</li>
    <li>Gender vs churn patterns</li>
    <li>Senior citizen churn behavior</li>
    <li>Internet service usage trends</li>
    <li>Phone and multiple line usage analysis</li>
    <li>SIM operator-based comparisons</li>
    <li>Contract type distribution</li>
    <li>Paperless billing impact</li>
    <li>Payment method behavior</li>
    <li>Quarterly tenure analysis</li>
    <li>Monthly charges comparison by churn</li>
    <li>Region-wise demographic insights</li>
</ul>
</div>

<div class="section">
<h2>⚙ Implementation Highlights</h2>
<ul>
    <li>Object-Oriented Programming using a dedicated EDA class</li>
    <li>Centralized execution through a single <code>run_complete_eda()</code> method</li>
    <li>Try-except blocks for robust error handling</li>
    <li>Logging of execution status and runtime issues</li>
    <li>Automated saving of all visualization outputs</li>
</ul>
</div>

<div class="section">
<h2>▶ How to Run the Project</h2>
<ol>
    <li>Clone the repository</li>
    <li>Ensure Python dependencies are installed</li>
    <li>Update the dataset path if required</li>
    <li>Run the script:
        <br><br>
        <code>python eda.py</code>
    </li>
</ol>
</div>

<div class="section">
<h2>📈 Output</h2>
<ul>
    <li>All charts are saved automatically as PNG files</li>
    <li>Console logs track successful execution</li>
    <li>Errors (if any) are logged with line numbers</li>
</ul>
</div>

<div class="section">
<h2>✅ Conclusion</h2>
<p>
This EDA project provides deep insights into customer churn behavior and builds a strong analytical foundation
for predictive modeling and customer retention strategies.
</p>
</div>

<hr>

<p><i>Developed as part of a Data Analytics / Machine Learning learning project.</i></p>

</body>
</html>
