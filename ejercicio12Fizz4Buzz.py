# ---
# Write a program that prints the numbers from 1 to 100. But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".


def unidad(mival):
    """

    return: str según enunciado
    """
    mistr=""
    if mival % 3 == 0:
        mistr="Fizz"
    if mival % 5 == 0:
        mistr+="Buzz"

    if mistr != "":
        result=mistr
    else:
        result=str(mival)

    return result


import unittests


class prueba(unittests.TestCase):
    def enunciado1(entrada,salida):
        """
        pruyeba contra multiplo de 3
        return: bool (OK?)
        """
        return entrada % 3 == 0

    def enunciado2(entrada,salida):
        """
        pruyeba contra multiplo de 5
        return: bool (OK?)
        """
        return entrada % 5 == 0

    def enunciado3(entrada,salida):
        """
        pruyeba contra número no múltiplo de (3 o 5)
        return: bool (OK?)
        """
        return entrada % 5 == 0



    def test_entrevista():

        self.assertTrue( enunciado1(linea) && enunciado2(linea) && enunciado3(linea))



