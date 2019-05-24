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

    def passRate(self,data,year,region,sex = 'all'):
        """
        Function calculates pass rate in given year and region.
        """
        passed = 0
        temp_attending = 0
        for i in range(len(data.year)):
            if str(region) in data.region[i] and str(year) in data.year[i] and (sex in data.sex[i] or sex == 'all'):
                if 'przystąpiło' in data.attended_or_passed[i]:
                    temp_attending = temp_attending + int(data.number[i])
                elif 'zdało' in data.attended_or_passed[i]:
                    passed = passed + int(data.number[i])/int(temp_attending)*100
                            
        return passed
        
    def passRateInRegion(self, data, region, sex ='all'):
        """
        Function calculates and returns dictionary with years and pass rate in corresponding year in percents for given region.
        If parameter sex is not given, function runs for all.
        """
        passed_in_years = {}
        years = set(data.year[1:])
        year= int(min(years))

        while year <= int(max(years)):
            passed_in_years[year] = data.passRate(data,year,region,sex)
            year += 1

        return passed_in_years


    def passRateInYears(self, data, year, sex ='all'):
        """
        Function calculates and returns dictionary with regions and pass rate in corresponding regions in percents for given year.
        If parameter sex is not given, function runs for all.
        """
        passed_in_region = {}
        regions = data.listOfRegions(data)
        for region in regions:
            passed_in_region[region] = data.passRate(data,year,region,sex)
        return passed_in_region

    def listOfRegions(self, data):
        regions = set(data.region)
        regions.remove("Terytorium")
        regions.remove("Polska")
        regions = list(regions)
        return regions

    def bestPassRate(self,data,year,sex = 'all'):
        regions = data.listOfRegions(data)
        regions_with_rates = {}
        max_passed = 0
        prev_max_passed = 0
        best_region = ''

        for region in regions:
            regions_with_rates[region] = data.passRateInRegion(data,region,sex)
            max_passed = max((d[year]) for d in regions_with_rates.values())
            if (prev_max_passed<max_passed):
                prev_max_passed = max_passed
                best_region = region

        max_passed = max((d[year]) for d in regions_with_rates.values())
        return best_region , max_passed
            

    def regionPassRegression(self, parameter_list):
        ## wykrycie województw, które zanotowały regresję (mniejszy współczynnik zdawalności w kolejnym roku), jeżeli takowe znajdują się w zbiorze
        pass
    
    def compareRegions(self, data, region_1, region_2):
        #porównanie dwóch województw - dla podanych dwóch województw wypisanie, które z województw miało lepszą zdawalność w każdym dostępnym roku
        pass

data = Graduate('','','','','')
data.readData('baza_maturzystow.csv',data)
year = 2012
voivodeship = 'Pomorskie'
sex = 'kobiety'
years = data.passRateInYears(data,'2012',sex)
#print(f'Średnia uczestnicząych w maturze w latach {min(data.year)}-{year} dla województwa'
#f'Pomorskiego wyniosła : {data.averageAttendedInYears(data,year,voivodeship,sex): .1f}')
print(f'Zdawalność w 2012 w województwach równa się {years} ')
#ms= 0 
#ms = data.bestPassRate(data,'2011',sex)
#print(ms)
print(f'Pomorskie {data.passRate(data,"2010","Pomorskie")}')
