import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, roc_auc_score,precision_score, recall_score, f1_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargar los datasets
df_train = pd.read_csv('resources/processed_data/dataset_train.csv')
df_valid = pd.read_csv('resources/processed_data/dataset_val.csv')

# 2. Separar características (X) y etiqueta (y)
X_train = df_train.drop(['label'], axis=1)
y_train = df_train['label']
X_test = df_valid.drop(['label'], axis=1)
y_test = df_valid['label']

# 3. Imputar valores faltantes (NaN)
imputer = SimpleImputer(strategy='median')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# 4. Estandarizar las características numéricas
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

# 5. Selección de algoritmo
def seleccionar_modelo():
    print("Seleccione el algoritmo a usar:")
    print("1. Regresión Logística")
    print("2. K-Nearest Neighbors (KNN)")
    print("3. Random Forest")
    print("4. Extreme Gradient Boosting (XGBoost)")
    print("5. Support Vector Machine (SVM)")
    choice = input("Introduzca el número de la opción (1-5): ")
    if choice == '1':
        return LogisticRegression(solver='liblinear', penalty='l2', C=1.0), 'Regresión Logística'
    elif choice == '2':
        return KNeighborsClassifier(n_neighbors=9, weights='distance', metric='minkowski', p=2, n_jobs=-1, algorithm='ball_tree'), 'K-Nearest Neighbors'
    elif choice == '3':
        return RandomForestClassifier(n_estimators=100, criterion='gini', max_depth=8, random_state=42, n_jobs=-1), 'Random Forest'
    elif choice == '4':
        return XGBClassifier(n_estimators=30, learning_rate=0.3, max_depth=6, eval_metric='logloss', random_state=42), 'XGBoost'
    elif choice == '5':
        return SVC(probability=True, kernel='rbf', C=50, random_state=42), 'Support Vector Machine'
    else:
        print("Opción no válida. Abortando ...")
        exit()

model, model_name = seleccionar_modelo()

# 6. Entrenamiento del modelo
model.fit(X_train_scaled, y_train)

# 7. Predicciones y probabilidades
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# 8. Evaluación del rendimiento
print(f"\n=== Resultados para {model_name} ===")

# Matriz de Confusión
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['No', 'Sí'], yticklabels=['No', 'Sí'])
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.title('Matriz de Confusión')
plt.show()

# Métricas resumidas
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
f1 = f1_score(y_test, y_pred, average='binary')
roc_auc = roc_auc_score(y_test, y_proba)

print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1-score:  {f1:.3f}")
print(f"ROC AUC:   {roc_auc:.3f}")