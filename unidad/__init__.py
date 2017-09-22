__all__=['unidad']



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


if __name__ == '__main__':
    print("paquete para ejercicio12Fizz4Buzz, no para correr directamente. Tests en tests_unidad.py")