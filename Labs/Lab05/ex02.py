def ex02_main():
    pin = "1234"
    count = 0
    while count <= 2:
      x = input("Enter your pin: ")
      if x == pin:
          print("Your PIN is correct.")
          break
      else:
          print("Your pin is incorrect.")
          count += 1
    else:
     print("Your bank card is blocked.")


ex02_main()
