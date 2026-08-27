import random
import csv
import matplotlib.pyplot as plt
import numpy as np

nombre = input("Enter the name of your patient: ")

num_med = int(input("How many meseaurements do you wish to generate (Suggested: 60)? "))

print("Set lower and upper boundaries")

lowerb = int(input("Enter lower boundary: "))
upperb = int(input("Enter upper boundary: "))


medidaanterior = int(random.randrange(50, 110))

def generate_measurements(medidaanterior):
    
    medidasuave = medidaanterior + random.randint(-5, 5)
    medidasuave = max(50, min(110, medidasuave))

    return medidasuave




def calculate_statistics(arrai):
    
    average = np.mean(arrai)
    maxi = np.max(arrai)
    minimo = np.min(arrai)

    statistics = [maxi, minimo, average]
    return f"\nTotal measurements: {len(arrai)}\nMaximum rate: {statistics[0]} \nMinimum rate: {statistics[1]} \nAverage: {statistics[2]}"


def classify_measurement(medida, lowerlimit, upperlimit):
    if medida > upperlimit:
        return "Above selected range"
    elif medida < lowerlimit:
        return "Under the selected range"
    else:
        return "Within the selected range"
    
    
def create_csv(datos, ruta):

    with open(ruta, "w", newline="", encoding="utf-8") as file:
        escritor = csv.writer(file)
        for row in datos:
            escritor.writerow(row)
    
    print(f"Data saved in '{ruta}'")


def create_chart(x_axis, y_axis, nombre, tiempo, promedio):
    plt.plot(x_axis, y_axis)
    plt.axhline(
    y=promedio,
    color="red",
    linestyle="--",
    label="Average"
)

    plt.xlabel("Minutes")
    plt.ylabel("Beats per Minute (BPM)")
    plt.title(f"{nombre}'s BPM measurements along {tiempo} minutes")

    
    plt.savefig('graph.png')
    plt.show()
    print(f"Data saved in 'graph.png'")



mlist = [] # BPM measurements list
minutes = [] # Lista de minutos (Eje x de la grafica)
datas = [["Minute", "Heart Rate", "Status"]] # List of lists for the cvs file
filas = [] # Transitional list for each individual row of the cvs file (changes within the for loop)
file_path = "heart_rate_data.csv"

for i in range(1, num_med+1, 1):
    measure = generate_measurements(medidaanterior)
    medidaanterior = measure
    print(f"Minute {i}: {measure}")
    mlist.append(measure)
    minutes.append(i)

    filas = [i, measure, classify_measurement(measure, lowerb, upperb)]
    datas.append(filas)

measurements_array = np.array(mlist)
promedio = np.mean(measurements_array)

print(calculate_statistics(measurements_array))
create_csv(datas, file_path)
create_chart(minutes, mlist, nombre, num_med, promedio)







