"""
Try-except-else-finally
Try is the keyword which is used to keep the code segment under check
except- segment used to handle the exceptions after catching it
else- runs this when no exception exists
finally- no matter what run this code if/if not for exceptions
"""
# Example 1
try:
    print(x)
except NameError:     # error wont be shown if the error is NameError.........and this message is displayed
    print("Your variable x is not defined")
except ZeroDivisionError:              # This error is not occured.....and msg is not displaye
           print("Cannot divide by 0")
finally:
    print(1)
"""
output:
Your variable x is not defined
1
"""
# Example 2
try:
           print('1'+1)
           print(sum)
           print(1/0)
except NameError:
           print("sum does not exist")
except ZeroDivisionError:
           print("Cannot divide by 0")
except:
           print("Something went wrong")
"""
Output:
Something went wrong
"""
# Example 3
try:
       print(1/0)
except ZeroDivisionError:
       raise
finally:
       print("Okay")
print("Bye")
