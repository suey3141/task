import pandas as pd
import numpy as np
from datetime import datetime


# Define the dataset file path
dataset_file = "/users/SueYang/task/pearl_city_home_sales.csv"
result_file = "analysis_result.txt"

def load_dataset(file_path):
    """Load the dataset into a pandas DataFrame and clean the data."""
    df = pd.read_csv(file_path)

    # Ensure sale_price is numeric, and drop rows with invalid sale_price
    df["sale_price"] = pd.to_numeric(df["sale_price"], errors="coerce")
    df = df.dropna(subset=["sale_price"])  # Drop rows where sale_price is NaN

    return df

def estimate_typical_home_value(df):
    """Estimate the current value of a typical home based on average sale price."""
    return df["sale_price"].mean()

def analyze_seasonal_trends(df):
    """Analyze seasonal trends to determine the best time to sell."""
    df["sale_month"] = pd.to_datetime(df["sale_date"]).dt.month
    monthly_sales = df.groupby("sale_month")["sale_price"].mean()
    best_month = monthly_sales.idxmax()
    return best_month, monthly_sales[best_month]

def suggest_home_improvements(df):
    """Suggest home improvements based on features that correlate with higher sale prices."""
    # Ensure only numeric columns are used for correlation
    numeric_df = df.select_dtypes(include=[np.number])

    # Check if 'sale_price' exists in the numeric DataFrame
    if "sale_price" not in numeric_df.columns:
        raise ValueError("The 'sale_price' column is missing or not numeric.")

    # Compute correlations
    correlations = numeric_df.corr()

    # Sort correlations with 'sale_price' and drop 'sale_price' itself
    improvement_suggestions = correlations["sale_price"].sort_values(ascending=False).drop("sale_price", errors="ignore")

    # Return the top 3 suggestions
    return improvement_suggestions.head(3)

def save_results_to_file(typical_home_value, best_month, best_month_avg_price, improvements, result_file):
    """Save the analysis results to a text file."""
    with open(result_file, mode="w") as file:
        file.write(f"Estimated value of a typical home: ${typical_home_value:,.2f}\n")
        file.write(f"Best time to sell: Month {best_month} (Average sale price: ${best_month_avg_price:,.2f})\n")
        file.write("Top 3 home improvements for better ROI:\n")
        for feature, correlation in improvements.items():
            file.write(f"- {feature}: Correlation with sale price = {correlation:.2f}\n")

def main():
    # Load the dataset
    df = load_dataset(dataset_file)

    # Estimate the current value of a typical home
    typical_home_value = estimate_typical_home_value(df)

    # Analyze seasonal trends
    best_month, best_month_avg_price = analyze_seasonal_trends(df)

    # Suggest home improvements
    improvements = suggest_home_improvements(df)

    # Save the results to a file
    save_results_to_file(typical_home_value, best_month, best_month_avg_price, improvements, result_file)
    print(f"Analysis results saved to {result_file}")

if __name__ == "__main__":
    main()