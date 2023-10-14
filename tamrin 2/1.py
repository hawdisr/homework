class User:
  def __init__(self, username, password):
    self.username = username
    self.password = password


class Buyer(User):
  def __init__(self, username, password, address, codemeli):
    super().__init__(username, password)
    self.address = address
    self.codemeli = codemeli

  def print(self):
    print("Username:", self.username)
    print("Password:", self.password)
    print("Address:", self.address)
    print("Codemeli:", self.codemeli)


buyer = Buyer("Sara", "Ali123456", "Iran - Tehran", "2535645667")
buyer.print()









