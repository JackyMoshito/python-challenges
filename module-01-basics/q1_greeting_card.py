name = input("Enter your name: ")
age = int(input("Enter your age: "))
f_hobby = input("Enter your favorite hobby: ")

target_age = 100
years_remaining = target_age - age

print("\n--- PERSONALISED GREETING CARD ---")
print(f"Name               : {name}")
print(f"Age                : {age}")
print(f"Favorite hobby     : {f_hobby}")
print(f"Years until 100    : {years_remaining}")
print(f"-------------------------------------")
print(f"Hello {name}! Keep enjoying {f_hobby} - you have {years_remaining} great years ahead.")