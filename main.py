import csv
from selenium import webdriver
from time import sleep

product_name = {}


def read_file(file_name):
    reader = csv.DictReader(file_name)
    for r in reader:
        try:
            count = int(r["SKLAD_ALL"])
        except ValueError:
            count = 0
        info = [r["CENA_ROZN"].replace(",", "."), count]
        product_name[r["NAIMEN"]] = info
    return product_name


def search_product(login, password):
    driver = webdriver.Firefox("/home/rutraq/Projects Python/Geckodriver")
    driver.get("https://zozo.by/admin/index.php?route=catalog/product")
    user = driver.find_element_by_id("input-username")
    user.send_keys(login)
    passw = driver.find_element_by_id("input-password")
    passw.send_keys(password)
    passw.submit()
    sleep(6)
    for i in product_name:
        check_product = driver.find_element_by_id("input-name")
        check_product.clear()
        check_product.send_keys(i)
        button_filter = driver.find_element_by_id("button-filter")
        sleep(1)
        button_filter.click()
        sleep(1)
        price = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[2]/form/div/table/tbody/tr/td[5]")
        price = price.text
        settings = driver.find_element_by_xpath(
            "/html/body/div/div/div[2]/div/div[2]/form/div/table/tbody/tr/td[9]/a")
        if float(product_name[i][0]) != float(price):
            settings.click()
            sleep(2)
            info = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[2]/a")
            info.click()
            sleep(3)

            input_stock = driver.find_element_by_id("input-quantity")
            print(input_stock.get_attribute("value"))
            if int(input_stock.get_attribute("value")) == 0 and product_name[i][1] != 0:
                stock = '99'
                change_stock2(input_stock, stock)
            elif int(input_stock.get_attribute("value")) != 0 and product_name[i][1] == 0:
                stock = '0'
                change_stock2(input_stock, stock)

            price_product = driver.find_element_by_id("input-price")
            price_product.clear()
            price_product.send_keys(product_name[i][0])
            sleep(2)
            save = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/button")
            save.click()

        in_stock = driver.find_element_by_xpath('//*[@id="form-product"]/div/table/tbody/tr/td[7]/span')
        if int(in_stock.text) == 0 and product_name[i][1] != 0:
            stock = '99'
            change_stock(settings, driver, stock)
        elif int(in_stock.text) != 0 and product_name[i][1] == 0:
            stock = '0'
            change_stock(settings, driver, stock)


def change_stock(settings, driver, stock):
    settings.click()
    sleep(2)
    info = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/form/ul/li[2]/a")
    info.click()
    sleep(2)
    input_stock = driver.find_element_by_id("input-quantity")
    input_stock.clear()
    input_stock.send_keys(stock)
    save = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/button")
    save.click()


def change_stock2(input_stock, stock):
    input_stock.clear()
    input_stock.send_keys(stock)


if __name__ == "__main__":
    file = "1.csv"
    with open(file) as obj:
        read_file(obj)
    print(product_name)
    search_product("vasya", "qwertyadmin")
