def upper_case_name(name):
  return name.upper()

# this prevents this piece of code from running when it is being used as a library by another program
# __name__ returns "__main__" when it is being directly used. However when it is being used as a library it returns the lib name (name_lib)
if __name__ == "__main__":
  name = "DonBob"
  name = upper_case_name(name)
  print(f"Running lib code {name}")
  print(f"dunder (aka double underscore) name {__name__}")