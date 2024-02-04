import pygame
import sys
import random
import matplotlib.pyplot as plt
import pickle

class QLearningEnvironment:
    """
    Classe que implementa um ambiente de grade para o algoritmo Q-Learning.
    """

    def __init__(self):
        """
        Inicializa a classe QLearningEnvironment com os parâmetros padrão do ambiente.
        """
        # Parâmetros do ambiente
        self.grid_width = 12
        self.grid_height = 4
        self.cell_size = 30
        self.fps = 5
        self.total_rewards = []

        # Definição dos estados especiais
        self.start_state = (0, self.grid_height - 1)
        self.goal_state = (self.grid_width - 1, self.grid_height - 1)
        self.cliff_state = [(i, self.grid_height - 1) for i in range(1, self.grid_width - 1)]

        # Ações possíveis
        self.actions = ["UP", "DOWN", "LEFT", "RIGHT"]

        # Inicialização do ambiente gráfico com Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((self.grid_width * self.cell_size, self.grid_height * self.cell_size))
        self.clock = pygame.time.Clock()

    def draw_gridworld(self, agent_pos):
        """
        Desenha o ambiente da grade com o agente na posição especificada.

        :param agent_pos: Posição do agente na forma (x, y).
        """
        # Limpa a tela
        self.screen.fill((255, 255, 255))

        # Desenha cada célula da grade
        for x in range(self.grid_width):
            for y in range(self.grid_height):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)

                # Define cores para diferentes estados
                if (x, y) not in [self.start_state, self.goal_state] and (x, y) not in self.cliff_state:
                    pygame.draw.rect(self.screen, (200, 200, 200), rect)
                elif (x, y) == self.start_state:
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)
                elif (x, y) == self.goal_state:
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)
                elif (x, y) in self.cliff_state:
                    pygame.draw.rect(self.screen, (0, 0, 255), rect)

                # Desenha o agente como um círculo
                if (x, y) == agent_pos:
                    pygame.draw.circle(self.screen, (0, 0, 0),
                                       (x * self.cell_size + self.cell_size // 2, y * self.cell_size + self.cell_size // 2),
                                       self.cell_size // 3)

        # Atualiza a tela
        pygame.display.flip()

    def take_action(self, state, action):
        """
        Executa uma ação no ambiente e retorna o próximo estado.

        :param state: Estado atual na forma (x, y).
        :param action: Ação a ser tomada ("UP", "DOWN", "LEFT" ou "RIGHT").
        :return: Próximo estado após a ação.
        """
        x, y = state

        # Move o agente com base na ação escolhida
        if action == "UP" and y > 0:
            return x, y - 1
        elif action == "DOWN" and y < self.grid_height - 1:
            return x, y + 1
        elif action == "LEFT" and x > 0:
            return x - 1, y
        elif action == "RIGHT" and x < self.grid_width - 1:
            return x + 1, y
        else:
            return x, y

    def q_learning(self):
        """
        Implementação do algoritmo Q-Learning para treinar o agente no ambiente.
        """
        # Inicialização da função Q com valores arbitrários
        Q = {(x, y): {action: 0 for action in self.actions} for x in range(self.grid_width) for y in range(self.grid_height)}

        # Parâmetros do algoritmo
        alpha = 0.1
        gamma = 1.0
        epsilon = 0.1

        episode_steps = []

        # Loop de episódios de treinamento
        for episode in range(2000):
            state = self.start_state
            total_reward = 0

            # Loop de passos dentro de um episódio
            while state != self.goal_state:
                # Escolhe a ação com base na política epsilon-greedy
                action = max(Q[state], key=Q[state].get) if random.uniform(0, 1) > epsilon else random.choice(self.actions)

                # Executa a ação e obtém o próximo estado
                next_state = self.take_action(state, action)

                # Define a recompensa com base no próximo estado
                if next_state in self.cliff_state:
                    reward = -100
                    next_state = self.start_state
                else:
                    reward = -1

                # Atualiza a função Q com base na equação Q-Learning
                max_next_action_value = max(Q[next_state].values()) if Q[next_state] else 0
                Q[state][action] += alpha * (reward + gamma * max_next_action_value - Q[state][action])

                total_reward += reward
                state = next_state

                # Desenha o ambiente para visualização
                self.draw_gridworld(state)

                # Imprime informações sobre o episódio
                print(f"Episódio: {episode + 1}, Passos: {total_reward}, Q({state}): {Q[state]}")

                # Aguarda um curto intervalo e verifica eventos (como fechar a janela)
                pygame.time.delay(300)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

            # Armazena a recompensa total do episódio
            self.total_rewards.append(total_reward)

            episode_steps.append(total_reward)

            # A cada 10 episódios, imprime a função Q
            if episode % 10 == 0:
                print("\nFunção Q:")
                for y in range(self.grid_height):
                    for x in range(self.grid_width):
                        action_values = Q[(x, y)]
                        print(f"({x}, {y}): {action_values}    ", end="")
                    print()
                print("\n" + "=" * 80)

            # Aguarda um intervalo maior a cada 100 episódios
            pygame.time.delay(1000)

            # A cada 100 episódios, salva o modelo treinado
            if episode % 100 == 0:
                with open('q_learning_model.pkl', 'wb') as file:
                    pickle.dump(Q, file)

            # Plota a recompensa total por episódio
            self.plot_total_reward()
            plt.show()

    def plot_total_reward(self):
        """
        Plota o gráfico da recompensa total por episódio.
        """
        plt.plot(range(1, len(self.total_rewards) + 1), self.total_rewards, marker='o', linestyle='-', color='g')
        plt.title('Recompensa Total por Episódio')
        plt.xlabel('Episódio')
        plt.ylabel('Recompensa Total')
        plt.show()

    def load_and_run_episode(self):
        """
        Carrega o modelo treinado e executa um episódio sem treinamento.
        """
        with open('q_learning_model.pkl', 'rb') as file:
            Q_loaded = pickle.load(file)

        state = self.start_state

        while state != self.goal_state:
            # Escolhe a ação com base na política greedy
            action = max(Q_loaded[state], key=Q_loaded[state].get)
            
            # Executa a ação e obtém o próximo estado
            next_state = self.take_action(state, action)

            self.draw_gridworld(state)

            # Imprime informações sobre o episódio carregado
            print(f"Estado: {state}, Ação: {action}, Próximo Estado: {next_state}")

            pygame.time.delay(300)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            state = next_state


# Criar uma instância da classe e executar o Q-Learning
env = QLearningEnvironment()
env.q_learning()

# Executar a função para carregar o modelo e executar um episódio
env.load_and_run_episode()
sys.exit()
