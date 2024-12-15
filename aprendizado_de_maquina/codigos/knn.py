from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

# Carregar o dataset
data = pd.read_csv("shoePrices.csv")

data['Size'] = data['Size'].str.replace('US ', '').astype(float)

data['Price (USD)'] = data['Price (USD)'].str.replace('$', '').str.strip().astype(float)


# Transformar o target em categorias
y_classification = pd.cut(data['Price (USD)'], bins=3, labels=['baixo', 'médio', 'alto'])
X_simple = data[['Size']]

# Dividir os dados
X_train, X_test, y_train, y_test = train_test_split(X_simple, y_classification, test_size=0.2, random_state=42)

# Treinar o modelo KNN
model_knn = KNeighborsClassifier(n_neighbors=5)
model_knn.fit(X_train, y_train)

# Previsões e avaliação
y_pred = model_knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print("Acurácia:", accuracy)
print("Precisão:", precision)
print("Recall:", recall)
print("F1-score:", f1)

# Matriz de Confusão
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Matriz de Confusão')
plt.show()
