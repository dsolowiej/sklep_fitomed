import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
   @classmethod
   def setUpClass(self):
       self.driver = webdriver.Chrome(executable_path=r'D:\TestFiles\chromedriver.exe')

   def test_strona_jeden(self):
       driver = self.driver
       driver.get('https://www.printwhatyoulike.com/?ref=discuvver')
       title = driver.title
       print(title)
       assert 'Save paper & ink printing only what you want « PrintWhatYouLike.com' == title

   def test_strona_dwa(self):
       driver = self.driver
       driver.get('https://www.printwhatyoulike.com/support')
       title = driver.title
       print(title)
       assert 'Support « PrintWhatYouLike.com' == title

   @classmethod
   def tearDownClass(self):
       self.driver.quit()



