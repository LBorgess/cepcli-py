import sys
from functions import *

if __name__ == '__main__':

    if not sys.argv[1:]:
        print('\nO argumento de CEP não foi informado' 
              'Execute o programa da seguinte forma:\n'      
              'python main.py \'cep\'\n'
              'Onde \'cep\' é o valor que deseja localizar\n')
    else:
        cep = (sys.argv[1])
        cep = cep.replace('-', '')

        if len(cep) != 8:
            print('\nO Formato e/ou comprimento do CEP informado está inválido\n')
        else:
            get_cep(cep)    