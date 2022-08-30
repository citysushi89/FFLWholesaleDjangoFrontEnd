import csv
from PPSapp.models import Data

# Change path before deployment
# TODO: remove reading from CSV in production, just go straight from the dict/list to writing to db
with open(rf"C:/Users/Owen/Documents/Programming/Projects/PPsW_Django\Wholesalers/grice_wholesale_data.csv") as file:
    # get number of rows
    # rows = sum(1 for line in file)
    # reader = csv.reader(file)
    # # Skips header
    # for i in range(1, rows):
    #     _, created = Teacher.objects.get_or_create(
    #                     first_name=row[0],
    #                     last_name=row[1],
    #                     middle_name=row[2],
    #                     )

    reader = csv.reader(file) 
    for line in reader:
        print(line)  

    