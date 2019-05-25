# Statystyki-matur
Zadania rekrutacyjne dla Profil Software

Wszystkie funkcje mogą zostać wywołane tylko dla jednej z płci lub dla obu płci - w przypadku nie podania w parametach płci dla której mają zostać wywołane funkcje - domyślnie zostanie wywołana dla mężczyzn i kobiet.

Projekt został napisany w Visual Studio Code.


Dostępne komendy:
   readData(filename, new_data)
      Odczyt danych z pliku do obiektu klasy Graduate
   
   averageAttendedInYears(self, data, year, region, sex ='all')
      Wylicza średnią zdawalność w danym województwie od najniższego roku do roku podanego przez parametr funkcji
   
   passRate(self,data,year,region,sex = 'all')
      Oblicza zdawalność w podanym roku i regionie
   
   passRateInRegion(self, data, region, sex ='all')
      Oblicza zdawalność w wszystkich latach dla danego województwa
   
   passRateInYear(self, data, year, sex ='all')
      Oblicza zdawalność w danym roku dla wszystkich województw
   
   listOfRegions(self, data)
      Przepisuje do zwracanej listy wszystkie województwa które wystąpiły w pliku
   
   bestPassRate(self,data,year,sex = 'all')
      Zwraca województwo w którym zdawalność w danym roku była najwyższa
      
   passRegression(self, data, region, year, sex = 'all')
      Oblicza regresje w danym województwie miedzy rokiem podanym a następnym
   
   regionRegression(self, data, region, sex = 'all')
      Wypisuje lata w których wystąpiła regresja w danym województwie
   
   yearRegression(self,data,year,sex = 'all')
      Wypisuje województwa w których wystąpiła regresja w danym roku
      
   compareRegions(self, data, region_A, region_B, sex = 'all')
      Porównuje w którym województwie była większa zdawalność na przestrzeni lat
   
   
