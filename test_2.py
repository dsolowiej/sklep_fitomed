import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
   @classmethod
   def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path=r'D:\TestFiles\chromedriver.exe')

   def test_demo_login(self):
       driver = self.driver
       driver.get('https://sklep.fitomed.pl/pl/login')
       title = driver.title
       print(title)
       assert 'FitoTeka' == title

   def test_demo_newsletter(self):
       driver = self.driver
       driver.get('https://sklep.fitomed.pl/pl/reg?')
       title = driver.title
       print(title)
       assert 'FitoTeka' == title

   def test_demo_surowce(self):
       driver = self.driver
       driver.get('https://sklep.fitomed.pl/pl/c/SUROWCE-KOSMETYCZNE/60')
       title = driver.title
       print(title)
       assert 'SUROWCE KOSMETYCZNE - FitoTeka' == title

   @classmethod
   def tearDownClass(self):
        self.driver.quit()