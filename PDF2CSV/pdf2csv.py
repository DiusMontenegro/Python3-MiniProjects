import tabula
import logging
from multiprocessing import Pool

# Set up logging configuration
logging.basicConfig(filename='tabula.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

def convert_pdf_to_csv(file):
    input_file = file + ".pdf"
    output_file = file + ".csv"
    try:
        # Convert PDF to CSV using tabula
        tabula.convert_into(input_file, output_file, output_format="csv", pages="all", stream=True)
    except Exception as e:
        # Handle errors and log them
        logging.error(f"Error: {e} - {input_file}")
        print(f"Error: {e} - {input_file}")
    else:
        # Handle successful conversion and log it
        logging.info(f"{input_file} successfully converted to {output_file}")
        print(f"{input_file} successfully converted to {output_file}")

# List of PDF files to convert
pdf_files = ["samplecsv1", "samplecsv2", "samplecsv3"]

# Use multiprocessing to convert PDF files in parallel
with Pool() as p:
    p.map(convert_pdf_to_csv, pdf_files)

