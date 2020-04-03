import csv
from selenium import webdriver
from time import sleep

product_name = []


def read_file(file_name):
    reader = csv.DictReader(file_name)
    for r in reader:
        print(r["NAIMEN"] + " " + r["CENA_ROZN"])
        product_name.append(r["NAIMEN"])
    return product_name


def search_product(login, password):
    driver = webdriver.Firefox("/home/evgeniy/Рабочий стол/Check/")
    driver.get("https://zozo.by/admin/index.php?route=catalog/product")
    user = driver.find_element_by_id("input-username")
    user.send_keys(login)
    passw = driver.find_element_by_id("input-password")
    passw.send_keys(password)
    passw.submit()
    sleep(4)
    for i in product_name:
        print(i)
        check_product = driver.find_element_by_id("input-name")
        check_product.clear()
        check_product.send_keys(i)
        button_filter = driver.find_element_by_id("button-filter")
        sleep(1)
        button_filter.click()
        sleep(1)


if __name__ == "__main__":
    file = "1.csv"
    with open(file) as obj:
        read_file(obj)
    search_product("admin", "8765tgrfcd675hgtf")
