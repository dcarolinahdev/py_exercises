# -*- coding: utf-8 -*-

def run():
    """ print only even numbers """
    # for contador in range(50):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    """ exit the loop until 5 """
    # for i in range(10):
    #     print(i)
    #     if i == 5:
    #         break
    #    break
    
    """ exit the loop until char 'i' """
    texto = str(input('Escribe un texto: '))
    for letra in texto:
        if letra == 'i':
            break
        print(letra)


if __name__ == '__main__':
    run()
