from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# יצירת דפדפן
driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")

# הגדלת המסך למניעת בעיות פריסה
driver.maximize_window()

# הזנת שם פרטי
driver.find_element(By.ID, "firstName").send_keys("יוסי")

# שם משפחה
driver.find_element(By.ID, "lastName").send_keys("כהן")

# אימייל
driver.find_element(By.ID, "userEmail").send_keys("yossi@example.com")

# בחירת מין (Male)
driver.find_element(By.XPATH, "//label[text()='Male']").click()

# מספר טלפון
driver.find_element(By.ID, "userNumber").send_keys("0501234567")

# בחירת תאריך לידה (לחיצה ואז בחירה דרך JavaScript או עם חיצים – דילגנו לצורך פשטות)

# בחירת תחביב: Sports
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

# הזנת כתובת
driver.find_element(By.ID, "currentAddress").send_keys("רחוב הדוגמה 5, תל אביב")

# גלילה למטה (חשוב!)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# שליחת טופס
driver.find_element(By.ID, "submit").click()

# המתנה קצרה לראות את הפופאפ
time.sleep(3)

# סגירת דפדפן
driver.quit()
