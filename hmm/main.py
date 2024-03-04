import re

def main():
  while True:
    user_input = str(input(" "))
    if "*" in user_input:
      user_input_elements = [m.start() for m in re.finditer('\*', user_input)]
      for i in user_input_elements:
        user_input = user_input.replace
    if "+" in user_input:
      user_input_elements = [m.start() for m in re.finditer('\+', user_input)]
      print(user_input_elements)
    if user_input == "" or user_input == " ":
      return False

if __name__ == "__main__":
  main() 