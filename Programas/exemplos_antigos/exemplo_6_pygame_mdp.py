import numpy as np
import pygame
import sys

# Definindo o labirinto
# 0: espaço vazio
# 1: parede
# 9: objetivo
maze = np.array([
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 9, 1],
    [1, 1, 1, 1, 1, 1]
])

num_rows, num_cols = maze.shape
V = np.zeros((num_rows, num_cols))

gamma = 0.9

# Inicializando o Pygame
pygame.init()

# Configurações da janela
cell_size = 50
width, height = num_cols * cell_size, num_rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MDP Calculation")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# Fonte para renderizar texto
font = pygame.font.Font(None, 36)

# Função para desenhar o labirinto com os valores atuais
def draw_maze_with_values():
    screen.fill(black)
    for row in range(num_rows):
        for col in range(num_cols):
            if maze[row, col] == 1:
                pygame.draw.rect(screen, gray, (col * cell_size, row * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, white, (col * cell_size, row * cell_size, cell_size, cell_size), 2)
                if maze[row, col] != 1:
                    value = V[row, col]
                    color_value = min(int(value * 255), 255)
                    pygame.draw.circle(screen, (0, color_value, 0), (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 3)

                    # Renderiza o valor na posição do estado
                    text = font.render(f'{value:.2f}', True, white)
                    text_rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                    screen.blit(text, text_rect)

# Função para calcular o valor de um estado usando a fórmula do MDP
def calculate_value(state, action):
    row, col = state
    if maze[row, col] == 9:  # Objetivo
        return 1
    if maze[row, col] == 1:  # Parede
        return 0

    next_state = (row, col)
    if action == 'up':
        next_state = (max(row - 1, 0), col)
    elif action == 'down':
        next_state = (min(row + 1, num_rows - 1), col)
    elif action == 'left':
        next_state = (row, max(col - 1, 0))
    elif action == 'right':
        next_state = (row, min(col + 1, num_cols - 1))


    # gamma: Este é o fator de desconto. Ele penaliza recompensas futuras, dando mais importância a recompensas imediatas. O valor de gamma deve estar entre 0 e 1.
    
    # 0.8: Este é o fator de transição para o estado seguinte quando a ação é executada. 
    #      No contexto de um MDP, uma ação não garante uma transição direta para o próximo estado devido à natureza estocástica do ambiente. 
    #      Neste caso, assume-se que há 80% de probabilidade de que o agente vá para o próximo estado após executar a ação.
        
    # V[next_state[0], next_state[1]]: Este termo representa o valor estimado do próximo estado. 
    #                                  next_state é a tupla que representa as coordenadas do próximo estado. 
    #                                  V é a função de valor, que atribui um valor a cada estado com base nas recompensas esperadas.
    
    # 0.2 * V[row, col]: Este termo representa uma "tentativa" de transição para o mesmo estado após a ação. 
    #                    Novamente, reflete a natureza estocástica do ambiente, onde há uma probabilidade de 20% de permanecer no mesmo estado.

    action_value = gamma * (0.8 * V[next_state[0], next_state[1]] + 0.2 * V[row, col])
    print(f'Estado: {state}, Ação: {action}, Valor Calculado: {action_value:.2f}')
    return action_value

# Algoritmo de iteração de valor
iteration = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if maze[row, col] != 1:  # Ignorar paredes
                v = V[row, col]
                max_value = -float('inf')
                for action in ['up', 'down', 'left', 'right']:
                    action_value = calculate_value((row, col), action)
                    if action_value > max_value:
                        max_value = action_value
                V[row, col] = max_value
                delta = max(delta, abs(v - V[row, col]))

    # Explicação da iteração atual
    print(f'Iteração {iteration}: Delta (Maior diferença entre os valores): {delta}')

    # Desenha o labirinto com os valores atuais
    draw_maze_with_values()

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do jogo
    clock.tick(1)

    iteration += 1

    if delta < 1e-2:
        break
