import openpyxl
import pandas as pd
import statistics
import math
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew

data = [32, 54, 43, 31, 7, 3, 8, 32, 945, 426, 423, 654, 132, 43, 32, 32, 543, 64, 87, 432, 31, 843, 423, 75, 45, 55]


def srednia():
    sum = 0
    for el in data:
        sum += el
    return sum / len(data)


def odchylenie_standardowe():
    srd = srednia()
    sum = 0
    step = 0
    for el in data:
        sum += pow(el - srd, 2)
    return math.sqrt(sum / srd)


def wspolczynnik_zmiennosci():
    return (odchylenie_standardowe() / srednia())*100


def minimum():
    return min(data)


def percentyl_10():
    return np.percentile(data, 10)


def kwartyl_1():
    return np.quantile(data, 0.25)


def mediana():
    return statistics.median(data)


def kwartyl_3():
    return np.quantile(data, 0.75)


def percentyl_90():
    return np.percentile(data, 90)


def maksimum():
    return max(data)


def rozstep_danych():
    return maksimum() - minimum()


def rozstep_miedzykwartylowy():
    q3, q1 = np.percentile(data, [75, 25])
    return q3 - q1


def skosnosc():
    # Fisher-Pearson correlation of skewness
    return skew(data)


def kurtoza():
    # PEARSON's definition -> Normal value is 3
    return kurtosis(data, fisher=False)


def export_output():
    df = pd.DataFrame(data_obj)

    df.to_excel("wynik.xlsx", sheet_name="zadanie 2")


data_obj = {
    "Nazwa Statystyki": ["średnia", "odchylenie standardowe", "współczynnik zmienności", "minimum", "10 percentyl", "1 kwartyl",
             "mediana", "3 kwartyl", "90 percentyl", "maksimum", "rozstęp danych", "rozstęp miedzykwartylowy",
             "skośność", "kurtoza"],
    "Wartość": [srednia(), odchylenie_standardowe(), wspolczynnik_zmiennosci(), minimum(), percentyl_10(), kwartyl_1(),
              mediana(), kwartyl_3(), percentyl_90(), maksimum(), rozstep_danych(), rozstep_miedzykwartylowy(),
              skosnosc(), kurtoza()]
}

export_output()