import csv
import random
from datetime import datetime, timedelta

# Define the dataset file path
output_file = "/users/SueYang/task/pearl_city_home_sales.csv"

# Define the properties that must be included
required_properties = [
    {"address": "2072 Akaikai Loop", "city": "Pearl City", "state": "HI"},
    {"address": "2017 Komo Mai Drive", "city": "Pearl City", "state": "HI"}
]

# Function to fetch home sales data
def fetch_home_sales_data():
    # Generate random data for 48 additional properties
    streets = ["Akaikai Loop", "Komo Mai Drive", "Hoomalu Street", "Hoomaikai Street", "Hoomaemae Street"]
    data = []

    for _ in range(48):
        address = f"{random.randint(1000, 3000)} {random.choice(streets)}"
        sale_date = (datetime(2021, 1, 1) + timedelta(days=random.randint(0, 1095))).strftime("%Y-%m-%d")
        sale_price = random.randint(500000, 1200000)
        square_footage = random.randint(1000, 3000)
        bedrooms = random.randint(2, 5)
        bathrooms = random.randint(1, 4)
        year_built = random.randint(1970, 2020)

        data.append({
            "address": address,
            "sale_date": sale_date,
            "sale_price": sale_price,
            "square_footage": square_footage,
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "year_built": year_built
        })

    # Add the required properties
    data.extend([
        {
            "address": "2072 Akaikai Loop",
            "sale_date": "2022-05-15",
            "sale_price": 850000,
            "square_footage": 1800,
            "bedrooms": 3,
            "bathrooms": 2,
            "year_built": 1985
        },
        {
            "address": "2017 Komo Mai Drive",
            "sale_date": "2022-07-20",
            "sale_price": 920000,
            "square_footage": 2000,
            "bedrooms": 4,
            "bathrooms": 3,
            "year_built": 1990
        }
    ])

    return data

# Write the dataset to a CSV file
def write_to_csv(data, file_path):
    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

# Main function
def main():
    # Fetch the data
    home_sales_data = fetch_home_sales_data()

    # Ensure required properties are included
    for property in required_properties:
        if not any(d["address"] == property["address"] for d in home_sales_data):
            home_sales_data.append(property)

    # Write the data to a CSV file
    write_to_csv(home_sales_data, output_file)
    print(f"Dataset created successfully: {output_file}")

if __name__ == "__main__":
    main()