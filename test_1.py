from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"D:\TestFiles\chromedriver.exe")
driver.get('https://sklep.fitomed.pl/pl/i/PROGRAM-LOJALNOSCIOWY/36')
title = driver.title
print(title)
assert 'PROGRAM LOJALNOŚCIOWY - FitoTeka' == title
driver.quit()