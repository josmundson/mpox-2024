
import csv
import sys

def modify_and_write(input_file, output_file):
    with open(input_file, 'r', newline='') as f_in:
        reader = csv.reader(f_in, delimiter='\t')
        with open(output_file, 'w', newline='') as f_out:
            writer = csv.writer(f_out, delimiter='\t')
            for row in reader:
                modified_row = []
                for item in row:
                    modified_row.append(str(item))
                modified_institution = ''.join(row[14].split())  # Remove spaces from the 15th column
                if "losangeles" in modified_institution.lower():  # Case insensitive search
                    modified_row[6] = "Los Angeles"
                writer.writerow(modified_row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    modify_and_write(input_file, output_file)




