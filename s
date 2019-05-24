



                passed_in_years = {}
        temp_attending = 0
        years = data.year[1:]
        years = range(int(min(years)),int(max(years)))
        temp_year = 0
        for i in range(len(data.region)):
            if region in data.region[i] and (sex in data.sex[i] or sex == 'all'):
                if str(years[temp_year]) in data.year[i]:
                    if 'przystąpiło' in data.attended_or_passed[i]:
                        temp_attending = data.number[i]
                    elif 'zdało' in data.attended_or_passed[i]:
                        passed_in_years[data.year[i]] = int(data.number[i])/int(temp_attending)*100
                    temp_year += 1
        return passed_in_years

        """
    def bestPassRate(self, data, year, sex = 'all'):
        ##podanie województwa o najlepszej zdawalności w konkretnym roku 
        regions = set(data.region)
        regions = list(regions)
        stat_regions = {}
        temp_count = 0
        for i in range(len(data.year)):
            if str(year) in data.year[i] and (sex in data.sex[i] or sex == 'all'):
                if regions[temp_count] in data.region[i]:
                    if 'przystąpiło' in data.attended_or_passed[i]:
                        temp_attending = data.number[i]
                    elif 'zdało' in data.attended_or_passed[i]:
                        stat_regions[data.region[i]] = int(data.number[i])/int(temp_attending)*100
                        temp_count+1 
        return stat_regions
""" 