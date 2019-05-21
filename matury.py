import csv

class Graduate:
    def __init__(self, region, attended_or_passed, sex, year, number):
        self.region = region = []
        self.attended_or_passed = attended_or_passed = []
        self.sex = sex = []
        self.year = year = []
        self.number = number = []

    def averageAttendedInYears(self, data, year, region):
        """
        Function calculate average number of students that attended exam in given voivodeship in years from lowest year to given year
        
        Parameters
        ----------
        data : Graduate
            Object of the type Graduate which contains a list for each parameter of database
        year : int
            Year up to which to calculate the average
        region : string
            Voivodeship in which user wants to calculate the average
        Returns
        ----------
        int
            Average number of stutents that attended exam in given voivodeship in years from lowest year to given year
        """
        average = 0
        for i in range(len(data.year)):
            if 'przystąpiło' in data.attended_or_passed[i] and int(data.year[i])<=year:
                if region in data.region[i]:
                    average += int(data.number[i])
        i+=1
        return average/(1+year-int(min(data.year)))

    def readData(self, filename, new_data):
        """
        Function reads data from .csv file and copies it into object of type Graduate

        Parameters
        ----------
        filename : string
            Name of the file to be read which filetype .csv
        new_data : Graduate
            Object of type Graduate which contains a list for each parameter of database

        """
        with open(filename) as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=';')
            for row in csv_reader:
                new_data.region.append(row[0])
                new_data.attended_or_passed.append(row[1])
                new_data.sex.append(row[2])
                new_data.year.append(row[3])
                new_data.number.append(row[4])


data = Graduate('','','','','')
data.readData('baza_maturzystow.csv',data)
year = 2012
voivodeship = 'Pomorskie'
print(f'Średnia uczestnicząych w maturze w latach {min(data.year)}-{year}dla województwa'
f'Pomorskiego wyniosła : {data.averageAttendedInYears(data,year,voivodeship): .1f}')
