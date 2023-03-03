import auth_package
login_or_registration = input("login or registration ")
if login_or_registration == "login":
    from auth_package import login
elif login_or_registration == "registration":
    from auth_package import registration    