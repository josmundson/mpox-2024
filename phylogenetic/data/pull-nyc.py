
import csv
import sys

def search_and_write(input_file, output_file):
    with open(input_file, 'r', newline='') as f_in:
        reader = csv.reader(f_in, delimiter='\t')
        next(reader)  # Skip header row
        with open(output_file, 'w') as f_out:
            for row in reader:
                accession = row[0]
                institution = row[14]  # Assuming column index starts from 0
                if "nyc" in institution.lower():  # Case insensitive search
                    f_out.write(accession + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python py.ny input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    search_and_write(input_file, output_file)



