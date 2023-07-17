import secrets,string,random

my_acci=string.ascii_letters
my_numbers=string.digits
my_special=string.punctuation

def select_word():
  '''
  this function select a word from a sentence and + it to the next word
  '''
  global my_acci_2,my_numbers_2,my_special_2
  my_acci_2=random.choice(my_acci)+random.choice(my_numbers)
  my_numbers_2=random.choice(my_numbers)+random.choice(my_acci)
  my_special_2=random.choice(my_special)+random.choice(my_numbers)
  
select_word()

def generate_password():
  '''
  this function generates the password that we want to have
  '''
  global my_pass
  my_pass=my_acci_2+my_numbers_2+my_special_2
  print(f"Your password is:{my_pass}")
  
generate_password()
  

def pass_validation():
  '''
  this function validating the password of unusable characters
  '''
  if(my_pass.find("-")>0):
    my_pass.replace("-","")
  if(my_pass.find("+")>0):
    my_pass.replace("+","")
  for i in string.digits:
    if(my_pass[0]==i):
      print("your password is incorrent please correct your password \n youcant use numbers first letter")

pass_validation()