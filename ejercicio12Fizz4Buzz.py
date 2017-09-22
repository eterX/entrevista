# ---
# Requerimiento_1: Write a program that prints the numbers from 1 to 100.
# Requerimiento_1_1:But for multiples of three print "Fizz" instead of the number For numbers which are multiples of both three and five print "FizzBuzz".
#  Requerimiento_1_2: and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

import unidad as u

def ejercicio():
    migen = ( x for x in range(1,101))

    while True:
        try:
            mival=next(migen)
            print(u.unidad(mival))
        except StopIteration: break
        except Exception as e:
            print("Excepción no relacionada con el generador: {}".format(e))


if __name__ == '__main__':
    ejercicio()