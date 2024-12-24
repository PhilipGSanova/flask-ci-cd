def login(username,password):
  stored_username = "admin"
  stored_password = "password123"

if username == stored_username and password == stored_password:
  return "Login successful!"
else:
  return "Login failed"

if __name__ == "__main__":
  user = input("Enter username: ")
  pwd = input("Enter password: ")
  print(login(user, pwd))
