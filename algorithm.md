# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
1. prompt user to enter package type "Enter your package type:"
2. case correct package type given
3. While package type does not equal purple or green or blue:
   1. Prompt user to Enter a valid package type "Enter a valid package type."
4. Check if package type is 'green'    
   1. price is 49.99 a month  
   2. if GB is greater than 2:   
      1. subtract 2 from GB used 
      2. price = price + 15 * GB used 
      3. prompt user to enter if they have a coupon   
      4. check if user entered 'yes' and if price is greater than 75
         1. if true price = price - 20  
5. check if package is 'blue' 
   1. set price to 70
   2. check if gb used is greater than 4
      1. subtract 4 from GB used
      2. price = price + 10 * GB used
6. check if package is 'purple'
   1.  set price to 99.95
7. Output Price and GB used to user "Your total is _. You used _GB."



