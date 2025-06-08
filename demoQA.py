from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# פונקציה: גלילה + לחיצה בטוחה
def scroll_and_click(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element.get_attribute("xpath"))))
    element.click()

# פונקציה: הסרת פרסומות iframe מהדף
def remove_ads(driver):
    driver.execute_script("""
        const ads = document.querySelectorAll('iframe');
        ads.forEach(ad => ad.remove());
    """)

# רשימת המינים לבדיקה
genders = ["Male", "Female", "Other"]

for gender in genders:
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/automation-practice-form")
    driver.maximize_window()

    # הסרת פרסומות שמפריעות
    remove_ads(driver)

    # מילוי שדות בסיסיים
    driver.find_element(By.ID, "firstName").send_keys("יוסי")
    driver.find_element(By.ID, "lastName").send_keys("כהן")
    driver.find_element(By.ID, "userEmail").send_keys("yossi@example.com")

    # בחירת מין (gender)
    gender_element = driver.find_element(By.XPATH, f"//label[text()='{gender}']")
    driver.execute_script("arguments[0].scrollIntoView();", gender_element)
    gender_element.click()

    # מספר טלפון
    driver.find_element(By.ID, "userNumber").send_keys("0501234567")

    # בחירת תחביב - Sports
    sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
    driver.execute_script("arguments[0].scrollIntoView();", sports_checkbox)
    sports_checkbox.click()

    # כתובת
    driver.find_element(By.ID, "currentAddress").send_keys("רחוב הדוגמה 5, תל אביב")

    # גלילה לסוף הדף לפני שליחה
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # שליחת הטופס
    driver.find_element(By.ID, "submit").click()

    # המתנה קצרה לראות את הפופאפ
    time.sleep(2)

    # ניסיון סגירת הפופאפ עם כל ההגנות
    try:
        remove_ads(driver)
        modal_close_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "closeLargeModal"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", modal_close_btn)
        modal_close_btn.click()
    except Exception as e:
        print(f"שגיאה בסגירת הפופאפ: {e}")

    # סגירת הדפדפן
    driver.quit()
