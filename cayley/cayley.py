#!/usr/bin/python

import sys

from fractions import gcd

def createGroup(group_type, group_size):
  '''Creates the group needed for generating a cayley table
  
    :param group_type: group type ("u" or "z")
    :type group_type: string
    :param group_size: size of group
    :type group_size: int
    :returns: generated group based on group type and group size
    :rtype: array
  '''
  if group_type == "u":
    generated_group = createUGroup(group_size)
  elif group_type == "z":
    generated_group = createZGroup(group_size)
  
  return generated_group

def createZGroup(group_size):
  '''Creates a Z group
  
    :param group_size: size to make group
    :type group_size: int
    :returns: generated z group
    :rtype: array
  '''
  zgroup = range(0, group_size)
  return zgroup

def createUGroup(group_size):
  '''Creates U Group which is made up of all relative primes less then the group size
  
    :param group_size: the size determins group size and used to find primes relative to it
    :type group_size: int
    :returns: generated u group
    :rtype: array
  '''
  start_value = 1
  relative_primes = []
  for i in range(start_value, group_size):
    greatest_common_divisor = gcd(i, group_size)
    if greatest_common_divisor == 1:
      relative_primes.append(i)

  return relative_primes

def createTable(group_type, group_size, operator):
  '''Creates a Cayley based on defined group type, group size, and operator
  
    :param group_type: group type
    :type group_type: string
    :param group_size: size of group
    :type group_size: int
    :param operator: operator performed to generate table
    :type operator: string
    :returns generated cayley table
    :rtype: array
  '''
  group = createGroup(group_type, group_size)
  cayley_table = []

  for i in group:
    columns = []
    for j in group:
      if operator == "x":
        remainder =  (i * j) % group_size
      elif operator == "+":
        remainder =  (i + j) % group_size

      columns.append(remainder)

    cayley_table.append(columns)

  displayTable(group, operator, group_size, cayley_table)
  
  return cayley_table

def displayTable(group_used, operator, group_size, cayley_table):
  '''Displays the created Cayley Table
  
    :param group_used: the group used to generate the table
    :type group_user: array
    :param operator: operation used to generate table
    :type operator: string
    :param group_size: size of group used
    :type group_size: int
    :param cayley_table: the generated cayley table
    :type cayley_table: a two dimensional array
  '''
  header = "{}{} | {}" .format(operator,group_size, group_used)
  print header
  
  for i in range(0, len(group_used)):
    display_row = "  {} | {}".format(group_used[i], cayley_table[i])
    print display_row 

def main():
  #accpets two inputs "u" or "z"
  group_type = sys.argv[1]
  
  #size of group, normally know as n in math
  group_size = int(sys.argv[2])
  
  #operator used when generating the table, current support is "x" and "+"
  operator = sys.argv[3]

  #creates and displays a cayley table based on inputed parameters
  createTable(group_type, group_size, operator)

if __name__ == "__main__":
  main()