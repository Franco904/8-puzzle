from src.models.puzzle import Puzzle

if __name__ == '__main__':
    Puzzle().start_search()

'''
    - Transformar estado em tuple ok
    - Visited_Staes virar dicionário no formato tupla : objeto
    - reimplementar open_States com duplicação dos dados em um set - jeito mais fácil
        - Verificar forma de melhorar depois. Reverse lookup funciona?

'''