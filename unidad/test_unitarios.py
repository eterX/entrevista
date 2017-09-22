import unittest
import unidad

def requerimiento1_1(entrada):
    """
    Requerimiento_1_1:But for multiples of three print "Fizz" instead of the number For numbers which are multiples of
    both three and five print "FizzBuzz".

    return: bool (OK?)
    """
    if entrada % 3 != 0:
        raise ValueError("La entrada de este test tiene que se múltiplo de 3")
    elif entrada % 5 == 0:
        mistr="FizzBuzz"
    else:
        mistr="Fizz"

    return unidad.unidad(entrada) == mistr

def requerimiento1_2(entrada):
    """
  Requerimiento_1_2: and for the multiples of five print "Buzz". For numbers which are multiples of both three and five
                        print "FizzBuzz".

    return: bool (OK?)
    """
    if entrada % 5 != 0:
        raise ValueError("La entrada de este test tiene que se múltiplo de 3")
    elif entrada % 3 == 0:
        mistr="FizzBuzz"
    else:
        mistr="Buzz"

    return unidad.unidad(entrada) == mistr

print("|ejecuto|salida|ok/error|")
print("|---|---|---|")

class prueba(unittest.TestCase):
    def test_rq11(self):
        """
            rq1_1 contra multiplos de 3
        """
        for i in range(1,6):
            entrada=i*3
            print("|unidad.unidad({})|{}|".format(entrada,unidad.unidad(entrada)),end="")
            try:
                self.assertTrue(requerimiento1_1(entrada))
            except Exception as e: print("{}|".format(e))
            else: print("OK|")

    def test_rq12(self):
        """
            rq1_2 contra multiplos de 5
        """
        for i in range(1,4):
            entrada=i*5
            print("|unidad.unidad({})|{}|".format(entrada,unidad.unidad(entrada)),end="")
            try:
                self.assertTrue(requerimiento1_2(entrada))
            except Exception as e: print("{}|".format(e))
            else: print("OK|")

    def test_rq1(self):
        """
            Requerimiento_1: Write a program that prints the numbers
        """
        for i in range(1,16): #son primos qué causalidad, pruebo hasta 15  es como probar hasta \infty... no?
            if ( i % 5 >  i % 3 > 0):
                print("|unidad.unidad({})|".format(i),end="")
                try:
                    self.assertEqual(unidad.unidad(i),str(i))
                    print("{}|".format(unidad.unidad(i)),end="")
                except Exception as e: print("{}|".format(e))
                else: print("OK|")


