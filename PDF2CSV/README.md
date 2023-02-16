# PDF to CSV Converter

A Python script that converts PDF files to CSV format using the Tabula library.

## Prerequisites

- Python 3
- Tabula library
- Pandas library

## Installation

1. Clone this repository:

- git clone https://github.com/DreaUltimate/MyMiniProjects/tree/main/PDF2CSV

2. Install the Tabula and Pandas libraries:

- pip install tabula pandas

## Usage

1. Put your PDF files in the `pdf` directory.
2. Run the script with the following command:

- python convert.py

3. The CSV files will be generated in the `csv` directory.

### Options

- `-f` or `--file`: specify a single file to convert (e.g. `--file example.pdf`).
- `-p` or `--pages`: specify which pages to convert (e.g. `--pages 1-3,5`).
- `-s` or `--stream`: stream output to stdout instead of writing to file.
- `-d` or `--debug`: enable debug mode.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m "Add some feature"`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.


## Contact

If you have any questions or comments, please contact me at montenegrodiussantos1@gmail.com
