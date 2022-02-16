import os
import threading
from django.shortcuts import render
import json
import random
import datetime
from .models import Point, Type, Device

time_step = 5 * 60 * 1000


# получение путей к девайс-значение
def select_path():
    _location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(_location, 'settings.json')) as read_file:
        paths = json.load(read_file)
    return paths


# чтение показателей и занос в базу
def select_point():
    global time_step
    temp = select_path()
    try:
        for element in temp:
            name_device = Device.objects.filter(device=element["name"])[0].pk
            name_files = element["path"]

            types_list_temp = str(element["params"]).split(";")
            types_list = list()
            for t in types_list_temp:
                c = Type.objects.filter(type=t)[0].pk
                types_list.append(c)

            files = open(name_files, 'r')
            list_value = list()
            for i in list_value:
                j = 0
                point = float(random.randint(0, 100))
                Point.objects.get_or_create(device=name_device, value=point, time=datetime.datetime.now(),
                                            type_id=types_list[j])
            files.close()
            os.remove(name_files)

    except Exception as e:
        print("error: " + e)
    threading.Timer(time_step, select_point()).start()


select_point()


def define_home(request):
    if request.POST:
        types = request.POST["type"]
        if types == "select":
            time_from = convertDataTime(str(request.POST["time_from"]))
            time_to = convertDataTime(str(request.POST["time_to"]))

    list_type = Type.objects.all()
    list_devices = Device.objects.all()

    a = returnInDatabase()
    a["zipped"] = requestInDatebase()
    return render(request, "public/home.html", context=a)


def returnInDatabase():
    return {
        "point": 2020,
        "zipped": list([
            ["Installation", [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]],
            ["Manufacturing", [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]],
            ["Sales", [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]],
            ["Project Development", [7988, 12169, 7988, 12169, 15112, 22452, 34400, 34227]]
        ]),
        "pointSelect": 2020,
        "zippedSelect": list([
            ["Installation", [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]],
            ["Manufacturing", [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]],
            ["Sales", [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]],
            ["Project Development", [7988, 12169, 7988, 12169, 15112, 22452, 34400, 34227]]
        ])
    }


def requestInDatebase():
    a = Point.objects.all()
    allName = list()
    allPoint = list()
    for point in a:
        if point.device not in allName:
            allName.append(point.device)
            allPoint.append(list())
        index = allName.index(point.device)
        allPoint[index].append(point.value)
    resultList = list()
    for i in range(0, len(allName), 1):
        resultList.append([allName[i], allPoint[i]])
    return resultList


def convertDataTime(time):
    temp = time.split('T')
    date = temp[0].split('-')
    temp_time = temp[1].split(':')
    return datetime.datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]), hour=int(temp_time[0]),
                             minute=int(temp_time[1]), second=int(temp_time[2]))
