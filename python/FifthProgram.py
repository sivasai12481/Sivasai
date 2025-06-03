'''
a="""My name is sai,
ans I ma from perf team,"""
print(a)

print("second letter in variable a")
a = "Hello, World!"
print(a[1])

print("letters in banana")
for x in "banana":
  print(x)

print(len(a))

txt = "The best things in life are free!"
print(txt)
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

'''

print("F-String was introduced in Python 3.6")
import sys
version=sys.version
print(f"python version is {version}")

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

print("escape character allows you to use double quotes")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
