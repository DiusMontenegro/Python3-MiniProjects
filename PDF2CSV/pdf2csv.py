import tabula
import logging

# Set up logging configuration
logging.basicConfig(filename='tabula.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s')

try:
    # Convert PDF to CSV using tabula
    tabula.convert_into("samplecsv.pdf", "samplecsv.csv", output_format="csv", pages="all")

except FileNotFoundError:
    # Handle file not found errors
    logging.error("Error: File not found")
    print("Error: File not found")
except Exception as e:
    # Handle other errors
    logging.error(f"Error: {e}")
    print(f"Error: {e}")
else:
    # Handle successful conversion
    logging.info("PDF successfully converted to CSV")
    print("PDF successfully converted to CSV")


