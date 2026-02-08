import pygame
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

# Inicialização do Pygame
pygame.init()

# Definição de cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BUTTON_COLOR = (100, 100, 255)
BUTTON_HOVER_COLOR = (150, 150, 255)

# Configurações da tela
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BUTTON_WIDTH = 150
BUTTON_HEIGHT = 50
BUTTON_RADIUS = 10
BUTTON_SPACING = 20

# Número de braços (botões)
K = 5

# Médias e desvios padrão para as distribuições de recompensa de cada braço
reward_means = np.random.uniform(low=0, high=1, size=K)
reward_std = 0.1  # Desvio padrão comum para todas as distribuições

# Função para gerar uma recompensa com base na distribuição de recompensa do braço
def pull_arm(arm):
    lower_bound = 0  # Limite inferior
    upper_bound = 1  # Limite superior
    mean = reward_means[arm]  # Média da distribuição
    std = reward_std  # Desvio padrão da distribuição
    # Gera uma distribuição normal truncada com os parâmetros especificados
    return truncnorm.rvs((lower_bound - mean) / std, (upper_bound - mean) / std, loc=mean, scale=std)

# Função para desenhar os botões na tela
def draw_buttons(screen):
    button_font = pygame.font.Font(None, 24)
    for i in range(K):
        button_rect = pygame.Rect(BUTTON_SPACING, BUTTON_HEIGHT * i + BUTTON_SPACING * (i+1), BUTTON_WIDTH, BUTTON_HEIGHT)
        pygame.draw.rect(screen, GRAY, button_rect)
        pygame.draw.rect(screen, BUTTON_COLOR, button_rect.inflate(-6, -6), border_radius=BUTTON_RADIUS)
        button_text = button_font.render(f'Arm {i+1}', True, BLACK)
        screen.blit(button_text, (button_rect.centerx - button_text.get_width() / 2,
                                  button_rect.centery - button_text.get_height() / 2))

# Função principal
def main():
    # Configuração da tela
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("k-Armed Bandit")

    reward_text = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Verifica se foi clicado com o botão esquerdo do mouse
                    x, y = event.pos
                    for i in range(K):
                        button_rect = pygame.Rect(BUTTON_SPACING, BUTTON_HEIGHT * i + BUTTON_SPACING * (i+1), BUTTON_WIDTH, BUTTON_HEIGHT)
                        if button_rect.collidepoint(x, y):
                            reward = pull_arm(i)
                            reward_text = f'Reward: {reward:.2f}'
                            reward_font = pygame.font.Font(None, 24)
                            reward_surface = reward_font.render(reward_text, True, BLACK)
                            reward_rect = reward_surface.get_rect()
                            reward_rect.topleft = (button_rect.right + BUTTON_SPACING, button_rect.centery - reward_rect.height / 2)
                            break
                    # Verifica se o clique foi no botão do menu
                    if SCREEN_WIDTH - 120 <= x <= SCREEN_WIDTH - 20 and 20 <= y <= 70:
                        plot_distributions()

        screen.fill(WHITE)
        draw_buttons(screen)
        if reward_text:
            screen.blit(reward_surface, reward_rect)
        draw_menu(screen)
        pygame.display.flip()

    pygame.quit()

# Função para desenhar o menu
def draw_menu(screen):
    menu_rect = pygame.Rect(SCREEN_WIDTH - 120, 20, 100, 50)
    pygame.draw.rect(screen, GRAY, menu_rect)
    pygame.draw.rect(screen, BUTTON_COLOR, menu_rect.inflate(-6, -6), border_radius=BUTTON_RADIUS)
    menu_font = pygame.font.Font(None, 24)
    menu_text = menu_font.render("Menu", True, BLACK)
    screen.blit(menu_text, (menu_rect.centerx - menu_text.get_width() / 2,
                            menu_rect.centery - menu_text.get_height() / 2))

# Função para plotar a distribuição das probabilidades em um gráfico do tipo violino
def plot_distributions():
    plt.figure(figsize=(8, 6))
    for i, mean in enumerate(reward_means):
        lower_bound = 0
        upper_bound = 1
        std = reward_std
        samples = truncnorm.rvs((lower_bound - mean) / std, (upper_bound - mean) / std, loc=mean, scale=std, size=1000)
        plt.violinplot(samples, positions=[i], showmeans=False, showextrema=False, showmedians=True)
    plt.xlabel('Arms')
    plt.ylabel('Reward Distribution')
    plt.title('Reward Distribution for Each Arm')
    plt.grid(True)
    plt.xticks(np.arange(0, K))
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
