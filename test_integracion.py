import unittest
import ejercicio12Fizz4Buzz as e
import os

salida="ejercicio12Fizz4Buzz-out.txt"
salida_lineas=100
num_min=1
num_max=salida_lineas
print("|ejecuto|salida|ok/error|")
print("|---|---|---|")


class SistemaCompleto(unittest.TestCase):
    def test_file(self):
        process = os.popen('python3 ejercicio12Fizz4Buzz.py >{file}'.format(file=salida))
        process.close()
        print("|test_file()|{}|OK|".format(salida))

    def test_lineas(self):
        lineas=0
        mifile=open(salida,mode="r")
        for linea in mifile:
            linea=linea.strip("\n")
            lineas+=1
            try:
                linea=int(linea)
                if linea > num_max or linea < num_min:
                    raise Exception("Numero fuera de rango")
            except ValueError as e:
                if not (linea in ['Buzz','Fizz','FizzBuzz']):
                        raise Exception("Ni número ni palabra clave: {}".format(linea))
            except Exception as e: raise

        self.assertEqual(lineas,salida_lineas,"largo de archivo incorrecto") # cantidad correcta?


        mifile.close()
        print("|test_lineas()|{}|OK|".format(salida))
