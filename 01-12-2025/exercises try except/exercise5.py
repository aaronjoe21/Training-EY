import csv


def read_csv_file(filename):
    try:
        # Attempt to open and read the CSV file
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            print("\nCSV File Content:\n")
            for row in reader:
                print(row)

    except FileNotFoundError:
        print("Error: The file was not found. Please check the file name and path.")

    except PermissionError:
        print("Error: You do not have permission to read this file.")

    except csv.Error:
        print("Error: The file is not in a valid CSV format.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage:
filename = input("Enter the CSV file name: ")
read_csv_file(filename)