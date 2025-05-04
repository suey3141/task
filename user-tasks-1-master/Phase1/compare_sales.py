import csv

# Define the dataset file path
dataset_file = "pearl_city_home_sales.csv"
result_file = "result.txt"

# Properties to compare
target_properties = ["2072 Akaikai Loop", "2017 Komo Mai Drive"]

def find_highest_sale_in_2022(dataset_file, target_properties):
    highest_sale = None

    # Read the dataset
    with open(dataset_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Check if the property is one of the target properties and sold in 2022
            if row["address"] in target_properties and row["sale_date"].startswith("2022"):
                sale_price = float(row["sale_price"])
                if highest_sale is None or sale_price > highest_sale["sale_price"]:
                    highest_sale = {
                        "address": row["address"],
                        "sale_price": sale_price
                    }

    return highest_sale

def write_result_to_file(result, result_file):
    with open(result_file, mode="w") as file:
        if result:
            file.write(f"The property that sold for the highest price in 2022 is:\n")
            file.write(f"Address: {result['address']}\n")
            file.write(f"Sale Price: ${result['sale_price']:,}\n")
        else:
            file.write("No sales data found for the specified properties in 2022.\n")

def main():
    # Find the highest sale in 2022 for the target properties
    highest_sale = find_highest_sale_in_2022(dataset_file, target_properties)

    # Write the result to the result file
    write_result_to_file(highest_sale, result_file)
    print(f"Result written to {result_file}")

if __name__ == "__main__":
    main()