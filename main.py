from enum import Enum
import re

s = str(input("Enter string: "))
s = s.replace(';', ' ; ')
s = s.replace('=', ' = ')
s = s.replace(',', ' , ')
tokens = s.split()

class Types(Enum):
  DATA_TYPE     = 0
  EQUALS        = 1
  VALID_STR     = 2
  NUMBER        = 3
  COMMA         = 4
  SEMICOLON     = 5
  INVALID       = 6

table = [
  [2,1,1,1,1,1,1],
  [1,1,1,1,1,1,1],
  [1,1,3,1,1,1,1],
  [1,4,1,1,7,6,1],
  [1,1,1,5,1,1,1],
  [1,1,1,1,7,6,1],
  [0,1,1,1,1,1,1],
  [1,1,3,1,1,1,1],
]

def str_is_number(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

def str_is_valid_name(s):
  return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', s)

def get_type(s):
  if s == 'int':
    return Types.DATA_TYPE
  if s == '=':
    return Types.EQUALS
  if s == ',':
    return Types.COMMA
  if s == ';':
    return Types.SEMICOLON
  if str_is_valid_name(s):
    return Types.VALID_STR
  if str_is_number(s):
    return Types.NUMBER
  return Types.INVALID
  

print(tokens, '\n')
state = 0
for c in tokens:
  input_type = get_type(c)
  print(str(input_type).replace("Types.",""))
  state = table[state][input_type.value]
  print(f'CURRENT TOKEN = {c}')
  print(f'CURRENT STATE = {state}')
  input()
  
if state == 6:
  print(f'STRING ACCEPTED')
else:
  print(f'INT DECALARATION IS INVALID')

