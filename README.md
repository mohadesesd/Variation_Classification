# Variant Classification

This exercise is designed to classify DNA sequence variants into three categories: insertions, deletions, and mutations. It takes a CSV file as input, where each line contains an ID, the original DNA sequence, and its variant, and outputs the count of each variant type.

A variant is an 'Insertion' if a single letter is inserted into the original sequence, e.g. 'ATCG' -> 'ATTCG'.

A variant is a 'Deletion' if a single letter is deleted from the original sequence, e.g. 'ATTCG' -> 'ATCG'.

A variant is a 'Mutation' if a single letter changes from one base to another in the original sequence, e.g. 'ATCG' -> 'ATGG'.

Assumptions: 

• Original and variant sequences are always different from each other, i.e. There won't be any situation where there is no variation.

• Only one edit occurs for the original sequence to change to the variant sequence, i.e. There won't be multiple types of edits or multiple edits of the same type.

• Original sequence can not be empty. But variant sequence may be empty if a deletion occurs on a single letter original sequence, e.g. 'T' -> ''.

## Features
- Classify variants into insertions, deletions, and mutations
- Efficiently handles large CSV files using chunk-based processing
- Detailed logging for process monitoring and debugging

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites

    Python 3.x
    Pandas library

You can install Pandas using pip if you don't have it already:
```bash
pip install pandas
```
### Installation

Clone the GitHub repository:

```bash
git clone https://github.com/mohadesesd/Variation_Classification.git
cd Variation_Classification
```
## Parameters

- `input`: Path to the input CSV file. This file should contain the DNA sequences and their variants.
- `output`: Path where the output file will be saved. This file will contain the count of each variant type.
- `log`: Path for the log file to record process information and errors.
- `chunk`: Chunk size for reading the input file. This is useful for processing large files in manageable parts. This parameter is optional and if it's not specified, the default value of 10^6 will be used as the chunk size.

## Running the Code

To run the script, navigate to the project directory and use the following command:

```bash
python classification.py --input path/to/input.csv --output path/to/output.txt --log path/to/logfile.log --chunk 1000
```
or 

```bash
python classification.py -i path/to/input.csv -o path/to/output.txt -l path/to/logfile.log -c 1000
```

Replace path/to/input.csv, path/to/output.txt, path/to/logfile.log, and 1000 with your actual file paths and desired chunk size.

## Running Tests

This project comes with a suite of unit tests to ensure the functionality of the variant classification. To run the tests, use:


```bash
python -m unittest ./tests/test_variant_classification.py
```
you can define your own test by creating a function related to the test in test_variant_classification.py, a csv file, and a truth file that will be compared to the output of the program. 

## Assessment Exercise

Inside this folder, there is a input CSV containing IDs, original and resulted sequences, the result.txt contains the number of each variant type, and the result.log which logs information regarding each row of the input file, warnings and errors.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Contact information
Contact: [Mohadese.sayahiandehkordi@mail.mcgill.ca](Mohadese.sayahiandehkordi@mail.mcgill.ca)
