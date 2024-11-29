def check_age(age):
    assert age >= 18, "Вам має бути 18 років або більше"
    print("Ви можете використовувати цей сервіс")
try:
    check_age(17)
except AssertionError as age:
    print(age)

try:
    check_age(20)
except AssertionError as age:
    print(age)
