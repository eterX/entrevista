# ---
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


migen = ( x for x in range(1,101))

while True:
    try:
        mival=next(migen)
        mistr=""
        if mival % 3 == 0:
            mistr="Fizz"
        if mival % 5 == 0:
            mistr+="Buzz"

        if mistr != "":
            print(mistr)
        else:
            print(str(mival))
    except StopIteration: break
    except Exception as e:
        print("Excepción no relacionada con el generador: {}".format(e))
