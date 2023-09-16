"""
#* Casos de teste
#* case1: Fácil: (1,2,3,4,9,5,7,8,6) - 2
#* case2: Médio: (9,3,1,4,6,2,8,7,5)- 10
#* case3: Médio: (2,3,7,1,5,4,8,6,9) - 12
#* case4: Difícil: (7,8,4,5,6,1,9,3,2) - 18
#* case5: Difícil: (7,6,5,8,9,4,3,1,2 )  - 20

Fornecidos pelo professor:

case6: (4,7,5,9,2,1,3,6,8) - 27 passos - em sala
case7: (6, 7, 5, 1, 2, 3, 9, 4, 8) - 18 passos  - slide
case8: (3, 1, 8, 5, 6, 2, 7, 4, 9) - 24 passos - slide
"""

"""

- Como utilizar:

  Este é o arquivo de configuração do programa. Ele permite definir dois parâmetros para a execução: o tipo de heurística utilizado e o estado inicial.

  A definição dos parâmetros deve observar as seguintes regras:

  - INITIAL_STATE:

    - Informa um estado inicial para a execução do programa (ou seja, qual a configuração inicial do tabuleiro do 8-puzzle)
    - Deve ser definido como uma tupla com 9 elementos, a qual é "enxergada" pelo programa como uma matriz 3x3. Por exemplo, a tupla (7,8,4,5,6,1,9,3,2)
      representa o tabuleiro:

          7 8 4
          5 6 1
            3 2

    - Cada elemento deve ser um número inteiro entre 1 e 9
    - Conforme exemplo, os inteiros informados na tupla representam o número do "bloco" no tabuleiro do jogo, com exceção do número 9, que representa o bloco vazio.
    - Não é realizada nenhuma validação da configuração informada, cabendo ao usuário certificar-se de que inseriu uma configuração válida.

  - HEURISTIC:

    - Informa ao programa qual heurística deve ser utilizada, conforme a legenda:

      - 0 (ou qualquer número diferente de 1 e 2): Não utiliza heurística
      - 1: Utiliza heurística simples
      - 2: Utiliza heurística mais precisa (avançada) 

"""
  
SETTINGS = {
  "HEURISTIC": 1,
  "INITIAL_STATE": (3, 1, 8, 5, 6, 2, 7, 4, 9)
}