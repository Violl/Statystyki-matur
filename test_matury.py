import pytest
import matury
import csv

def test_passRate_one():
    data = matury.Graduate('','','','','')
    data.readData('baza_maturzystow.csv',data)
    result = data.passRate(data,2012,'pomorskie','Kobiety')
    assert result == 79.97

def test_passRate_two():
    data = matury.Graduate('','','','','')
    data.readData('baza_maturzystow.csv',data)
    result = data.passRate(data,'2015','warmińsko-Mazurskie')
    assert result == 70.92
    
def test_passRate_three():
    data = matury.Graduate('','','','','')
    data.readData('baza_maturzystow.csv',data)
    result = data.passRate(data,'2018','Zachodniopomorskie')
    assert result == 76.82


def test_capitalize_region():
    result = matury.capitalize_region("warmińsko-mazurskie")
    assert result == 'Warmińsko-Mazurskie'

def test_averageAttendedInYears():
    data = matury.Graduate('','','','','')
    data.readData('baza_maturzystow.csv',data)
    result = data.averageAttendedInYears(data,2014,'warmińsko-mazurskie')
    assert result == 12365.8


