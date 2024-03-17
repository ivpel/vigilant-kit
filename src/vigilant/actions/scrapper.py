import asyncio
import csv
from vigilant.actions.finder import Finder
from vigilant.actions.waiter import Waiter

class Scrapper:
    def __init__(self, driver):
        self.driver = driver
        self.finder = Finder
        self.waiter = Waiter

    def get_text_from(self, locator_type, locator_value):
        """Extracts text from a web element specified by its locator."""
        element = self.driver.find_element(locator_type, locator_value)
        return element.text

    def get_attribute_from(self, locator_type, locator_value, attribute_name):
        """Extracts the value of a specified attribute from a web element."""
        element = self.driver.find_element(locator_type, locator_value)
        return element.get_attribute(attribute_name)

    def get_table_data(self, table_locator_type, table_locator_value):
        """Extracts all data from a table into a list of dictionaries (one per row)."""
        table = self.driver.find_element(table_locator_type, table_locator_value)
        headers = [th.text for th in table.find_elements_by_tag_name('th')]
        rows = table.find_elements_by_tag_name('tr')
        table_data = []
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            if cells:
                row_data = {headers[i]: cell.text for i, cell in enumerate(cells)}
                table_data.append(row_data)
        return table_data

    def save_data_to_csv(self, data, file_path, fieldnames):
        """Saves a list of dictionaries to a CSV file."""
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

    def save_table_data_to_csv(self, table_locator_type, table_locator_value, file_path):
        """Extracts table data and saves it directly into a CSV file."""
        data = self.get_table_data(table_locator_type, table_locator_value)
        if data:
            fieldnames = data[0].keys()
            self.save_data_to_csv(data, file_path, fieldnames)

    async def monitor_changes(self, locator_type, locator_value, check_interval, change_action):
        """Monitors changes in a web element and executes an action when a change is detected."""
        previous_state = None
        while True:
            try:
                element = self.driver.find_element(By[locator_type], locator_value)
                current_state = element.text
                if previous_state is not None and current_state != previous_state:
                    await change_action(current_state)
                previous_state = current_state
            except Exception as e:
                print(f"Error during monitoring: {e}")
                break  # Or handle the error as needed
            await asyncio.sleep(check_interval)