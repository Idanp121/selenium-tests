from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# רשימת המינים לבדיקה
genders = ["Male", "Female", "Other"]

# לולאה לכל מין
for gender in genders:
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()

    # מילוי שדות קבועים
    driver.find_element(By.ID, "firstName").send_keys("יוסי")
    driver.find_element(By.ID, "lastName").send_keys("כהן")
    driver.find_element(By.ID, "userEmail").send_keys("yossi@example.com")

    # בחירת מין לפי הטקסט (משתנה בכל פעם בלולאה)
    driver.find_element(By.XPATH, f"//label[text()='{gender}']").click()

    driver.find_element(By.ID, "userNumber").send_keys("0501234567")
    driver.find_element(By.XPATH, "//label[text()='Sports']").click()
    driver.find_element(By.ID, "currentAddress").send_keys("רחוב הדוגמה 5, תל אביב")

    # גלילה למטה כדי שהכפתור יהיה גלוי
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # שליחת הטופס
    driver.find_element(By.ID, "submit").click()

    # המתנה לפופאפ – רק לראות שהטופס נקלט
    time.sleep(6)

    # סגירת הפופאפ – כדי שההרצה תוכל להתקדם (או סגירת דפדפן)
    driver.find_element(By.ID, "closeLargeModal").click()

    # סגירת הדפדפן
    driver.quit()

