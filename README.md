# Reinforcement Learning MBA em Data Science & AI — FIAP

Bem-vindo ao **Reinforcement Learning**, o repositório oficial das aulas de **Aprendizado por Reforço (Reinforcement Learning – RL)** do **MBA da FIAP**.

Aqui você encontrará **notebooks práticos, experimentais e orientados a decisão**, cobrindo desde os fundamentos do RL clássico até uma introdução sólida ao **Deep Reinforcement Learning**, sempre conectando teoria, implementação e interpretação de resultados — exatamente como se espera em um MBA.

Os experimentos utilizam ambientes do **Gymnasium**, permitindo simular cenários controlados que representam problemas reais de negócio, engenharia e otimização.

**Professor:** Ms. Felipe Amaral

Abordagem prática, com foco em raciocínio estratégico, modelagem correta do problema e análise crítica dos resultados.

---

## Por que Reinforcement Learning importa para executivos e líderes em IA?

Reinforcement Learning é o **framework matemático por trás de decisões inteligentes em ambientes dinâmicos**, onde não existe resposta pronta — apenas consequências ao longo do tempo.

Ao final deste módulo, você será capaz de:
- Pensar problemas complexos como **processos de decisão sequencial**;
- Traduzir desafios reais em **MDPs (Markov Decision Processes)**;
- Entender como agentes aprendem **por tentativa, erro e feedback**;
- Avaliar quando RL faz sentido (e quando não faz);
- Ler artigos, discutir soluções e conversar tecnicamente com times de IA.

---

## Objetivos de Aprendizagem

Este material foi desenhado para que você consiga:

- Compreender o paradigma de **aprendizado por interação com o ambiente**;
- Modelar estados, ações, recompensas e políticas;
- Aplicar algoritmos clássicos como **Q-Learning**;
- Entender profundamente a **Equação de Bellman**;
- Evoluir naturalmente para **Deep Q-Networks (DQN)**;
- Rodar experimentos, analisar curvas de aprendizado e diagnosticar falhas do agente.

---

## Estrutura do Curso e do Repositório

### Aula 1 — Q-Learning na prática (Taxi Problem)
Notebook: `Aula1_Q_Learning_Taxi.ipynb`

- Fundamentos do Q-Learning  
- Exploração de estados, ações e recompensas  
- Evolução da Q-table  
- Impacto da exploração no aprendizado  

---

### Aula 2 — Bellman, Gridworld e FrozenLake
Notebooks:
- `Aula2_Bellman.ipynb`
- `Aula2_Grid_movements_RL.ipynb`
- `Aula2_Q_Learning_FrozenLakev1.ipynb`

- Equação de Bellman  
- Aprendizado por valor  
- Ambientes estocásticos  
- Exploração vs. explotação  

---

### Aula 3 — Deep Reinforcement Learning com DQN
Notebooks:
- `Aula3_DQN_Breakout.ipynb`
- `Aula3_DQN_LunarLander.ipynb`

- Limitações das Q-tables  
- Redes neurais como aproximadores  
- Deep Q-Networks  
- Ambientes complexos  

---

## Executando os Notebooks

### Opção 1 — Execução local (Jupyter)

```bash
git clone https://github.com/ahirtonlopes/Mastering-Reinforcement-Learning.git
cd Mastering-Reinforcement-Learning
```

```bash
python -m venv .venv
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
jupyter notebook
```

---

### Opção 2 — Google Colab

Recomendado para evitar problemas de ambiente local.

---

## Dependências

- gymnasium  
- numpy  
- matplotlib  
- tensorflow ou torch  

---

## Estratégia de Estudo

- Execute os notebooks em ordem  
- Ajuste hiperparâmetros  
- Analise curvas de recompensa  
- Questione o comportamento do agente  

---

## Próximos Passos

- SARSA  
- Policy Gradient  
- Actor-Critic  
- PPO  
- Casos de negócio  

---

## Licença

MIT License
