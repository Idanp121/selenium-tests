from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from PIL import Image

# הגדרות עבור פתיחת כרום
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# הפעלת הדפדפן
driver = webdriver.Chrome(options=chrome_options)

# שלב 1: כניסה לקישור
driver.get("https://u.pcloud.link/publink/show?code=kZiwDj5ZTEa4RK2tViRR5fvjfxKLGJmxHy0X")

# המתנה לטעינה
time.sleep(5)

# שלב 2: כניסה לתיקיה BR-036
br_folder = driver.find_element(By.XPATH, "//div[text()='BR-036']")
br_folder.click()
time.sleep(5)

# שלב 3: כניסה לקובץ PDF
pdf_file = driver.find_element(By.XPATH, "//div[contains(text(),'.pdf')]")
pdf_file.click()
time.sleep(10)  # ממתינים שה-PDF ייפתח

# שלב 4: צילום מסך מלא
screenshot = pyautogui.screenshot()

# שמירת צילום מסך זמני
temp_path = "temp_full_screenshot.png"
screenshot.save(temp_path)

# שלב 5: חיתוך התמונה של התכשיט (צריך להתאים לפי מיקום על המסך)
# כאן דוגמה למיקום - תעדכן לפי הצורך
left = 300  # נקודת התחלה ציר X
top = 250   # נקודת התחלה ציר Y
width = 800
height = 600

image = Image.open(temp_path)
cropped_image = image.crop((left, top, left + width, top + height))

# שמירה של התמונה בתיקיה שציינת
save_path = r"C:\Users\idanp\OneDrive\שולחן העבודה\פרוייקטים\Brantelny modols\תמונות\jewel_image.png"
cropped_image.save(save_path)

# סיום
print("✅ תהליך הושלם! התמונה נשמרה.")

driver.quit()
