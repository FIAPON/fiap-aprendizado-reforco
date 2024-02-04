import numpy as np
import pygame
import sys

# Definindo o tamanho do ambiente (tabuleiro 2D)
n_rows, n_cols = 5, 5

# Definindo o labirinto (1 para obstáculos, 0 para caminhos livres)
maze = np.array([
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0]
])

# Inicializando o Pygame
pygame.init()

# Configurações da janela
cell_size = 50
width, height = n_cols * cell_size, n_rows * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Agente em um Labirinto")

# Cores
white = (255, 255, 255)
blue = (135, 206, 250)
red = (255, 0, 0)

# Função para desenhar o labirinto
def draw_maze():
    for row in range(n_rows):
        for col in range(n_cols):
            color = white if maze[row, col] == 0 else blue
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

# Função para desenhar o agente (bola)
def draw_agent(agent_position):
    pygame.draw.circle(screen, red, (agent_position[1] * cell_size + cell_size // 2, agent_position[0] * cell_size + cell_size // 2), cell_size // 4)

# Função para movimentar o agente aleatoriamente
def take_random_action():
    return np.random.choice(['up', 'down', 'left', 'right'])

# Função para atualizar a posição do agente com base na ação
def update_position(current_position, action):
    if action == 'down' and current_position[0] > 0 and maze[current_position[0] - 1, current_position[1]] == 0:
        return [current_position[0] - 1, current_position[1]]
    elif action == 'up' and current_position[0] < n_rows - 1 and maze[current_position[0] + 1, current_position[1]] == 0:
        return [current_position[0] + 1, current_position[1]]
    elif action == 'left' and current_position[1] > 0 and maze[current_position[0], current_position[1] - 1] == 0:
        return [current_position[0], current_position[1] - 1]
    elif action == 'right' and current_position[1] < n_cols - 1 and maze[current_position[0], current_position[1] + 1] == 0:
        return [current_position[0], current_position[1] + 1]
    else:
        return current_position

# Número de passos que o agente dará
num_steps = 20

# Definindo a posição inicial do agente
agent_position = [0, 0]

# Loop principal do jogo
running = True
for step in range(num_steps):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimento aleatório do agente
    action = take_random_action()
    previous_position = agent_position
    agent_position = update_position(agent_position, action)

    # Limpa a tela
    screen.fill((0, 0, 0))

    # Desenha o labirinto e o agente
    draw_maze()
    draw_agent(agent_position)

    # Atualiza a tela
    pygame.display.flip()

    # Imprime a posição atual, ação tomada e posição final do agente
    print(f"Step: {step}, Ação: {action}, Posição atual: {previous_position}, Posição final: {agent_position}")

    # Controla a velocidade do jogo
    pygame.time.delay(500)

# Finaliza o Pygame
pygame.quit()
sys.exit()
