import pandas as pd
import numpy as np
import seaborn as sns
from random import randint
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")

# Statystyka opisowa(ilość danych, średnia, odchylenie standardowe, minimum, 1 kwartyl, 2 kwartyl, 3, kwartyl, maksimum)
data.drop(data.columns[[0]], axis=1, inplace=True)
print(data.describe())

def count_store_locations():
    plt.figure(figsize=(7, 7))
    plt.title("Ilosc sklepów w lokalizacjach")
    sns.histplot(data['Store_Location'], stat='count', color="red")
    plt.xlabel("Location")
    plt.ylabel("Density")
    plt.show()

# Korelacja ilości klientów do wielkości sprzedaży
def num_of_clients_to_store_sales_chart():
    plt.title("Korelacja ilości klientów do wielkości sprzedaży")
    plt.scatter(data[['Daily_Customer_Count']], data[['Store_Sales']])
    plt.xlabel('Dzienna ilość klientów')
    plt.ylabel('Ilość sprzedaży')
    plt.xticks(np.arange(0, 3000, step=300))
    plt.yticks(np.arange(0, 120000, step=12000))
    plt.plot()
    plt.show()


# Korelacja wielkości sklepu do ilości dostępnych produktów
def size_to_items_available_chart():
    plt.title("Korelacja wielkości sklepu do ilości dostępnych produktów")
    plt.scatter(data[['Store_Area']], data[['Items_Available']])
    plt.xlabel('Wielkość sklepu [m^2]')
    plt.ylabel('Ilość dostępnych produktów')
    plt.xticks(np.arange(0, 3000, step=300))
    plt.yticks(np.arange(0, 3000, step=300))
    plt.plot()
    plt.show()


# Korelacja wielkości sklepu do wielkości sprzedaży
def store_sales_to_store_area_chart():
    plt.title("Korelacja wielkości sklepu do wielkości sprzedaży")
    plt.scatter(data[['Store_Area']], data[['Store_Sales']])
    plt.xlabel('Wielkość sklepu [m^2]')
    plt.ylabel('Ilość sprzedaży')
    plt.xticks(np.arange(0, 3000, step=300))
    plt.yticks(np.arange(0, 120000, step=12000))
    plt.plot()
    plt.show()


# Model liniowy 1
def linear_model_1():
    x = data['Store_Area']
    y = data['Items_Available']
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    data['xy'] = (x - mean_x) * (y - mean_y)
    data['xx'] = (x - mean_x) ** 2

    beta = data['xy'].sum() / data['xx'].sum()
    alpha = mean_y - (beta * mean_x)
    prediction = alpha + beta * x

    plt.figure(figsize=(12, 7))
    plt.plot(x, prediction)
    plt.plot(x, y, 'ro')
    plt.title('Model liniowy 1')
    plt.xlabel('Wielkość sklepu')
    plt.ylabel('Ilość dostępnych produktów')
    plt.show()


# Model liniowy 2
def linear_model_2():
    x = data['Daily_Customer_Count']
    y = data['Items_Available']
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    data['xy'] = (x - mean_x) * (y - mean_y)
    data['xx'] = (x - mean_x) ** 2

    beta = data['xy'].sum() / data['xx'].sum()
    alpha = mean_y - (beta * mean_x)
    prediction = alpha + beta * x

    plt.figure(figsize=(12, 7))
    plt.plot(x, prediction)
    plt.plot(x, y, 'ro')
    plt.title('Model liniowy 2')
    plt.xlabel('Dziena ilość klientów')
    plt.ylabel('Ilość dostępnych produktów')
    plt.show()


count_store_locations()
num_of_clients_to_store_sales_chart()
size_to_items_available_chart()
store_sales_to_store_area_chart()
linear_model_1()
linear_model_2()
