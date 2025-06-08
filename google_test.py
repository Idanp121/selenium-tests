from selenium import webdriver  # מייבא את הספרייה Selenium לעבודה עם דפדפנים
from selenium.webdriver.common.keys import Keys  # מייבא את מקשי המקלדת (כמו Enter)
import time  # מאפשר שימוש בהשהיה

# מפעיל את דפדפן Chrome
driver = webdriver.Chrome()

# נכנס לאתר של גוגל
driver.get("https://www.google.com")

# מחפש את שדה החיפוש לפי שם (name="q")
search_box = driver.find_element("name", "q")

# מקליד את הטקסט לשדה
search_box.send_keys ("אח שלי היקר")

# לוחץ על אנטר כדי לבצע את החיפוש
search_box.send_keys(Keys.RETURN)

# ממתין 3 שניות כדי שנראה את התוצאה
time.sleep(8)

# סוגר את הדפדפן
driver.quit()
