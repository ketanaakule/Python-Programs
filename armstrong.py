'''
Number of n digits which are equal to sum of nth power of its digits
'''
num = int(input("Enter a Number: "))

power = len(str(num))

result = 0

temp = num

while temp>0 :
      d = temp % 10
      result = result + d**power
      temp = temp // 10

if(result==num):
      print(num,"is Armstrong Number")
else:
      print(num,"is not Armstrong Number")


# Program to find Armstrong number in given range

'''
lower = int(input("Enter lower range: "))  
upper = int(input("Enter upper range: "))  
  
for num in range(lower,upper + 1):  
   sum = 0  
   temp = num  
   power = len(str(temp))
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** power  
       temp //= 10  

       if num == sum:  
            print(num)  
            
   '''               
            
