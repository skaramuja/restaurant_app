import csv


# parent class for importing CSV files
class CSVImporter:
    #  Import data from CSV file and ignoring column header in first line
    def import_data(self, filename):
        with open(filename) as cvs_file:
            csv_reader = csv.reader(cvs_file, delimiter=',')
            line_count = 0
            rows = []
            for row in csv_reader:
                if line_count == 0:
                    print(f'Column names are: {", ".join(row)}.\n')
                    line_count += 1
                    continue
                if str(row[0]) == "":
                    continue
                line_count += 1
                rows.append(row)
            return rows  # Returns a list of Tuples


# Subclass of CSVImports that imports restaurants
class RestaurantImporter(CSVImporter):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.import_data('model/csv_files/restaurants.csv')


# Subclass of CSVImports that imports addresses
class AddressImporter(CSVImporter):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.import_data('model/csv_files/addresses.csv')


# Subclass of CSVImports that imports categories
class CategoryImporter(CSVImporter):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.import_data('model/csv_files/categories.csv')


# Subclass of CSVImports that imports restaurant categories
class RestaurantCategoriesImporter(CSVImporter):
    def __init__(self):
        super().__init__()

    def get_data(self):
        return self.import_data('model/csv_files/restaurantcategories.csv')
