![](https://img.shields.io/github/repo-size/FIAPON/fiap-aprendizado-reforco)
![](https://img.shields.io/github/issues/FIAPON/fiap-aprendizado-reforco)
![](https://img.shields.io/github/watchers/FIAPON/fiap-aprendizado-reforco)
![](https://img.shields.io/github/last-commit/FIAPON/fiap-aprendizado-reforco)


# Aprendizado por Reforço  
## MBA em Inteligência Artificial & Machine Learning — FIAP

---

## Visão Geral da Disciplina

O **Aprendizado por Reforço (Reinforcement Learning – RL)** é um dos pilares da Inteligência Artificial moderna, especialmente em problemas onde **decisões precisam ser tomadas em sequência**, sob incerteza e com feedback atrasado.

Nesta disciplina, o foco não é apenas *“fazer o agente aprender”*, mas **entender como decisões são formuladas, avaliadas e otimizadas ao longo do tempo**, conectando teoria matemática, implementação prática e aplicações reais em negócios, engenharia e sistemas autônomos.

---

## Notebooks das aulas

### 1 - Tic-Tac-Toe: Aprendizado por Reforço Simples

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/tic-tae-toe/tic_tae_toe.ipynb)


### 2 - Grid World: Exemplo 1 - Pygame

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_1_pygame.ipynb)

### 3 - Frozen Lake: Exemplo 2 - OpenAI Gym

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_2_pygame_frozenlake.ipynb)

### 4 - Frozen Lake: Exemplo 3 - Determinístico

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_3_pygame_det_frozenlake_colab.ipynb)

### 5 - Equação de Bellman: Exemplo 4 - Value Iteration

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_5_bellman_resolvido.ipynb)

### 6 - Equação de Bellman: Exemplo 5 - Financeiro

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_6_bellman_fincaneiro.ipynb)

### 7 - MDP 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_6_pygame_mdp_colab.ipynb)

### 8 - Cadeia de Markov

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_7_cadeia_markov.ipynb)

### 9 - Q-Table

9.1 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_9_q_table_resolvido.ipynb)

9.2 - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_10_q_table_resolvido.ipynb)

11 - DQN Breakout

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/FIAPON/fiap-aprendizado-reforco/blob/main/Programas/exemplo_DQN_Breakout.ipynb)

---

## Abordagem Metodológica

- **Learning by doing**
- Aulas práticas com experimentos computacionais
- Ênfase em:
  - Raciocínio de decisão
  - Modelagem correta do problema
  - Interpretação crítica dos resultados
- Uso intensivo de simulações controladas

---

## Bibliografia e Materiais de Apoio

### Bibliografia Básica

- **Sutton, R. S., & Barto, A. G.**  
  *Reinforcement Learning: An Introduction (2nd Edition)*

- **Enes Bilgin**  
  *Mastering Reinforcement Learning with Python*

- **Ian Goodfellow, Yoshua Bengio, Aaron Courville**  
  *Deep Learning*

### Materiais Complementares

- David Silver (UCL / DeepMind) — Lectures  
- UC Berkeley — CS188  
- Coursera — *Fundamentals of Reinforcement Learning*  
- OpenAI — *Spinning Up in Deep RL*

---

## O que é Aprendizado por Reforço?

Aprendizado por Reforço é um paradigma de aprendizado de máquina baseado na **interação contínua entre um agente e um ambiente**, onde o agente aprende por **tentativa e erro**, buscando **maximizar uma recompensa acumulada ao longo do tempo**.

### Características principais

- O feedback não é imediato  
- O tempo importa  
- As ações atuais influenciam os dados futuros  

---

## Onde o Aprendizado por Reforço se Encaixa?

Dentro do aprendizado de máquina, o RL se diferencia por lidar explicitamente com:

- Tomada de decisão sequencial
- Planejamento
- Estratégia
- Trade-offs de curto vs. longo prazo

Ele dialoga com áreas como:

- Ciência da Computação
- Engenharia
- Matemática
- Economia
- Psicologia
- Neurociência

---

## Exemplos de Aplicação

### Jogos
- Atari
- AlphaGo
- Ambientes simulados complexos

### Robótica e Sistemas Autônomos
- Manipulação de objetos
- Navegação
- Controle motor

### Negócios e Indústria
- Supply Chain
- Planejamento de estoque
- Manutenção preditiva
- Alocação de recursos
- Estratégias financeiras

---

## Conceitos Fundamentais

### Elementos do Aprendizado por Reforço

- **Agente**: quem aprende e toma decisões  
- **Ambiente**: tudo que está fora do agente  
- **Estado (S)**: representação da situação atual  
- **Ação (A)**: decisão tomada pelo agente  
- **Recompensa (R)**: feedback numérico do ambiente  

---

## Tomada de Decisão Sequencial

Em cada passo de tempo:

1. O agente observa o estado  
2. Executa uma ação  
3. Recebe uma recompensa  
4. Transita para um novo estado  

Esse processo é naturalmente modelado como um **Processo de Decisão de Markov (MDP)**, onde:

> O futuro é independente do passado, dado o presente.

---

## Processo de Decisão de Markov (MDP)

Um MDP é definido por:

- Conjunto de estados  
- Conjunto de ações  
- Função de transição  
- Função de recompensa  
- Fator de desconto (γ)  

O objetivo do agente é aprender uma **política ótima** que maximize o retorno esperado.

---

## Políticas e Funções de Valor

### Política
- Define como o agente escolhe ações
- Pode ser:
  - Determinística
  - Estocástica

### Função de Valor
- **V(s)**: valor de um estado  
- **Q(s, a)**: valor de uma ação em um estado  

Essas funções guiam o processo de decisão.

---

## Equação de Bellman

A Equação de Bellman formaliza a ideia central do RL:

> O valor de uma decisão hoje depende das recompensas futuras esperadas.

Ela permite:

- Planejamento
- Avaliação de políticas
- Aprendizado incremental

---

## Q-Learning

O **Q-Learning** é um algoritmo:

- Livre de modelo (*model-free*)
- Baseado em diferença temporal
- Aprende diretamente a função **Q(s, a)**

### Características
- Atualização iterativa
- Uso de exploração vs. explotação
- Base de muitos algoritmos modernos de RL

---

## Exploração vs. Explotação

Um dos dilemas centrais do RL:

- **Explorar**: testar ações desconhecidas  
- **Explotar**: usar o que já funciona  

A política **ε-greedy** equilibra esse trade-off de forma simples e eficaz.

---

## Living Penalty

Introduz-se uma penalidade por tempo:

- Incentiva soluções eficientes
- Evita comportamentos procrastinadores
- Fundamental em ambientes reais

---

## Deep Reinforcement Learning

Quando o espaço de estados cresce:

- Q-tables deixam de ser viáveis  
- Redes neurais passam a aproximar funções de valor  

Surge o **Deep Q-Network (DQN)**:

- Combina RL + Deep Learning  
- Usa replay de experiências  
- Resolve problemas complexos e de alta dimensionalidade  

