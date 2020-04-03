import csv


def read_file(file_name):
    reader = csv.DictReader(file_name)
    for r in reader:
        print(r["NAIMEN"] + " " + r["CENA_ROZN"])


if __name__ == "__main__":
    file = "1.csv"
    with open(file) as obj:
        read_file(obj)
