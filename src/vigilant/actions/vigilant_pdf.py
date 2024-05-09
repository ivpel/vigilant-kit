import fitz  # PyMuPDF
import glob
import re
import os
from vigilant.logger import logger as log


class VigilantPDF:

    def find_pdf_file(self, directory, pattern, use_regex=True):
        """
        Find PDF files based on a regex pattern or a simple string within the specified directory.

        Args:
            directory (str): Directory to search in.
            pattern (str): The pattern to match the files. Can be a regex pattern or simple string.
            use_regex (bool): If True, treats pattern as a regex pattern. Otherwise, looks for an exact match.

        Returns:
            list: A list of matching file paths.
        """
        full_pattern = os.path.join(directory, '**/*.pdf')
        files = glob.glob(full_pattern, recursive=True)

        if use_regex:
            # Treat pattern as a regex pattern
            matching_files = [file for file in files if re.search(pattern, os.path.basename(file))]
        else:
            # Treat pattern as a simple string, look for exact matches only
            matching_files = [file for file in files if os.path.basename(file) == pattern]

        log.info(f"PDF files found: {matching_files}")

        if not matching_files:
            if use_regex:
                message = f"No PDF files found matching the regex pattern: {pattern} in directory: {directory}"
            else:
                message = f"No PDF files found with the name: {pattern} in directory: {directory}"
            log.error(message)
            raise AssertionError(message)

        return matching_files

    def assert_strings_are_in_file(self, pattern, strings_list, use_regex=True):
        """Assert that all strings in the list are found in the specified PDF files."""
        pdf_files = self.find_pdf_file('.', pattern, use_regex)

        for pdf in pdf_files:
            self.assert_strings_in_pdf(pdf, strings_list)

    def assert_strings_are_not_in_file(self, pattern, strings_list, use_regex=True):
        """Assert that none of the strings in the list are found in the specified PDF files."""
        pdf_files = self.find_pdf_file('.', pattern, use_regex)

        for pdf in pdf_files:
            self.assert_strings_not_in_pdf(pdf, strings_list)

    def assert_strings_in_pdf(self, pdf_path, strings_list):
        """Check if all strings in the list are present in the specified PDF file."""
        with fitz.open(pdf_path) as doc:
            text = "".join(page.get_text() for page in doc)

        missing_strings = [string for string in strings_list if string not in text]

        log.debug(f"PDF text: {text}")
        log.info(f"Strings that should be in the file: {strings_list}")

        if missing_strings:
            message = f"The following strings were not found in {pdf_path}: {', '.join(missing_strings)}"
            log.error(message)
            raise AssertionError(message)

    def assert_strings_not_in_pdf(self, pdf_path, strings_list):
        """Check if none of the strings in the list are present in the specified PDF file."""
        with fitz.open(pdf_path) as doc:
            text = "".join(page.get_text() for page in doc)

        found_strings = [string for string in strings_list if string in text]

        log.debug(f"PDF text: {text}")
        log.info(f"String should not be in the file: {strings_list}")

        if found_strings:
            message = f"The following strings were found in {pdf_path}, but should not be: {', '.join(found_strings)}"
            log.error(message)
            raise AssertionError(message)

    def delete_pdf_file(self, directory, pattern, use_regex=True):
        """Find and delete all PDF files that match the specified pattern or string."""
        pdf_files = self.find_pdf_file(directory, pattern, use_regex)

        for pdf in pdf_files:
            try:
                os.remove(pdf)
                log.info(f"Deleted PDF file: {pdf}")
            except Exception as e:
                message = f"Error occurred while deleting file {pdf}: {str(e)}"
                log.error(message)
                raise AssertionError(message)

        log.info("All matching PDF files have been deleted.")

    def find_file_and_assert_strings_are_in(self, directory, pattern, strings_list, use_regex=True):
        """Find PDF files and ensure the specified strings are present in each."""
        pdf_files = self.find_pdf_file(directory, pattern, use_regex)

        for pdf in pdf_files:
            self.assert_strings_in_pdf(pdf, strings_list)

    def find_file_and_assert_strings_are_not_in(self, directory, pattern, strings_list, use_regex=True):
        """Find PDF files and ensure the specified strings are not present in any of them."""
        pdf_files = self.find_pdf_file(directory, pattern, use_regex)

        for pdf in pdf_files:
            self.assert_strings_not_in_pdf(pdf, strings_list)
