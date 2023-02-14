# 1
users = [ [] ]
if users:
    print("users exist")
else:
    print("users not found")    

# 2
pythonists = ["Bush", "Jarvis", "Oxxi", "Buffon", "Vardan",]
# ---- 2.1 ----
if "Sur" in pythonists:
    print(pythonists)
else:
    pythonists.append("Sur")
    print(pythonists)

# ---- 2.2 ----
if 5<len(pythonists)<7:
    print(pythonists)
elif len(pythonists)<5:
    pythonists.append(input("appended new user"))
    print(pythonists)
elif len(pythonists)>7:
    pythonists.remove(input("user removed"))
    print(pythonists)

# 3
x = 0
while x < 20:
    x = x + 2
    print(x)

# 4
x = 21
while x > 0:
    x = x - 1
    if x == 17:
        continue
    print(f"{x}={x**2}")

# 5
x = 1
y = 0
while x < 50:
    if x % 3 == 0:
        if y == 10 :
            break
        print(x)   
        y = y + 1 
    x = x + 1         



