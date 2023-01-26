#!/usr/bin/python3
from selenium import webdriver
from datetime import date
from time import sleep

file = "data.csv"

# variables
exit_code = 0
max_tries = 20
error = True
error_count = 0

# Get on the page
try:
    driver = webdriver.Firefox()
    driver.get("http://192.168.1.225/index.html")
except:
    error = True
    error_count = max_tries + 1


# Try to fetch data from page
while error == True and error_count < max_tries:
    error = False
    try:
        day_energy = driver.find_element_by_id('Energy_Day').get_attribute("value")
        max_day_energy = driver.find_element_by_id('PMAX_Day').get_attribute("value")
        all_energy = driver.find_element_by_id('Energy').get_attribute("value")
        
        if day_energy == "" or max_day_energy == "" or all_energy == "":
            error = True
            error_count = error_count + 1
            sleep(0.1)
    except:
        error = True
        error_count = error_count + 1
    
# If failed, append empty line to say script was executed correctly
if error_count >= max_tries:
    day_energy = ""
    max_day_energy = ""
    all_energy = ""  
    exit_code = 3  
    
# parse data
new_line = "{};{};{};{}\n".format(date.today() ,day_energy, max_day_energy, all_energy)
new_line = new_line.replace('.', ',')

# append to file
file1 = open(file, "a")
file1.write(new_line)
file1.close()


driver.close()
exit(exit_code)

