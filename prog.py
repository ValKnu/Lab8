
import csv
from distutils.log import error
import errno

fileN='dataT.csv'

def open_or_create_file(filename):
    try:
        with open(filename, "r") as file:
            print("Файл існує")
    except FileNotFoundError as error:
        print("Файл не присутній")
        with open(filename, "w+") as file:
            data = [['Name', 'class',]]
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

def class_filter(age):
    try :
        intage=int(age)
        if (intage==6 or intage== 7):
            return 1

        elif (intage==8):
            return 2

        elif (intage==9):
            return 3

        elif (intage==10):
            return 4
        else:
            return "none"
    except ValueError as error:
        return "ValueError"


def show_tabl(filename):
    with open(filename, "r+") as file:
        text=csv.DictReader(file, delimiter=',')
        print("Name ----- class")
        for line in text:
        
            print(line["Name"], "-----", line["class"])

if __name__ == "__main__":
    open_or_create_file(fileN)

    with open(fileN, "r+") as file:
        text=csv.DictReader(file, delimiter=',')
        print("Name ----- class")
        for line in text:
        
            print(line["Name"], "-----", line["class"])

        writer = csv.writer(file)
        print("Щоб зупинити запис у полі ім'я напишить -")
        while(True):
       
            student = input("Введіть призвіще, ім'я:")
            if(student=="-"):
                break
            age = int(input("Введіть вік дитини:"))
            writer.writerow([student, class_filter(age)])

    show_tabl(fileN)



    
