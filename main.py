# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import ctypes
import os


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # libname = os.path.abspath(
    # os.path.join(os.path.dirname(__file__), "DLL1.dll"))
    #   os.path.join(os.path.dirname(__file__), "D:/Учебная литература/Информатика/Сорокоумов/library/Dll1/x64/Debug/DLL1.dll"))

    libc = ctypes.CDLL("D:/Учебная литература/Информатика/Сорокоумов/library/Dll1/x64/Debug/DLL1.dll")
    libc.create_plate.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_int]
    libc.create_plate.restype = ctypes.c_void_p
    plate = libc.create_plate()

    i = libc.create_plate(0, 30, 0, 30, 1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
