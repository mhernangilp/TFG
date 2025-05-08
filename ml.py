import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt

# 1. Cargar el dataset
df = pd.read_csv('resources/processed_data/dataset.csv')

# 2. Separar características (X) y etiqueta (y)
X = df.drop(['label'], axis=1)
y = df['label']

# 3. Dividir en entrenamiento y prueba (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Imputar valores faltantes (NaN)
imputer = SimpleImputer(strategy='median')
X_train_imputed = imputer.fit_transform(X_train)
X_test_imputed = imputer.transform(X_test)

# 5. Estandarizar las características numéricas
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_imputed)
X_test_scaled = scaler.transform(X_test_imputed)

# 6. Selección de algoritmo
def seleccionar_modelo():
    print("Seleccione el algoritmo a usar:")
    print("1. Regresión Logística")
    print("2. K-Nearest Neighbors (KNN)")
    print("3. Random Forest")
    print("4. Extreme Gradient Boosting (XGBoost)")
    print("5. Support Vector Machine (SVM)")
    choice = input("Introduzca el número de la opción (1-5): ")
    if choice == '1':
        return LogisticRegression(solver='liblinear',penalty='l2',C=1.0), 'Regresión Logística'
    elif choice == '2':
        return KNeighborsClassifier(n_neighbors=9,weights='distance',metric='minkowski',p=2,n_jobs=-1,algorithm='ball_tree'), 'K-Nearest Neighbors'
    elif choice == '3':
        return RandomForestClassifier(n_estimators=100,criterion='gini',max_depth=8,random_state=42,n_jobs=-1), 'Random Forest'
    elif choice == '4':
        return XGBClassifier(n_estimators=30,learning_rate=0.3,max_depth=6,eval_metric='logloss',random_state=42), 'XGBoost'
    elif choice == '5':
        return SVC(probability=True,kernel='rbf',C=50,random_state=42), 'Support Vector Machine'
    else:
        print("Opción no válida. Abortando ...")
        exit()

model, model_name = seleccionar_modelo()

# 7. Entrenamiento del modelo
model.fit(X_train_scaled, y_train)

# 8. Predicciones y probabilidades
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1]

# 9. Evaluación del rendimiento
print(f"=== Resultados para {model_name} ===")
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred))
print(f"ROC AUC Score: {roc_auc_score(y_test, y_proba):.3f}")

# 10. Curva ROC
def plot_roc(fpr, tpr, model_name):
    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC AUC = {roc_auc_score(y_test, y_proba):.3f}")
    plt.plot([0, 1], [0, 1], linestyle='--')
    plt.xlabel('Tasa de Falsos Positivos')
    plt.ylabel('Tasa de Verdaderos Positivos')
    plt.title(f'Curva ROC - {model_name}')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

fpr, tpr, _ = roc_curve(y_test, y_proba)
plot_roc(fpr, tpr, model_name)

# 11. Importancia de características (Solo para modelos con feature_importances_)
if hasattr(model, 'feature_importances_'):
    importances = pd.Series(model.feature_importances_, index=X.columns)
    importances = importances.sort_values(ascending=False)
    print("\nImportancia de características:")
    print(importances)
