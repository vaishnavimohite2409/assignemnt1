def personalized_greeting():

  first_name = input("Enter your first name: ")
  last_name = input("Enter your last name: ")

  full_name = first_name + " " + last_name  # Concatenate with a space

  print(f"Hello, {full_name}! Welcome! delighted to meet you")

if __name__ == "__main__":
  personalized_greeting()
