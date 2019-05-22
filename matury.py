import csv

class Graduate:
    def __init__(self, region, attended_or_passed, sex, year, number):
        self.region = region = []
        self.attended_or_passed = attended_or_passed = []
        self.sex = sex = []
        self.year = year = []
        self.number = number = []

    def readData(self, filename, new_data):
        """
        Function reads data from .csv file and copies it into object of type Graduate
        """
        with open(filename) as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=';')
            for row in csv_reader:
                new_data.region.append(row[0])
                new_data.attended_or_passed.append(row[1])
                new_data.sex.append(row[2])
                new_data.year.append(row[3])
                new_data.number.append(row[4])


    def averageAttendedInYears(self, data, year, region, sex ='all'):
        """
        Function calculates and returns average number of students that attended exam in given voivodeship in years from lowest year to given year.
        If parameter sex is not given, function runs for all.
        """
        average = 0
        for i in range(len(data.year)):
            if 'przystąpiło' in data.attended_or_passed[i] and int(data.year[i])<=year:
                    if region in data.region[i] and (sex in data.sex[i] or sex == 'all'):
                        average += int(data.number[i])
        return average/(1+year-int(min(data.year)))         


    def passRate(self, data, region, sex ='all'):
        """
        Function calculates and returns dictionary with years and pass rate in corresponding year in percents.
        If parameter sex is not given, function runs for all.
        """
        passed_in_years = {}
        temp_attending = 0
        years = data.year[1:]
        first_year= int(min(years))
        for i in range(len(data.region)):
            if region in data.region[i] and (sex in data.sex[i] or sex == 'all'):
                if str(first_year) in data.year[i]:
                    if 'przystąpiło' in data.attended_or_passed[i]:
                        temp_attending = data.number[i]
                    elif 'zdało' in data.attended_or_passed[i]:
                        passed_in_years[data.year[i]] = int(data.number[i])/int(temp_attending)*100
                        first_year += 1
        return passed_in_years

    def bestPassRate(self, parameter_list):
        ##podanie województwa o najlepszej zdawalności w konkretnym roku  
        pass

    def regionPassRegression(self, parameter_list):
        ## wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze
        pass
    
    def compareRegions(self, parameter_list):
        #porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku
        pass
"""
    def getYears(self, data):
        years = data.year.sort()
        years = set(data.year)
        years.remove('Rok')
        return years
        """
            

data = Graduate('','','','','')
data.readData('baza_maturzystow.csv',data)
year = 2012
voivodeship = 'Pomorskie'
sex = 'kobiety'
years = data.passRate(data,voivodeship,sex)
print(f'Średnia uczestnicząych w maturze w latach {min(data.year)}-{year} dla województwa'
f'Pomorskiego wyniosła : {data.averageAttendedInYears(data,year,voivodeship,sex): .1f}')
print(f'Zdawalność w pomorskim w latach równa się {years} ')