# Quine-McCluskey-Algorithm

# Installation and Run

  1. Clone or download this repository 

  2. Install dependencies
   + pip3 install -r requirements.txt
  
  3. Run file by terminal or cmd 
   + python3.6 GUI.py 
 
 # Examples of output
  
  + Example 1:
  
  ![Example 1](https://github.com/congdaoduy298/Quine-McCluskey-Algorithm/blob/master/image/Screenshot%20from%202020-05-09%2000-46-30.png)
    
    How many variables you want to use ?
      5
    
      {0: 1, 1: 2, 2: 4, 3: 8, 4: 16} # dictionary 2^k 
    
    List number ...
  
      0 1 16 17 22 23  
    
    Step 1:
  
      (0, 1) 0000-
    
      (0, 16) -0000
    
      (1, 17) -0001
    
      (16, 17) 1000-
      
      (22, 23) 1011-
    
    Step 2:
    
      (0, 1, 16, 17) -000-
    
      (22, 23) 1011-
    
    Step 3:
    
      (0, 1, 16, 17) -000-
    
      (22, 23) 1011-
    
    Final Result : Y = bcd+AbCD
  
   + Example 2:
   ![Example 2](https://github.com/congdaoduy298/Quine-McCluskey-Algorithm/blob/master/image/Screenshot%20from%202020-05-09%2000-46-45.png)
  
 ![Example 2](https://github.com/congdaoduy298/Quine-McCluskey-Algorithm/blob/master/image/Screenshot%20from%202020-05-09%2000-52-37.png)
  
 ![Example 2](https://github.com/congdaoduy298/Quine-McCluskey-Algorithm/blob/master/image/Screenshot%20from%202020-05-09%2000-52-39.png)
  
  
    How many variables you want to use ?
  
      4
    
      {0: 1, 1: 2, 2: 4, 3: 8}
    
    List number ... 
  
      2 3 6 7 12 13 14 15 
    
    Step 1:
    
      (2, 3) 001-
    
      (2, 6) 0-10
    
      (3, 7) 0-11
    
      (6, 7) 011-
    
      (6, 14) -110
    
      (7, 15) -111
    
      (12, 13) 110-
    
      (12, 14) 11-0
    
      (13, 15) 11-1
      
      (14, 15) 111-
    
    Step 2:
    
      (2, 3, 6, 7) 0-1-
    
      (6, 7, 14, 15) -11-
      
      (12, 13, 14, 15) 11--
    
    Step 3:
    
      (2, 3, 6, 7) 0-1-
      
      (6, 7, 14, 15) -11-
    
      (12, 13, 14, 15) 11--
    
    Final Result : Y = aC+AB
