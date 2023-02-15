import tabula
import logging

# Set up logging configuration
logging.basicConfig(filename='tabula.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

def convert_pdf_to_csv(input_file, output_file):
    try:
        # Convert PDF to CSV using tabula
        tabula.convert_into(input_file, output_file, output_format="csv", pages="all")
    except FileNotFoundError:
        # Handle file not found errors
        logging.error(f"Error: File not found - {input_file}")
        print(f"Error: File not found - {input_file}")
    except Exception as e:
        # Handle other errors
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
    else:
        # Handle successful conversion
        logging.info(f"{input_file} successfully converted to {output_file}")
        print(f"{input_file} successfully converted to {output_file}")

# Call the function for each file you need to convert
convert_pdf_to_csv("samplecsv1.pdf", "samplecsv1.csv")
convert_pdf_to_csv("samplecsv2.pdf", "samplecsv2.csv")
convert_pdf_to_csv("samplecsv3.pdf", "samplecsv3.csv")
