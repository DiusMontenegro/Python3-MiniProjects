import tabula

try:
    # Convert PDF to CSV using tabula
    tabula.convert_into("samplecsv.pdf", "samplecsv.csv", output_format="csv", pages="all")
except FileNotFoundError:
    # Handle file not found errors
    print("Error: File not found")
except Exception as e:
    # Handle other errors
    print(f"Error: {e}")
else:
    # Handle successful conversion
    print("PDF successfully converted to CSV")

