import numpy as np
import pygame
import sys

# Definindo o tamanho do ambiente (tabuleiro 2D)
n_rows, n_cols = 4, 4

# Criando o mapa FrozenLake (0 para caminhos livres, 1 para buracos, 2 para o objetivo)
frozen_lake_map = np.array([
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 1, 0, 2]
])

# Inicializando o Pygame
pygame.init()

# Configurações da janela
cell_size = 50
width, height = n_cols * cell_size, n_rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("FrozenLake Game")

# Cores
white = (255, 255, 255)
blue = (135, 206, 250)
red = (255, 0, 0)
green = (0, 255, 0)

# Função para desenhar o tabuleiro do FrozenLake
def draw_frozen_lake():
    for row in range(n_rows):
        for col in range(n_cols):
            if frozen_lake_map[row, col] == 0:
                color = white
            elif frozen_lake_map[row, col] == 1:
                color = blue
            elif frozen_lake_map[row, col] == 2:
                color = green
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Função para desenhar o agente (bola)
def draw_agent(agent_position):
    pygame.draw.circle(screen, red, (agent_position[1] * cell_size + cell_size // 2, agent_position[0] * cell_size + cell_size // 2), cell_size // 4)

# Função para movimentar o agente com base na ação
def move_agent(current_position, action):
    if action == 'down' and current_position[0] < n_rows - 1:
        current_position[0] += 1
    elif action == 'up' and current_position[0] > 0:
        current_position[0] -= 1
    elif action == 'left' and current_position[1] > 0:
        current_position[1] -= 1
    elif action == 'right' and current_position[1] < n_cols - 1:
        current_position[1] += 1


# Definindo a posição inicial do agente
agent_position = [0, 0]

# Loop principal do jogo
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_agent(agent_position, 'up')
            elif event.key == pygame.K_DOWN:
                move_agent(agent_position, 'down')
            elif event.key == pygame.K_LEFT:
                move_agent(agent_position, 'left')
            elif event.key == pygame.K_RIGHT:
                move_agent(agent_position, 'right')

    # Verifica se o agente caiu em um buraco ou atingiu o objetivo
    if frozen_lake_map[agent_position[0], agent_position[1]] == 1:
        print("O agente caiu em um buraco! Reiniciando o jogo...")
        agent_position = [0, 0]
    elif frozen_lake_map[agent_position[0], agent_position[1]] == 2:
        print("O agente alcançou o objetivo! Reiniciando o jogo...")
        agent_position = [0, 0]

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha o tabuleiro do FrozenLake e o agente
    draw_frozen_lake()
    draw_agent(agent_position)

    # Atualiza a tela
    pygame.display.flip()

    # Controla a velocidade do jogo
    pygame.time.delay(500)

# Finaliza o Pygame
pygame.quit()
sys.exit()
