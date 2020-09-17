import re

input_str = input("Please provide some info: ")
if not re.match("^[a-z]*$", input_str):
    print ("Error! Only letters a-z allowed!")