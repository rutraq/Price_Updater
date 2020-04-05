import csv
from selenium import webdriver
from time import sleep

product_name = {}


def read_file(file_name):
    reader = csv.DictReader(file_name)
    for r in reader:
        product_name[r["NAIMEN"]] = r["CENA_ROZN"].replace(",", ".")
    for key in product_name:
        print(product_name[key])
    return product_name


def search_product(login, password):
    driver = webdriver.Firefox("/home/evgeniy/Рабочий стол/Check/")
    driver.get("https://zozo.by/admin/index.php?route=catalog/product")
    user = driver.find_element_by_id("input-username")
    user.send_keys(login)
    passw = driver.find_element_by_id("input-password")
    passw.send_keys(password)
    passw.submit()
    sleep(6)
    for i in product_name:
        print(i + "     " + product_name[i])
        check_product = driver.find_element_by_id("input-name")
        check_product.clear()
        check_product.send_keys(i)
        button_filter = driver.find_element_by_id("button-filter")
        sleep(1)
        button_filter.click()
        sleep(1)
        try:
            price = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/form/div/table/tbody/tr/td[5]")
            if int(product_name[i]) != int(price):
                print(product_name[i])
                print(price.text)
                settings = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/form/div/table/tbody/tr/td[9]/a")
                settings.click()
                sleep(2)
                info = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[2]/a")
                info.click()
                sleep(2)
                price_product = driver.find_element_by_id("input-price")
                price_product.clear()
                price_product.send_keys(product_name[i])
                sleep(2)
                save = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/button")
                save.click()
        except:
            sleep(1)


if __name__ == "__main__":
    file = "1.csv"
    with open(file) as obj:
        read_file(obj)
    print(product_name)
    search_product("admin", "8765tgrfcd675hgtf")
