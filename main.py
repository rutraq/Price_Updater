import csv


def read_file(file_name):
    reader = csv.reader(file_name)
    print(list(reader))


if __name__ == "__main__":
    file = "1.csv"
    with open(file) as obj:
        read_file(obj)
