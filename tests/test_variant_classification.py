import unittest
from classification import *



class TestInterval(unittest.TestCase):

    def configure_logging(self, log_file):
        """
        Configures logging to a specified file. This is used to set up separate log files for each test case.

        Parameters:
        log_file (str): The file path for the log file.
        """
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        return log_file
    
    def setUp(self):
        """
        Set up that runs before each test case. 
        Initializes common variables used in the tests.
        """
        self.test_data_path = 'tests/data'
        self.chunk_size = 10**6

    def test_invalid_empty_DNA(self):
        """
        This function tests the scenario where there is at least one empty original sequence in the input file.
        Verifies that the program handles empty original sequences correctly.
        """
        # Configure logging specific to this test.
        log_path = self.configure_logging(f'{self.test_data_path}/test1.log')

        # Define file paths for the test input, expected output, and actual output.
        file_path = f'{self.test_data_path}/test1.csv'
        truth_path = f'{self.test_data_path}/truth1.txt'
        output_path = f'{self.test_data_path}/test1.txt'
        
        # Run the main function with the test files.
        main(file_path, output_path, self.chunk_size, log_path)
        
        # Compare the actual output with the expected output.
        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))
        
        # Shutdown logging after the test is complete.
        logging.shutdown()

    def test_invalid_input_DNA(self):
        """
        This function is testing a condition where there  is at least an invalid original/result sequence in our input file.
        Verifies that the program handles invalid original sequences correctly.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test2.log')
        file_path = f'{self.test_data_path}/test2.csv'
        truth_path = f'{self.test_data_path}/truth2.txt'
        output_path = f'{self.test_data_path}/test2.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_invalid_edit(self):
        """
        This function is testing a condition where there is at least an invalid edit type in our input file.
        Verifies that the program handles invalid edits correctly.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test3.log')

        file_path = f'{self.test_data_path}/test3.csv'
        truth_path = f'{self.test_data_path}/truth3.txt'
        output_path = f'{self.test_data_path}/test3.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_empty_input_file(self):
        """
        This function is testing a condition where our input file is empty.
        Verifies that the program handles empty input correctly.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test4.log')

        file_path = f'{self.test_data_path}/test4.csv'
        truth_path = f'{self.test_data_path}/truth4.txt'
        output_path = f'{self.test_data_path}/test4.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_inserted_nucleotide_at_the_end_of_sequence(self):
        """
        This function is testing a condition where there is at least an edit which the nucleotide is inserted at the end of sequence.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test5.log')

        file_path = f'{self.test_data_path}/test5.csv'
        truth_path = f'{self.test_data_path}/truth5.txt'
        output_path = f'{self.test_data_path}/test5.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_inserted_nucleotide_at_the_beginning_of_sequence(self):
        """
        This function is testing a condition where there is at least an edit in our input file which the nucleotide is inserted to the front of sequence.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test6.log')

        file_path = f'{self.test_data_path}/test6.csv'
        truth_path = f'{self.test_data_path}/truth6.txt'
        output_path = f'{self.test_data_path}/test6.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_deleted_nucleotide_at_the_beginning_of_sequence(self):
        """
        This function is testing a condition where there is at least an edit in our input file which the nucleotide is deleted from the front of sequence.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test7.log')

        file_path = f'{self.test_data_path}/test7.csv'
        truth_path = f'{self.test_data_path}/truth7.txt'
        output_path = f'{self.test_data_path}/test7.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def test_deleted_nucleotide_at_the_end_of_sequence(self):
        """
        This function is testing a condition where there is at least an edit in our input file which the nucleotide is deleted from the end of sequence.
        """

        log_path = self.configure_logging(f'{self.test_data_path}/test8.log')

        file_path = f'{self.test_data_path}/test8.csv'
        truth_path = f'{self.test_data_path}/truth8.txt'
        output_path = f'{self.test_data_path}/test8.txt'

        main(file_path, output_path, self.chunk_size, log_path)

        with open(truth_path) as truth, open(output_path) as output:
            self.assertListEqual(list(truth), list(output))

        logging.shutdown()

    def tearDown(self):
        """
        Tear down method that runs after each test case.
        Can be used to clean up resources or files used during tests.
        """
        # Optionally, uncomment these lines to remove test files after each test.
        #for f in glob.glob(f'{self.test_data_path}/test*.txt'):
        #   os.remove(f)
        #for f in glob.glob(f'{self.test_data_path}/test*.log'):
        #  os.remove(f)
        pass