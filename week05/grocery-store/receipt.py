"""
A program for a local grocery store that reads product and request
data from CSV files to generate a customer receipt.

Author: Jerenason Junnot Daniel

Creativity Note for Graders:
1. The receipt output is formatted with aligned columns for better
   readability.
2. Added comprehensive error handling for ValueError and IndexError
   to make the program more robust against malformed CSV data
3. The program provides specific, user-friendly error messages for
   each type of exception.
"""



import csv
from datetime import datetime


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            # Ensure the row has enough columns before accessing the key.
            if len(row_list) > key_column_index:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary


def main():
    PRODUCTS_FILE = "products.csv"
    REQUEST_FILE = "request.csv"
    PRODUCT_KEY_INDEX = 0
    PRODUCT_NAME_INDEX = 1
    PRODUCT_PRICE_INDEX = 2
    REQUEST_QTY_INDEX = 1
    SALES_TAX_RATE = 0.06

    try:
        print("Inkom Emporium")
        print()

        products_dict = read_dictionary(PRODUCTS_FILE, PRODUCT_KEY_INDEX)

        subtotal = 0
        total_items = 0

        print("Requested Items")
        with open(REQUEST_FILE, "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)  

            for row in reader:
                product_key = row[PRODUCT_KEY_INDEX]
                quantity = int(row[REQUEST_QTY_INDEX])

                product_data = products_dict[product_key]

                product_name = product_data[PRODUCT_NAME_INDEX]
                product_price = float(product_data[PRODUCT_PRICE_INDEX])

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity

                subtotal += quantity * product_price

        print()

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")

        sales_tax = subtotal * SALES_TAX_RATE
        print(f"Sales Tax: {sales_tax:.2f}")

        total = subtotal + sales_tax
        print(f"Total: {total:.2f}")
        print()

        print("Thank you for shopping at the Inkom Emporium.")

        current_date_and_time = datetime.now()
        print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}")

    except FileNotFoundError as not_found_err:
        print(f"Error: missing file")
        print(f"[Errno 2] No such file or directory: '{not_found_err.filename}'")

    except PermissionError as perm_err:
        print(f"Error: you do not have permission to read a required file.")
        print(perm_err)

    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file")
        print(f"'{key_err}'")

    except ValueError as val_err:
        print("Error: invalid value in a CSV file.")
        print(
            "Please check that quantities and prices contain only valid numbers."
        )
        print(val_err)

    except IndexError as index_err:
        print("Error: a row in a CSV file has an incorrect number of columns.")
        print(index_err)


if __name__ == "__main__":
    main()