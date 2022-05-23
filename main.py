# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ctypes

# Хочу глобальную переменную, которая будет списком всех плат
plate_list = []


def create_plate_py():
    """Is needed to create a new plate. Uses ctypes.create_plate
    Args: none
    Returns: none"""
    print("Enter coordinates of a new plate and its number")
    try:
        x1 = float(input('x1='))
    except ValueError:
        print("wrong args!\n")
        return
    if not isinstance(x1, float):
        print("Not a float!\n")
        return
    if x1 < 0:
        print("you can't create a plate with negative coordinates\n")
        return
    x1 = ctypes.c_double(x1)

    try:
        x2 = float(input('x2='))
    except ValueError:
        print("wrong args!\n")
        return
    if not isinstance(x2, float):
        print("Not a float!\n")
        return
    if x2 < 0:
        print("you can't create a plate with negative coordinates\n")
        return
    x2 = ctypes.c_double(x2)

    try:
        y1 = float(input('y1='))
    except ValueError:
        print("wrong args!\n")
        return
    if not isinstance(y1, float):
        print("Not a float!\n")
        return
    if y1 < 0:
        print("you can't create a plate with negative coordinates\n")
        return
    y1 = ctypes.c_double(y1)

    try:
        y2 = float(input('y2='))
    except ValueError:
        print("wrong args!\n")
        return
    if not isinstance(y2, float):
        print("Not a float!\n")
        return
    if y2 < 0:
        print("you can't create a plate with negative coordinates\n")
        return
    y2 = ctypes.c_double(y2)

    plate_num = int(input("plate number="))
    if not isinstance(plate_num, int):
        print("Not a number!\n")
        return
    plate_num = ctypes.c_int(plate_num)

    # Проверил корректность аргументов, теперь можно создать плату
    global plate_list
    plate_list.append(libc.create_plate(x1, x2, y1, y2, plate_num))
    print("Done\n")
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    libc = ctypes.CDLL("D:/Учебная литература/Информатика/Сорокоумов/library/Dll1/x64/Debug/DLL1.dll")

    # Getting the lib ready
    # Plate* create_plate(double x1 = 0, double x2 = 0, double y1 = 0, double y2 = 0, int plateNumber = 1)
    libc.create_plate.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    libc.create_plate.restype = ctypes.c_void_p

    # void delete_plate(Plate* plate)
    libc.delete_plate.argtypes = [ctypes.c_void_p]
    libc.delete_plate.restype = None

    # add_contact_data()
    libc.add_contact_data.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                      ctypes.c_int, ctypes.c_char_p]
    libc.add_contact_data.restype = ctypes.c_int

    # add_power_contact()
    libc.add_power_contact.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                       ctypes.c_int, ctypes.c_double]
    libc.add_power_contact.restype = ctypes.c_int

    # int remove_contact(Plate* plate, int x, int y)
    libc.remove_contact.argtypes = [ctypes.c_void_p, ctypes.c_int, ctypes.c_int]
    libc.remove_contact.restype = ctypes.c_int

    # void contact_info(Contact* contact)
    libc.contact_info.argtypes = [ctypes.c_void_p]
    libc.contact_info.restype = None

    # void plate_info(Plate* plate)
    libc.plate_info.argtypes = [ctypes.c_void_p]
    libc.plate_info.restype = None

    # Device* create_device(string name)
    libc.create_device.argtypes = [ctypes.c_char_p]
    libc.create_device.restype = ctypes.c_void_p

    # void delete_device(Device* device)
    libc.delete_device.argtypes = [ctypes.c_void_p]
    libc.delete_device.restype = None

    # Хочу создать контейнер с платами

    while True:
        print("=============================================================\n")
        print("1) Create a new plate\n"
              "2) Delete a plate\n"
              "3) Add a contact\n"
              "4) Remove a contact\n"
              "5) Get info about plate\n"
              "0) Exit\n")
        i = input("What do you want: ")
        i = int(i)
        match i:
            case 1:
                create_plate_py()
            case _:
                break

# See PyCharm help at https://www.jetbrains.com/he1p/pycharm/
