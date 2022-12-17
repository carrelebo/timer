#code by Benstitou Sofiane : 17/12/2022

import os
import time

"""
base :

 ......
.      .
.      .
.      .
 ...... 
.      .
.      .
.      .
 ...... 

You can adjust pixel by color with os and ANSI code

+

Use numpy marix to concatenate numbers display.
"""

def zero():
  return """
 ......
.      .
.      .
.      .
      
.      .
.      .
.      .
 ...... 
  """

def one():
    return """
 
       .
       .
       .
      
       .
       .
       .
  
  """

def two():
  return """
 ......
       .
       .
       .
 ...... 
.       
.       
.       
 ...... 
  """
  
def three():
  return """
 ......
       .
       .
       .
 ...... 
       .
       .
       .
 ...... 
  """
  
def four():
  return """
 
.      .
.      .
.      .
 ...... 
       .
       .
       .
  
  """
  
def five():
  return """
 ......
.      
.      
.      
 ...... 
       .
       .
       .
 ...... 
  """
  
def six():
  return """
 ......
.      
.      
.      
 ...... 
.      .
.      .
.      .
 ...... 
  """
  
def seven():
  return """
 ......
.      .
.      .
.      .
  
       .
       .
       .
  
  """
  
def eight():
  return """
 ......
.      .
.      .
.      .
 ...... 
.      .
.      .
.      .
 ...... 
  """
  
def nine():
  return """
 ......
.      .
.      .
.      .
 ...... 
       .
       .
       .
 ...... 
  """
  
#exemple of program (timer) :
t = 0

while t < 10:
  if t == 0:
    print(zero())
  
  elif t == 1:
    print(one())
  
  elif t == 2:
    print(two())
  
  elif t == 3:
    print(three())
  
  elif t == 4:
    print(four())
  
  elif t == 5:
    print(five())
    
  
  elif t == 6:
    print(six())
    
  
  elif t == 7:
    print(seven())
    
  elif t == 8:
    print(eight())
    
  elif t == 9:
    print(nine())

  t += 1
  time.sleep(1)
  os.system("clear")
