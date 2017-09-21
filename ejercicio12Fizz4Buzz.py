# ---
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


for mival in range(1,101):
    mistr=""
    if mival % 3 == 0:
        mistr="Fizz"
    if mival % 5 == 0:
        mistr+="Buzz"

    if mistr != "":
        print(mistr)
    else:
        print(str(mival))
