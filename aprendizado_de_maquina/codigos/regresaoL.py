# Importar as bibliotecas necessárias
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Carregar o dataset
data = pd.read_csv("shoePrices.csv")

# Corrigir a coluna 'Size' para ser numérica (remover 'US ' e converter para float)
data['Size'] = data['Size'].str.replace('US ', '').astype(float)

# Corrigir a coluna 'Price (USD)' para ser numérica (remover '$' e converter para float)
data['Price (USD)'] = data['Price (USD)'].str.replace('$', '').str.strip().astype(float)

# Usar apenas 'Size' como variável independente (X) para o modelo simples
X_simple = data[['Size']]
y = data['Price (USD)']

# Dividir o dataset em 80% treino e 20% teste
X_train, X_test, y_train, y_test = train_test_split(X_simple, y, test_size=0.2, random_state=42)

# Inicializar e treinar o modelo de Regressão Linear
model_regression = LinearRegression()
model_regression.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = model_regression.predict(X_test)

# Calcular MAE e MSE
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

# Calcular a porcentagem de erro para MAE e MSE
mae_percentage = (mae / y_test.mean()) * 100
mse_percentage = (mse / y_test.mean()) * 100

# Exibir os resultados das métricas de erro e suas porcentagens
print("Erro Médio Absoluto (MAE):", mae)
print("Erro Quadrático Médio (MSE):", mse)
print("Porcentagem de Erro MAE:", mae_percentage, "%")
print("Porcentagem de Erro MSE:", mse_percentage, "%")

# Plotar gráfico de dispersão para comparar valores reais e previstos
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='blue', label='Valor Real', alpha=0.5)
plt.plot(X_test, y_pred, color='red', label='Valor Previsto', alpha=0.5)
plt.xlabel('Tamanho (Size)')
plt.ylabel('Preço (USD)')
plt.title('Regressão Linear com uma Feature ou Recurso')
plt.legend()
plt.show()
