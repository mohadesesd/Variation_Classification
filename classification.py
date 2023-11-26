import argparse
import pandas as pd
import logging
import os

argparser = argparse.ArgumentParser(description = 'Script for counting the number of each variant type (i.e. Insertions, Deletions, Mutations) from a csv file by knowing the original and result sequence.')
argparser.add_argument('-i', '--input', metavar = 'file', dest = 'in_file_path', required = True, help = 'Input csv file which lists all variants, each line contains ID, original sequence, and variant.')#
argparser.add_argument('-o', '--output', metavar = 'file', dest = 'out_file_path', required = True, help = 'Output file containing the number of each variant type.')
argparser.add_argument('-l', '--log', metavar = 'file', dest = 'log_file_path', required = True, help = 'Log file containing each ID and each variant type also errors and exceptions.')
argparser.add_argument('-c', '--chunk', metavar = 'int', dest = 'chunk_size', required = False, default=1000000, type = int, help = 'Size of the chunk of data that we read in the memory.')


def is_valid_dna(sequence):
    """
    This function check it the input sequence is a valid DNA sequence or not. The definition of valid here is that the sequence only contains 4 type of nucleotides: A, T, C, and G.
    """
    return all(base in ['A', 'T', 'C', 'G'] for base in sequence)

def classify_variant(original, variant):
        """
        This function take a original sequence and a variant sequence as input and classify the type of the variant. 
        A variant is an 'Insertion' if a single letter is inserted into the original sequence, e.g. 'ATCG' -> 'ATTCG'.
        A variant is a 'Deletion' if a single letter is deleted from the original sequence, e.g. 'ATTCG' -> 'ATCG'.
        A variant is a 'Mutation' if a single letter changes from one base to another in the original sequence, e.g. 'ATCG' -> 'ATGG'.
        Assumptions: 
        • Original and variant sequences are always different from each other, i.e. There won't be any situation where there is no variation.
        • Only one edit occurs for the original sequence to change to the variant sequence, i.e. There won't be multiple types of edits or multiple edits of the same type.
        • Original sequence can not be empty. But variant sequence may be empty if a deletion occurs on a single letter original sequence, e.g. 'T' -> ''.
        Parameters:
            original (str): The original DNA sequence.
            variant (str): The variant DNA sequence.
        Returns:
            str: The type of variant ('Insertion', 'Deletion', 'Mutation').
        """
        # Handle special case of single letter deletion.
        if pd.isna(variant) and (len(original) == 1): 
            return 'Deletion'
        
        #Check for the Mutation, equal length and only a single letter difference.
        if len(original) == len(variant): 
            for i in range(len(original)):
                if ((original[i] != variant[i]) and ((original[:i] + original[i+1:]) == (variant[:i] + variant[i+1:]))):
                    return 'Mutation'
        
        #Check for the Deletion, original is one character longer than variant.
        if(len(original) == (len(variant) + 1)):
            for i in range(len(variant)):
                if ((original[i] != variant[i]) and ((original[:i] + original[i+1:]) == variant)):
                            return 'Deletion'
            if(original[:-1] == variant):
                return 'Deletion'
        
        #Check for the Insertion, variant is one character longer than original.
        if(len(variant) == (len(original) + 1)):
            for i in range(len(original)):
                if ((original[i] != variant[i]) and ((variant[:i] + variant[i+1:]) == original)):
                            return 'Insertion'
            if(original == variant[:-1]):
                return 'Insertion'
        
        # Raises an error if none of the above conditions are met.
        raise ValueError('Invalid edit: does not conform to specifications.')

def main(filepath, outputpath, chunksize, logpath):
    """
    This function processes a given CSV file containing DNA sequences and their variants, and outputs the count of each variant type.

    Parameters:
    filepath (str): Path to the input CSV file.
    outputpath (str): Path where the output file will be saved.
    chunksize (int): Number of rows to read at a time from the CSV file.
    logpath (str): Path for the log file to record process information and errors.
    """
    # Check if the input file is empty and log an error if it is.
    if os.path.getsize(filepath) == 0:
        logging.error("No data found in the file.")

    # Configure logging to record information and errors.
    logging.basicConfig(filename = logpath, 
                        level = logging.DEBUG,  format='%(asctime)s - %(levelname)s - %(message)s') 
    
    # Initialize a dictionary to keep count of each variant type.
    variant_counts = {'Insertion': [0], 'Deletion': [0], 'Mutation': [0]}

    try:
        # Read the CSV file in chunks to handle large files efficiently. Chunk size can be specified by user, default value is 10**6.
        for chunk in pd.read_csv(filepath, header = None, names = ['ID', 'Original', 'Variant'], chunksize = chunksize):
            # Iterate through each row in the chunk.
            for index, row in chunk.iterrows():
                try:
                    # Extract original and variant DNA sequences.
                    original = row['Original']
                    variant = row['Variant']

                    # Validate the DNA sequences.
                    if pd.isna(original):
                        raise ValueError(f'Empty input DNA sequence')
                    if not is_valid_dna(original):
                        raise ValueError(f'Invalid DNA sequence: {original}')
                    if not pd.isna(variant):        
                        if not is_valid_dna(variant):
                            raise ValueError(f'Invalid DNA sequence: {variant}')
                        
                    # Classify the variant type.
                    variant_type = classify_variant(original, variant)
                    variant_counts[variant_type][0] += 1

                    # Log the ID and variant type for each processed row.
                    logging.info("ID: %s, Variant Type: %s", row['ID'], variant_type)
                
                except ValueError as e:
                    # Log a warning for rows with invalid data and skip them.
                    logging.warning(f"Skipping row {row['ID']} due to error: {e}")

    except pd.errors.ParserError:
        # Log an error if there is an issue in parsing the CSV file.
        logging.error("Error during parsing the file.")

    except Exception as e:
        # Log any other unexpected errors.
        logging.error(f"An error occurred: {e}")
    
    # Save the counts of each variant type to the output file.
    variant_count_df = pd.DataFrame(variant_counts)
    variant_count_df.to_csv(outputpath, sep = '\t', index = None)

if __name__ == "__main__":
    args = argparser.parse_args()
    # Execute the main function with arguments from the command line.
    main(args.in_file_path, args.out_file_path, args.chunk_size, args.log_file_path)