# Recomendador de Productos y Análisis de Ofertas - Santa Isabel Chile

<img width="1200" height="1200" alt="logo" src="https://github.com/user-attachments/assets/7cf508a3-9325-4c16-83f1-6ab0b0edb891" />


---

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos de productos del supermercado **Santa Isabel (Chile)** y construir un sistema recomendador basado en similitud de texto para sugerir productos similares según el nombre ingresado por el usuario.

Este proyecto tiene un enfoque **demostrativo y educativo**. Su objetivo principal es mostrar la aplicación práctica de técnicas de Inteligencia Artificial y Machine Learning en un contexto de análisis de datos y sistemas de recomendación. Se ha utilizado un conjunto de datos de precios de productos para ilustrar cómo se pueden construir modelos predictivos y herramientas de análisis en un entorno real.

Los datos de precios y productos utilizados en este proyecto son de ejemplo y fueron recolectados en una fecha específica (2022-07-16). Este trabajo **no está oficialmente vinculado con Santa Isabel** y debe ser considerado únicamente con fines de demostración técnica. Los resultados, precios y recomendaciones aquí presentados no reflejan la información actual o real de la cadena de supermercados.

El proyecto consta de dos partes principales:


1. **Análisis Exploratorio de Datos (EDA):**  
   Se explora la distribución de precios, se identifican los productos más baratos, las categorías con mayor frecuencia y aquellas con mayores descuentos, además de calcular KPIs relevantes como porcentaje de productos en oferta y descuento promedio.

2. **Sistema Recomendador Web:**  
   Implementado con Streamlit, permite al usuario ingresar el nombre de un producto y obtener recomendaciones de productos similares, mostrando tanto el precio normal como el precio en oferta (si lo tiene). También se incluyen KPIs básicos en la interfaz.

---

## Dataset

El dataset utilizado fue obtenido desde Kaggle:  
[Santa Isabel Chile - Kaggle](https://www.kaggle.com/datasets/edwight/santa-isabel-chile)

**Características del dataset:**

- **Número de filas:** 4,468 productos  
- **Número de columnas:** 12  
- **Columnas usadas en el análisis:**  
  - `title`: Nombre o título del producto  
  - `brand`: Marca  
  - `normal_price`: Precio normal sin descuento  
  - `low_price`: Precio con oferta  
  - `high_price`: Precio antes de la oferta  
  - `oferta`: Indicador binario (1 = producto en oferta, 0 = no)  
  - `categoria1`: Categoría principal  
  - `categoria2`: Subcategoría  
  - `datetime`: Fecha de recolección  
  - `sin_stock`: Disponibilidad del producto (0 o 1)  

**Se eliminaron las columnas `Atributos` y `page` ya que no aportaban información relevante para este análisis.**

---

## Análisis Exploratorio

### Distribución de Precios con Oferta

- Se graficó un histograma general del precio con oferta (`low_price`) entre 0 y 6000 CLP para visualizar la distribución general.

<img width="1048" height="561" alt="image" src="https://github.com/user-attachments/assets/cb619486-dfa1-47f8-8c05-39fb358e93a7" />


- Se hizo un zoom en precios entre 2000 y 4000 CLP, rango con alta concentración de productos.

<img width="1031" height="556" alt="image" src="https://github.com/user-attachments/assets/9773fbfa-d721-4cc3-9457-51e9bc89393a" />


### Productos Más Baratos

| Producto             | Marca         | Precio con Oferta (CLP) |
|---------------------|---------------|-------------------------|
| Bicarbonato 30 g     | Cuisine & Co  | 87                      |
| Ají color 15 g       | Cuisine & Co  | 127                     |
| Aliño completo 15 g  | Cuisine & Co  | 135                     |
| Ajo en polvo 15 g    | Cuisine & Co  | 151                     |
| Merquén 15 g         | Cuisine & Co  | 191                     |


### Top 10 Subcategorías más frecuentes

<img width="836" height="654" alt="image" src="https://github.com/user-attachments/assets/2920d2f1-a8b9-4533-a818-1a2fe21afb5e" />


### KPIs Clave

- Porcentaje de productos en oferta: **19.19%**  
- Descuento promedio en productos con oferta: **7.37%**  
- Categorías con mayor descuento promedio:  
  - aceites-sal-y-condimentos: 63.75%  
  - instantaneos-y-sopas: 38.54%  
  - pavo: 35.54%  
  - leches: 33.79%  
  - lacteos: 32.56%

---

## Modelo de Machine Learning

Se entrenó un modelo de **Regresión Lineal** para predecir el precio con oferta (`low_price`) usando como variables predictoras:

- `normal_price` (precio normal)  
- `high_price` (precio antes de la oferta)  
- `oferta` (si tiene oferta o no)  

### Interpretación y Resultado

* **R² Score:** Con un valor de **0.89**, el modelo explica el **89% de la variabilidad** en los precios con oferta. Este resultado sugiere que la regresión lineal es capaz de capturar una porción significativa de la relación entre las variables, lo que indica un ajuste bastante bueno.

* **RMSE:** El **Error Cuadrático Medio** (RMSE) es de **614.29 CLP**. Esto significa que, en promedio, las predicciones del modelo se desvían del precio real en aproximadamente **$614,29 pesos chilenos**. Este valor es aceptable para el contexto comercial y el propósito del proyecto.

Con un R² de 0.89, el modelo explica muy bien la variabilidad en los precios con oferta, es decir, puede predecir con bastante precisión cuánto costará un producto cuando tiene descuento, basándose en su precio original y condiciones de oferta.

Sin embargo, este modelo no es indispensable para el análisis ni la recomendación; su objetivo principal es demostrar el uso de técnicas de Machine Learning y cómo pueden aplicarse para entender mejor los datos de precios. En escenarios reales, podrían usarse modelos más complejos o incorporar más variables para mejorar la predicción.

### Alcances y Limitaciones


* El modelo tiene fines **demostrativos y didácticos**. Su objetivo es ilustrar la aplicación de técnicas de machine learning en un contexto real de precios y ofertas.
* **No es un sistema de predicción definitivo.** No está diseñado para la toma de decisiones comerciales automáticas, ya que no considera factores externos clave como la estacionalidad, la competencia del mercado o promociones dinámicas.
* La base de datos se limita a un solo día (2022-07-16), por lo que el modelo **no captura cambios temporales ni tendencias** a lo largo del tiempo. Esto restringe su capacidad predictiva para otros períodos.

### Mejoras Futuras

1.  **Incorporar datos históricos:** Recolectar datos de múltiples días o períodos para modelar tendencias temporales y estacionalidad.
2.  **Modelos más complejos:** Explorar modelos de Machine Learning más avanzados, como **Árboles de Decisión, Random Forests o Redes Neuronales**, para capturar relaciones no lineales en los datos.
3.  **Integrar variables externas:** Añadir variables adicionales como datos de la competencia o el comportamiento de compra de los usuarios para mejorar la robustez y precisión del modelo.
4.  **Desarrollar un sistema de recomendación:** Crear un recomendador avanzado basado en técnicas de **aprendizaje profundo** o **sistemas híbridos** de filtrado colaborativo y contenido para ofrecer sugerencias de productos más precisas.
***

---

## Aplicación Web - Sistema Recomendador

La aplicación fue desarrollada en **Streamlit** para proporcionar una interfaz sencilla y rápida donde el usuario puede ingresar el nombre de un producto y obtener recomendaciones similares.

El sistema de recomendación utiliza técnicas de **Inteligencia Artificial** del área de **Procesamiento de Lenguaje Natural (NLP)** para sugerir productos similares. Funciona de la siguiente manera:

1.  **TF-IDF**: Se aplica **Term Frequency-Inverse Document Frequency** (`TfidfVectorizer`) a los títulos de los productos para convertirlos en vectores numéricos. Esto permite al modelo entender la importancia de cada palabra.
2.  **Similitud del Coseno**: Una vez que los títulos son vectores, se usa la **Similitud del Coseno** (`cosine_similarity`) para medir la cercanía entre ellos. Un ángulo más pequeño entre dos vectores indica que sus títulos son más parecidos, y por lo tanto, se consideran productos similares para la recomendación.


### Características

- Busca productos que contengan el texto ingresado en su título (búsqueda insensible a mayúsculas).  
- Calcula la similitud de texto usando TF-IDF y similitud de coseno para obtener productos relacionados.  
- Muestra una tabla con:  
  - Producto  
  - Marca  
  - Precio Normal (formateado con signo $ y miles)  
  - Precio con Oferta (si no hay oferta muestra "-")  
- Permite mostrar KPIs básicos (porcentaje de productos en oferta y descuento promedio).  
- Logo de Santa Isabel centrado en la cabecera para mayor identidad visual.  

---

## Ejemplo de Uso

Ingresando la palabra **"cepillo"** en el buscador, se obtienen recomendaciones como:

<img width="723" height="931" alt="image" src="https://github.com/user-attachments/assets/00d79d6a-05e4-4b08-8508-8951fe881919" />

Ingresando la palabra **"Shampoo"** en el buscador, se obtienen recomendaciones como:

<img width="746" height="907" alt="image" src="https://github.com/user-attachments/assets/159f6ad5-6849-4f9b-bb6a-4a7786858299" />


---

## Requisitos e Instalación

### Dependencias

- Python 3.7+  
- pandas  
- numpy  
- streamlit  
- scikit-learn  
- nltk  
- matplotlib  
- seaborn  


