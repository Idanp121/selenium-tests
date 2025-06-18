# בנה תוכנית שמבקשת מהמשתמש:
# את השם שלו
# את הגיל שלו
# ולאחר מכן:
# תחשב בעוד כמה שנים המשתמש יהיה בן 100
# תדפיס משפט מסכם עם השם והחישוב
# name = input("Enter your name" + " ")
# age = int(input("enter your age" + " "))
# x = (100 - age)
# print('your name is ' + name + " mor " + str(x) + ' year you will be 100 age')

# ספירה מ-1 עד 10
# for i in range(1, 11):
#     print(i)

# משחק ניחוש מספר פשוט

# Simple number guessing game

# secret_number = 4 #המספר הנכון 
# attempts = 3 # מספר הניסיונות

# print("👋 Hi! I'm thinking of a number between 1 and 10.")
# print("🎯 You have 3 attempts to guess it!")

# for i in range(1, attempts + 1):
#     guess = input(f"\n🔢 Attempt {i}: What's my number? ")

#     if not guess.isdigit():
#         print("⚠️ Please enter numbers only!")
#         continue

#     guess = int(guess)

#     if guess == secret_number:
#         print("🎉 Congratulations! You guessed it right!")
#         break
#     else:
#         if i < attempts:
#             print("❌ Nope, try again...")
#         else:
#             print(f"😢 Out of attempts! My number was {secret_number}")

# חישוב ממוצע
# כתוב/י פונקציה average(nums) שמקבלת רשימת מספרים ומחזירה את הממוצע. טפלו במקרה של רשימה ריקה.
# numberone = int(input("Enter number : "))
# numbertwo = int(input("Enter number : "))
# numbertree = int(input("Enter number : "))
# x = numberone + numbertwo + numbertree
# def 

#
# 🔹 תרגיל 1 – הדפסת מספרים
# כתוב לולאת for שמדפיסה את המספרים מ־1 עד 10 (כולל).

# 🔹 תרגיל 2 – חיבור מספרים
# כתוב לולאת while שמחשבת את סכום המספרים מ־1 עד 100.

# 🔹 תרגיל 3 – אותיות ברוורס
# כתוב לולאת for שמדפיסה את האותיות במילה "python" מהסוף להתחלה.

# 🔹 תרגיל 4 – רק זוגיים
# כתוב לולאה שמדפיסה את כל המספרים הזוגיים מ־0 עד 20.

# 🔹 תרגיל 5 – משתמש מזין מספרים
# בקש מהמשתמש להזין מספרים בלולאת while. עצור כשהוא מזין את המספר 0, ואז הדפס את סכום כל המספרים שהזין (לא כולל ה-0).

#תשובה לשאלה 1 
# for i in range(11):
#     print(i)
   
# # תשובה לשאלה 2 
# i = 0
# while i < 101:
#     print(i)
#     i += 1

# תשובה לשאלה מספר 3 
# word = "python"
# reversed_word = ""

# for letter in word:
#     reversed_word = letter + reversed_word

# print(reversed_word)

# תשובה לשאלה 4 

# for i in range(21):
#     if i % 2 == 0:
#         print(i)

# תשובה לשאלה 5
# total = 0

# while True:
#     number = int(input("Enter a number (0 to quit): "))
#     if number == 0:
#         break
#     total += number

# print("The total sum is:", total)

# הכנסת שם ואם השם הוא idan אז ישלים ל perz, אם לא יצא bom, כניסה רק לגיל 18 ומעלה
x = input("enter your name : ")
if x == "idan":
    print(f"hi {x} perez")
else:
    print("you are shamen")
year = 2025
y = int(input("enter your age : ")) 
if y > 18:
    print(f"you can enter in {x}")
else:
    print(f"sorry {x} go home ")
