import json
import os


class FileHandler:

    def __init__(self, filename):
        self.filename = filename

    def load_students(self):
        try:
            if not os.path.exists(self.filename):
                return []

            with open(self.filename, "r") as file:
                data = json.load(file)

            return data

        except json.JSONDecodeError:
            print("Error: Student data file is corrupted.")
            return []

        except FileNotFoundError:
            print("Error: Student data file not found.")
            return []

        except PermissionError:
            print("Error: Permission denied while reading the file.")
            return []

        except Exception as error:
            print(f"Unexpected error: {error}")
            return []

    def save_students(self, students):
        try:
            with open(self.filename, "w") as file:
                json.dump(students, file, indent=4)

        except PermissionError:
            print("Error: Permission denied while writing to the file.")

        except Exception as error:
            print(f"Unexpected error while saving data: {error}")