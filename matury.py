import csv

class Graduate:
    def __init__(self, region, attended_or_passed, sex, year, number):
        self.region = region = []
        self.attended_or_passed = attended_or_passed = []
        self.sex = sex = []
        self.year = year = []
        self.number = number = []

    def average_graduates(self, parameter_list):
        raise NotImplementedError   
    
    def read_data(self, filename, new_data):
        line_count = 0
        with open(filename) as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=';')
            for row in csv_reader:
                new_data.region.append(row[0])
                new_data.attended_or_passed.append(row[1])
                new_data.sex.append(row[2])
                new_data.year.append(row[3])
                new_data.number.append(row[4])
                line_count += 1

new_data = Graduate('','','','','')
new_data.read_data('baza_maturzystow.csv',new_data)