import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import warnings
warnings.filterwarnings("ignore")

from log_code import setup_logging
logger = setup_logging("customer_churn_eda")


class CUSTOMER_CHURN_EDA:

    def __init__(self, path):
        try:
            self.telecom_df = pd.read_csv(path)
            logger.info("CSV file loaded successfully")
            logger.info(f"Dataset shape: {self.telecom_df.shape}")
        except Exception as e:
            logger.error(f"Error loading CSV file: {e}")
            raise

    def run_complete_eda(self):
        try:
            telecom_df = self.telecom_df

            # ================= DATA CLEANING =================
            telecom_df["TotalCharges"] = pd.to_numeric(
                telecom_df["TotalCharges"], errors="coerce"
            )
            telecom_df["TotalCharges"].fillna(0, inplace=True)

            #1.Churn Distribution (%)

            churn_counts = telecom_df["Churn"].value_counts()
            churn_percent = churn_counts * 100 / len(telecom_df)

            plt.figure(figsize=(6, 4))
            bars = plt.bar(churn_counts.index, churn_percent, color=["green", "red"])

            for i in range(len(churn_percent)):
                plt.text(i, churn_percent[i], f"{churn_percent[i]:.1f}%", ha="center", va="bottom")

            plt.title("Customer Churn Distribution (%)")
            plt.xlabel("Churn Status")
            plt.ylabel("Percentage")

            plt.savefig("churn_distribution.png")
            plt.show()

            # 2.Gender vs Churn (%)

            gender_data = telecom_df.groupby("gender")["Churn"].value_counts(normalize=True) * 100

            gender_data.unstack().plot(
                kind="bar",
                figsize=(6, 4),
                color=["green", "red"]
            )

            plt.title("Gender vs Churn (%)")
            plt.xlabel("Gender")
            plt.ylabel("Percentage")

            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.show()

            # 3.Churned Customers by Gender & Senior Citizen

            churned_df = telecom_df[telecom_df["Churn"] == "Yes"]

            gender_senior = churned_df.groupby(["gender", "SeniorCitizen"]).size()
            gender_senior_pct = gender_senior / gender_senior.groupby(level=0).sum() * 100

            gender_senior_pct.unstack().plot(
                kind="bar",
                figsize=(6, 4),
                color=["blue", "orange"]
            )

            plt.title("Churned Customers by Gender & Senior Citizen Status")
            plt.xlabel("Gender")
            plt.ylabel("Percentage")

            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.legend(["Non-Senior", "Senior"], title="Senior Citizen")
            plt.savefig("gender_senior_churned.png")
            plt.show()

            # 4.Internet Service Usage by Gender

            # Group by Gender and Internet Service
            internet_gender = telecom_df.groupby(["gender", "InternetService"]).size()

            # Convert counts to percentage within each gender
            internet_gender_pct = internet_gender / internet_gender.groupby(level=0).sum() * 100

            # Plot with colors
            internet_gender_pct.unstack().plot(
                kind="bar",
                figsize=(7, 4),
                color=["green", "orange", "red"]
            )

            plt.title("Internet Service Usage by Gender")
            plt.xlabel("Gender")
            plt.ylabel("Percentage")

            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.savefig("internet_service_by_gender.png")
            plt.show()

            # 5.Phone Service Usage by Gender & Senior Citizen (Churned Customers)

            # Take only churned customers
            churned_customers = telecom_df[telecom_df["Churn"] == "Yes"]

            # Group by Gender, Senior Citizen and Phone Service
            phone_gender_senior = churned_customers.groupby(
                ["gender", "SeniorCitizen", "PhoneService"]
            ).size()

            # Convert counts to percentage within each Gender & SeniorCitizen group
            phone_gender_senior_pct = (
                    phone_gender_senior
                    / phone_gender_senior.groupby(level=[0, 1]).sum()
                    * 100
            )

            # Plot
            phone_gender_senior_pct.unstack().plot(
                kind="bar",
                figsize=(8, 4),
                color=["green", "red"]
            )

            plt.title("Phone Service Usage by Gender & Senior Citizen (Churned Customers)")
            plt.xlabel("Gender, Senior Citizen")
            plt.ylabel("Percentage")

            # Add percentage labels
            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.savefig("phone_service_gender_senior_churned.png")
            plt.show()

            # 6.Multiple Lines Usage by Gender & Senior Citizen

            multi_lines_data = churned_df.groupby(
                ["gender", "SeniorCitizen", "MultipleLines"]
            ).size()

            # Convert counts to percentage
            multi_lines_percent = (
                    multi_lines_data
                    / multi_lines_data.groupby(level=[0, 1]).sum()
                    * 100
            )

            # Plot
            multi_lines_percent.unstack().plot(
                kind="bar",
                figsize=(8, 4),
                color=["green", "orange", "red"]
            )

            plt.title("Multiple Lines Usage by Gender & Senior Citizen")
            plt.xlabel("Gender, Senior Citizen")
            plt.ylabel("Percentage")

            # Show percentage labels
            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.savefig("multiple_lines_usage_gender_senior.png")
            plt.show()

            # 7.MultipleLines by SIM Operator

            # Group by SIM Operator and MultipleLines
            sim_multiline_counts = telecom_df.groupby(
                ["SIM", "MultipleLines"]
            ).size()

            # Convert counts to percentage within each SIM Operator
            sim_multiline_percent = (
                    sim_multiline_counts
                    / sim_multiline_counts.groupby(level=0).sum()
                    * 100
            )

            # Plot
            sim_multiline_percent.unstack().plot(
                kind="bar",
                figsize=(8, 4),
                color=["green", "orange", "red"]
            )

            plt.title("Multiple Lines Usage by SIM Operator")
            plt.xlabel("SIM Operator")
            plt.ylabel("Percentage")

            # Add percentage labels
            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.legend(title="MultipleLines")
            plt.savefig("multiplelines_by_sim_operator.png")
            plt.show()

            # 8.Multiple Lines Usage by SIM Operator & Gender

            # Group by SIM, Gender and MultipleLines
            sim_gender_multiline = telecom_df.groupby(
                ["SIM", "gender", "MultipleLines"]
            ).size()

            # Convert counts to percentage within each SIM & Gender
            sim_gender_multiline_pct = (
                    sim_gender_multiline
                    / sim_gender_multiline.groupby(level=[0, 1]).sum()
                    * 100
            )

            # Plot
            sim_gender_multiline_pct.unstack().plot(
                kind="bar",
                figsize=(9, 4),
                color=["green", "orange", "red"]
            )

            plt.title("Multiple Lines Usage by SIM Operator & Gender")
            plt.xlabel("SIM Operator, Gender")
            plt.ylabel("Percentage")

            # Add percentage labels
            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.legend(title="MultipleLines")
            plt.savefig("multiplelines_by_sim_operator_gender.png")
            plt.show()

            # 9.Multiple Lines Usage by SIM, Gender & Senior Citizen

            # Group by SIM, Gender, SeniorCitizen and MultipleLines
            sim_gender_senior_multiline = telecom_df.groupby(
                ["SIM", "gender", "SeniorCitizen", "MultipleLines"]
            ).size()

            # Convert counts to percentage within each SIM, Gender & SeniorCitizen group
            sim_gender_senior_multiline_pct = (
                    sim_gender_senior_multiline
                    / sim_gender_senior_multiline.groupby(level=[0, 1, 2]).sum()
                    * 100
            )

            # Plot
            sim_gender_senior_multiline_pct.unstack().plot(
                kind="bar",
                figsize=(15, 4),
                color=["green", "orange", "red"]
            )

            plt.title("Multiple Lines Usage by SIM, Gender & Senior Citizen")
            plt.xlabel("SIM, Gender, Senior Citizen")
            plt.ylabel("Percentage")

            # Add percentage labels
            for container in plt.gca().containers:
                plt.bar_label(container, fmt="%.1f%%")

            plt.legend(title="MultipleLines")
            plt.savefig("multiplelines_by_sim_gender_senior.png")
            plt.show()

            # 10.Total Customers by Internet Service

            # Count customers by Internet Service
            internet_service_count = telecom_df["InternetService"].value_counts()

            # Plot pie chart
            plt.figure(figsize=(6, 6))
            plt.pie(
                internet_service_count.values,
                labels=internet_service_count.index,
                autopct=lambda p: f"{p:.1f}%\n({int(p * sum(internet_service_count) / 100)})",
                startangle=90,
                colors=["green", "orange", "red"]
            )

            plt.title("Total Customers by Internet Service Distribution")
            plt.tight_layout()
            plt.savefig("total_customers_by_internet_service_pie.png")
            plt.show()

            # 11.Internet Service Usage by SIM Operator

            # Create cross-tabulation of Internet Service and SIM
            service_sim_table = pd.crosstab(telecom_df["InternetService"], telecom_df["SIM"])
            print(service_sim_table)

            # Select required internet service rows
            service_sim_selected = service_sim_table.loc[
                ["DSL", "Fiber optic", "No"]
            ]

            # Plot with different colors
            plt.figure(figsize=(6, 4))
            axis = service_sim_selected.plot(
                kind="bar",
                color=["#4CAF50", "#FF9800", "#2196F3", "#9C27B0"]  # green, orange, blue, purple
            )

            plt.title("Internet Service Usage by SIM Operator")
            plt.xlabel("Internet Service")
            plt.ylabel("Customer Count")
            plt.legend(title="SIM")

            # Add value labels
            for container in axis.containers:
                axis.bar_label(container)

            plt.tight_layout()
            plt.savefig("internet_service_by_sim.png")
            plt.show()

            # 12.Internet Service Usage by SIM Operator & Gender

            # Filter customers who have internet service
            internet_df = telecom_df[telecom_df["InternetService"] != "No"]

            # Group by SIM, Gender and Internet Service
            grouped_data = (
                internet_df
                .groupby(["SIM", "gender", "InternetService"])
                .size()
                .unstack(fill_value=0)
            )

            # Create x-axis labels
            x_labels = [(idx[0], idx[1]) for idx in grouped_data.index]
            x_pos = np.arange(len(x_labels))
            bar_width = 0.35

            # Get DSL and Fiber Optic values
            dsl_values = grouped_data.get("DSL", 0)
            fiber_values = grouped_data.get("Fiber optic", 0)

            # Plot with different colors
            plt.figure(figsize=(14, 6))
            plt.bar(x_pos - bar_width / 2, dsl_values, bar_width, label="DSL", color="#03A9F4")  # light blue
            plt.bar(x_pos + bar_width / 2, fiber_values, bar_width, label="Fiber Optic", color="#E91E63")  # pink

            plt.xticks(x_pos, x_labels, rotation=20)
            plt.xlabel("SIM Operator / Gender")
            plt.ylabel("Customer Count")
            plt.title("Internet Service Usage by SIM Operator & Gender")
            plt.legend(title="Internet Service")
            plt.tight_layout()

            plt.savefig("internet_service_by_sim_operator_gender.png")
            plt.show()

            # 13.Internet Service Usage by SIM Operator, Gender & Churn

            # Consider only customers with internet service
            internet_only = telecom_df[telecom_df["InternetService"] != "No"]

            # Group by SIM, Gender and Churn
            churn_grouped = (
                internet_only
                .groupby(["SIM", "gender", "Churn"])
                .size()
                .unstack(fill_value=0)
                .reset_index()
            )

            # Prepare x-axis labels
            x_labels = [(row["SIM"], row["gender"]) for _, row in churn_grouped.iterrows()]
            x_pos = np.arange(len(x_labels))
            bar_width = 0.35

            # Churn counts
            no_churn_vals = churn_grouped["No"]
            yes_churn_vals = churn_grouped["Yes"]
            total_vals = no_churn_vals + yes_churn_vals

            # Plot
            plt.figure(figsize=(14, 6))
            plt.bar(x_pos - bar_width / 2, no_churn_vals, bar_width, label="No", color="#4CAF50")
            plt.bar(x_pos + bar_width / 2, yes_churn_vals, bar_width, label="Yes", color="#F44336")

            # Add percentage labels inside bars
            for i in range(len(x_pos)):
                plt.text(
                    x_pos[i] - bar_width / 2,
                    no_churn_vals[i] / 2,
                    f"{(no_churn_vals[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

                plt.text(
                    x_pos[i] + bar_width / 2,
                    yes_churn_vals[i] / 2,
                    f"{(yes_churn_vals[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

            plt.xticks(x_pos, x_labels, rotation=20)
            plt.xlabel("SIM Operator / Gender")
            plt.ylabel("Customer Count")
            plt.title("Internet Service Usage by SIM Operator, Gender & Churn")
            plt.legend(title="Churn")
            plt.tight_layout()

            plt.savefig("internet_service_by_sim_gender_churn.png")
            plt.show()

            # 14.OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies

            # List of service-related columns
            service_features = [
                "OnlineSecurity",
                "OnlineBackup",
                "DeviceProtection",
                "TechSupport",
                "StreamingTV",
                "StreamingMovies"
            ]

            plt.figure(figsize=(18, 10))

            # Loop through each service column
            for idx, feature in enumerate(service_features, 1):
                plt.subplot(2, 3, idx)

                # Calculate percentage distribution
                percent_data = telecom_df[feature].value_counts(normalize=True) * 100

                ax = percent_data.plot(
                    kind="bar",
                    color=["#4CAF50", "#FF9800", "#F44336"]  # green, orange, red
                )

                plt.title(f"{feature} Usage (%)")
                plt.xlabel("")
                plt.ylabel("Percentage")

                # Add percentage labels
                for container in ax.containers:
                    ax.bar_label(container, fmt="%.1f%%")

            plt.tight_layout()
            plt.savefig("service_columns_usage.png")
            plt.show()

            # 15 Service Usage by Gender (%)

            # Service-related columns
            service_features = [
                "OnlineSecurity",
                "OnlineBackup",
                "DeviceProtection",
                "TechSupport",
                "StreamingTV",
                "StreamingMovies"
            ]

            plt.figure(figsize=(18, 10))

            for idx, feature in enumerate(service_features, 1):
                plt.subplot(2, 3, idx)

                gender_pct = pd.crosstab(
                    telecom_df["gender"],
                    telecom_df[feature],
                    normalize="index"
                ) * 100

                axis = gender_pct.plot(
                    kind="bar",
                    ax=plt.gca(),
                    color=["#2196F3", "#FF9800", "#9C27B0"]  # blue, orange, purple
                )

                plt.title(f"{feature} Usage by Gender (%)")
                plt.xlabel("Gender")
                plt.ylabel("Percentage")

                for container in axis.containers:
                    axis.bar_label(container, fmt="%.1f%%")

            plt.tight_layout()
            plt.savefig("service_columns_by_gender.png")
            plt.show()

            # 16 Contract Distribution

            # Loop through each SIM operator
            for sim_name in telecom_df["SIM"].unique():

                sim_data = telecom_df[telecom_df["SIM"] == sim_name]

                fig, axis = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
                bar_width = 0.35

                for idx, churn_status in enumerate(["No", "Yes"]):

                    churn_df = sim_data[sim_data["Churn"] == churn_status]

                    contract_gender = (
                        churn_df
                        .groupby(["Contract", "gender"])
                        .size()
                        .unstack(fill_value=0)
                    )

                    x_pos = np.arange(len(contract_gender))

                    axis[idx].bar(
                        x_pos - bar_width / 2,
                        contract_gender["Male"],
                        bar_width,
                        label="Male",
                        color="#2196F3"
                    )
                    axis[idx].bar(
                        x_pos + bar_width / 2,
                        contract_gender["Female"],
                        bar_width,
                        label="Female",
                        color="#E91E63"
                    )

                    # Add count labels
                    for j in range(len(contract_gender)):
                        axis[idx].text(
                            x_pos[j] - bar_width / 2,
                            contract_gender["Male"].iloc[j],
                            contract_gender["Male"].iloc[j],
                            ha="center",
                            va="bottom",
                            fontsize=8
                        )
                        axis[idx].text(
                            x_pos[j] + bar_width / 2,
                            contract_gender["Female"].iloc[j],
                            contract_gender["Female"].iloc[j],
                            ha="center",
                            va="bottom",
                            fontsize=8
                        )

                    axis[idx].set_xticks(x_pos)
                    axis[idx].set_xticklabels(contract_gender.index, rotation=15)
                    axis[idx].set_title(f"Churn = {churn_status}")
                    axis[idx].set_xlabel("Contract")
                    axis[idx].set_ylabel("Number of Customers")
                    axis[idx].legend(title="Gender")

                fig.suptitle(f"Contract vs Gender by Churn (SIM = {sim_name})")
                plt.tight_layout()
                plt.savefig(f"contract_gender_churn_{sim_name}.png")
                plt.show()

            # 17 Contract Distribution by Gender, Senior Citizen & SIM

            # Create combined demographic column
            telecom_df["Gender_Senior_SIM"] = (
                    telecom_df["gender"]
                    + "-"
                    + telecom_df["SeniorCitizen"].map({0: "Non-Senior", 1: "Senior"})
                    + "-"
                    + telecom_df["SIM"]
            )

            # Percentage distribution of Contract
            contract_demo_percent = (
                    pd.crosstab(
                        telecom_df["Gender_Senior_SIM"],
                        telecom_df["Contract"],
                        normalize="index"
                    ) * 100
            )

            plt.figure(figsize=(15, 6))
            axis = contract_demo_percent.plot(
                kind="bar",
                ax=plt.gca(),
                color=["#4CAF50", "#FF9800", "#9C27B0"]
            )

            plt.title("Contract Distribution by Gender, Senior Citizen & SIM")
            plt.xlabel("Gender - Senior - SIM")
            plt.ylabel("Percentage")

            for container in axis.containers:
                axis.bar_label(container, fmt="%.1f%%")

            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.savefig("contract_by_gender_senior_sim.png")
            plt.show()

            # 18 Paperless Billing by Gender, SIM Operator & Churn

            # Group by SIM, Gender, Churn and PaperlessBilling
            billing_grouped = (
                telecom_df
                .groupby(["SIM", "gender", "Churn", "PaperlessBilling"])
                .size()
                .unstack(fill_value=0)
                .reset_index()
            )

            # Create x-axis labels
            x_labels = [
                f"{row['SIM']}, {row['gender']}, {row['Churn']}"
                for _, row in billing_grouped.iterrows()
            ]

            x_pos = np.arange(len(x_labels))
            bar_width = 0.35

            # Billing counts
            paper_bill = billing_grouped["No"]
            paperless_bill = billing_grouped["Yes"]
            total_vals = paper_bill + paperless_bill

            # Plot
            plt.figure(figsize=(16, 6))
            plt.bar(
                x_pos - bar_width / 2,
                paper_bill,
                bar_width,
                label="Paper Billing",
                color="#03A9F4"
            )
            plt.bar(
                x_pos + bar_width / 2,
                paperless_bill,
                bar_width,
                label="Paperless Billing",
                color="#E91E63"
            )

            # Add percentage labels inside bars
            for i in range(len(x_pos)):
                plt.text(
                    x_pos[i] - bar_width / 2,
                    paper_bill[i] / 2,
                    f"{(paper_bill[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

                plt.text(
                    x_pos[i] + bar_width / 2,
                    paperless_bill[i] / 2,
                    f"{(paperless_bill[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

            plt.xticks(x_pos, x_labels, rotation=30)
            plt.xlabel("SIM Operator / Gender / Churn")
            plt.ylabel("Customer Count")
            plt.title("Paperless Billing by Gender, SIM Operator & Churn")
            plt.legend()
            plt.tight_layout()

            plt.savefig("paperless_billing_by_sim_gender_churn.png")
            plt.show()

            # 19 Payment Method by Gender & Churn

            # Group by Payment Method, Gender and Churn
            payment_grouped = (
                telecom_df
                .groupby(["PaymentMethod", "gender", "Churn"])
                .size()
                .unstack(fill_value=0)
                .reset_index()
            )

            # Create x-axis labels
            x_labels = [
                f"{row['PaymentMethod']}, {row['gender']}"
                for _, row in payment_grouped.iterrows()
            ]

            x_pos = np.arange(len(x_labels))
            bar_width = 0.35

            # Churn counts
            no_churn_vals = payment_grouped["No"]
            yes_churn_vals = payment_grouped["Yes"]
            total_vals = no_churn_vals + yes_churn_vals

            # Plot
            plt.figure(figsize=(16, 6))
            plt.bar(
                x_pos - bar_width / 2,
                no_churn_vals,
                bar_width,
                label="No Churn",
                color="#4CAF50"
            )
            plt.bar(
                x_pos + bar_width / 2,
                yes_churn_vals,
                bar_width,
                label="Churn",
                color="#FF5722"
            )

            # Add percentage labels inside bars
            for i in range(len(x_pos)):
                plt.text(
                    x_pos[i] - bar_width / 2,
                    no_churn_vals[i] / 2,
                    f"{(no_churn_vals[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

                plt.text(
                    x_pos[i] + bar_width / 2,
                    yes_churn_vals[i] / 2,
                    f"{(yes_churn_vals[i] / total_vals[i]) * 100:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=9
                )

            plt.xticks(x_pos, x_labels, rotation=30)
            plt.xlabel("Payment Method / Gender")
            plt.ylabel("Customer Count")
            plt.title("Payment Method by Gender & Churn")
            plt.legend()
            plt.tight_layout()

            plt.savefig("payment_method_by_gender_churn.png")
            plt.show()

            # 20 Quarterly Tenure Analysis with SIM

            # Quarterly tenure analysis for each SIM operator
            for sim_name in telecom_df["SIM"].unique():

                sim_data = telecom_df[telecom_df["SIM"] == sim_name]

                fig, axis = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
                bar_width = 0.45

                for idx, churn_status in enumerate(["No", "Yes"]):

                    churn_data = sim_data[sim_data["Churn"] == churn_status]

                    # Group tenure into quarters and split by gender
                    tenure_quarter = (
                        churn_data
                        .groupby([((churn_data["tenure"] - 1) // 3 + 1), "gender"])
                        .size()
                        .unstack(fill_value=0)
                    )

                    x_pos = np.arange(len(tenure_quarter))

                    axis[idx].bar(
                        x_pos - bar_width / 2,
                        tenure_quarter["Male"],
                        bar_width,
                        label="Male",
                        color="#2196F3"
                    )
                    axis[idx].bar(
                        x_pos + bar_width / 2,
                        tenure_quarter["Female"],
                        bar_width,
                        label="Female",
                        color="#E91E63"
                    )

                    # Add count labels
                    for j in range(len(tenure_quarter)):
                        axis[idx].text(
                            x_pos[j] - bar_width / 2,
                            tenure_quarter["Male"].iloc[j],
                            tenure_quarter["Male"].iloc[j],
                            ha="center",
                            va="bottom",
                            fontsize=8
                        )
                        axis[idx].text(
                            x_pos[j] + bar_width / 2,
                            tenure_quarter["Female"].iloc[j],
                            tenure_quarter["Female"].iloc[j],
                            ha="center",
                            va="bottom",
                            fontsize=8
                        )

                    axis[idx].set_xticks(x_pos)
                    axis[idx].set_xticklabels([int(q) for q in tenure_quarter.index])
                    axis[idx].set_title(f"Churn = {churn_status}")
                    axis[idx].set_xlabel("Tenure (Quarter Number)")
                    axis[idx].set_ylabel("Customers")
                    axis[idx].legend(title="Gender")

                fig.suptitle(f"Quarterly Tenure Analysis | SIM = {sim_name}")
                plt.tight_layout()
                plt.savefig(f"quarterly_tenure_sim_{sim_name}.png")
                plt.show()

            # 21 Monthly Charges vs SIM Operator by Churn

            # Calculate average monthly charges by SIM and Churn
            avg_monthly_cost = (
                telecom_df
                .groupby(["SIM", "Churn"])["MonthlyCharges"]
                .mean()
                .unstack()
            )

            x_pos = np.arange(len(avg_monthly_cost.index))
            bar_width = 0.35

            no_churn_avg = avg_monthly_cost["No"]
            yes_churn_avg = avg_monthly_cost["Yes"]

            # Plot
            plt.figure(figsize=(10, 6))
            plt.bar(
                x_pos - bar_width / 2,
                no_churn_avg,
                bar_width,
                label="No Churn",
                color="#4CAF50"
            )
            plt.bar(
                x_pos + bar_width / 2,
                yes_churn_avg,
                bar_width,
                label="Churn",
                color="#FF7043"
            )

            # Add percentage labels above bars
            for i in range(len(x_pos)):
                total_val = no_churn_avg[i] + yes_churn_avg[i]

                no_pct = (no_churn_avg[i] / total_val) * 100
                yes_pct = (yes_churn_avg[i] / total_val) * 100

                plt.text(
                    x_pos[i] - bar_width / 2,
                    no_churn_avg[i],
                    f"{no_pct:.1f}%",
                    ha="center",
                    va="bottom",
                    fontsize=9
                )

                plt.text(
                    x_pos[i] + bar_width / 2,
                    yes_churn_avg[i],
                    f"{yes_pct:.1f}%",
                    ha="center",
                    va="bottom",
                    fontsize=9
                )

            plt.xticks(x_pos, avg_monthly_cost.index)
            plt.xlabel("SIM Operator")
            plt.ylabel("Average Monthly Charges")
            plt.title("Average Monthly Charges by SIM Operator & Churn (with %)")
            plt.legend()
            plt.tight_layout()

            plt.savefig("avg_monthly_charges_by_sim_churn.png")
            plt.show()

            # 22 Region vs Gender with Senior Citizen

            # Split data into Non-Senior and Senior citizens
            non_senior_data = telecom_df[telecom_df["SeniorCitizen"] == 0]
            senior_data = telecom_df[telecom_df["SeniorCitizen"] == 1]

            # Group by Region and Gender
            region_gender_non = (
                non_senior_data
                .groupby(["Region", "gender"])
                .size()
                .unstack(fill_value=0)
            )

            region_gender_sen = (
                senior_data
                .groupby(["Region", "gender"])
                .size()
                .unstack(fill_value=0)
            )

            regions = region_gender_non.index
            x_pos = np.arange(len(regions))
            bar_width = 0.35

            # Create subplots
            fig, axis = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

            # Non-Senior plot
            axis[0].bar(
                x_pos - bar_width / 2,
                region_gender_non["Male"],
                bar_width,
                label="Male",
                color="#2196F3"
            )
            axis[0].bar(
                x_pos + bar_width / 2,
                region_gender_non["Female"],
                bar_width,
                label="Female",
                color="#E91E63"
            )
            axis[0].set_title("Region vs Gender (Non-Senior Citizens)")
            axis[0].set_xlabel("Region")
            axis[0].set_ylabel("Customer Count")
            axis[0].set_xticks(x_pos)
            axis[0].set_xticklabels(regions, rotation=20)
            axis[0].legend()

            # Senior plot
            axis[1].bar(
                x_pos - bar_width / 2,
                region_gender_sen["Male"],
                bar_width,
                label="Male",
                color="#2196F3"
            )
            axis[1].bar(
                x_pos + bar_width / 2,
                region_gender_sen["Female"],
                bar_width,
                label="Female",
                color="#E91E63"
            )
            axis[1].set_title("Region vs Gender (Senior Citizens)")
            axis[1].set_xlabel("Region")
            axis[1].set_xticks(x_pos)
            axis[1].set_xticklabels(regions, rotation=20)
            axis[1].legend()

            plt.suptitle("Region vs Gender with Senior Citizen")
            plt.tight_layout()

            plt.savefig("region_gender_seniorcitizen.png")
            plt.show()

            logger.info("Complete EDA executed successfully")

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logger.error(
                f"Error in line {exc_tb.tb_lineno}: {exc_obj}"
            )


# ================= MAIN EXECUTION =================
if __name__ == "__main__":

    obj = CUSTOMER_CHURN_EDA(
        "D:\\Project 2\\Customer_Churn_Updated.csv"
    )

    obj.run_complete_eda()
