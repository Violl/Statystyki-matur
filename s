



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