from pprint import pprint

import psutil

def temperatura() -> float:
    sensors = psutil.sensors_temperatures()

    if __name__ == "__main__":
        pprint(sensors)

    promedio = 0
    cantidad = 0
    for sensor in sensors:
        s = sensors.get(sensor)[0]
        temp = s.current
        promedio = promedio + temp
        cantidad += 1

    promedio = promedio // cantidad
    return promedio

if __name__ == '__main__':
    print(temperatura())