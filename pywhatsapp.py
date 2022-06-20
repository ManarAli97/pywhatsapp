# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import mysql.connector
# from datetime import datetime
# from datetime import date
# import sys
# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')
# options = webdriver.ChromeOptions()
# options.add_argument('--user-data-dir=/User_data')
# today = date.today()

# # dd/mm/YY
# d1 = today.strftime("%Y/%m/%d")
# success = 0
# error = 0
# # timestamp = 1655298813
# # dt_obj = datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")

# # print("date:",dt_obj)
# # if d1 == dt_obj:
# #   print("Today is:")

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="whatsapp"
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT phone, date, message FROM whatsapppy WHERE date = 0")

# myresult = mycursor.fetchall()
# phones = []
# for x in myresult:
#   v = x[0]
#   d = x[1]
#   message = x[2]
#   phones.append(v)
#   # dt_obj = datetime.fromtimestamp(d).strftime("%Y/%m/%d")
#   # if(d1 == dt_obj):
#     # phones.append(v)
# print(len(phones))



# # for phone in phones:
# #     driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe',chrome_options=options)
# #     driver.get(f'https://web.whatsapp.com/send?phone=+964{phone}&text={message}')
# #     sleep(5)
# #     try:
# #         driver.implicitly_wait(35)
# #         button = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
# #         button.click()
# #         sleep(10)
# #         success++
# #         print("success:",success)
# #         driver.close()
# #     except Exception as e:
# #         driver.close()
# #         error++
# #         print("error:",error)
# #         print(e)



from time import sleep
from urllib.parse import urlencode
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import mysql.connector
from datetime import datetime
from datetime import date
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/User_data')
today = date.today()

# dd/mm/YY
d1 = today.strftime("%Y-%m-%d")
success = 0
error = 0
# timestamp = 1655298813
# dt_obj = datetime.fromtimestamp(timestamp).strftime("%Y/%m/%d")

# print("date:",dt_obj)
# if d1 == dt_obj:
#   print("Today is:")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="amani_sms"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT phone, `msg` FROM phone_whats WHERE date = '"+d1+"' AND deleted = 0")

myresult = mycursor.fetchall()
phones = []
msgs = []
for x in myresult:
  phones.append(x[0])
  msgs.append(str(x[1]))
  # dt_obj = datetime.fromtimestamp(d).strftime("%Y/%m/%d")
  # if(d1 == dt_obj):
  # phones.append(v)
  # print(message)
# print(len(phones))



for (i, phone) in enumerate(phones):
  driver = webdriver.Chrome(executable_path='C:/chromedriver/chromedriver.exe',chrome_options=options)
  driver.get(f'https://web.whatsapp.com/send?phone=+964{phone}&text={msgs[i]}')
  sleep(5)
  try:
    driver.implicitly_wait(35)
    button = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    button.click()
    sleep(10)
    success = success + 1
    driver.close()
  except Exception as e:
    driver.close()
    error = error + 1
    print(e)

print("All Message: ",len(phones))
print("\nsuccess:",success)
print("\nerror:",error)
