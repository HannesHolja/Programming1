import usefulFunctions as use
import time

def main():
   use.greetingsjokeri()
   numbers = use.randomnumberlist()
   for i in range(1,8):
        print("And here goes the {} number.....".format(use.nameofnumber(i)))
        time.sleep(1)
        print("And it's number {0}!".format(numbers[i-1]))
        time.sleep(1)
   print("And the line is: ", end='')
   for number in numbers:
        print(int(number), end=' ')

main()
