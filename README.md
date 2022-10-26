## Previsão de quantidade de vendas de jogos no mundo utilizando IA.

A IA consegue prever o quanto um jogo venderá no mundo (em milhões), utilizando de somente algumas informações, são elas:

- Gênero do jogo;
- Plataforma (consoles ou PC);
- Expectativa de venda no continente Norte Americano;
- Expectativa de venda no continente Europeu;

### Criação do modelo
Para o desenvolvimento do modelo de IA foi utlizado python e um dataset disponível no Kaggle que pode ser acessado [aqui](https://www.kaggle.com/datasets/gregorut/videogamesales).

No processo de desenvolvimento e treinamento da IA foi utilizado um modelo de Regressão Linear, utilizando um test_size de 0.3, ou seja, 70% para treino e 30% para testes e também foi utilizado um random_state de 42 para que o modelo possa ser recriado com a mesma acurácia.

Após testes o modelo de Regressão Linear se mostrou mais acurado que o modelo XG Boost, sendo a acurácia do XG de 0.86 e da Regressão Linear atingiu o valor de 0.97 de acurácia. O arquivo contendo o código utilizado no colab para a criação do modelo está disponível nesse repositório no arquivo [colab.py](https://github.com/jinkijack/Classificador-Jogos-FlaskIA/blob/main/colab.py).
