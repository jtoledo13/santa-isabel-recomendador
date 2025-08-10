# Recomendador de Productos y Análisis de Ofertas - Santa Isabel Chile

<img width="1200" height="1200" alt="logo" src="https://github.com/user-attachments/assets/7cf508a3-9325-4c16-83f1-6ab0b0edb891" />


---

## Descripción del Proyecto

Este proyecto tiene como objetivo analizar un conjunto de datos de productos del supermercado **Santa Isabel (Chile)** y construir un sistema recomendador basado en similitud de texto para sugerir productos similares según el nombre ingresado por el usuario.

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
- Se hizo un zoom en precios entre 2000 y 4000 CLP, rango con alta concentración de productos.

### Productos Más Baratos

| Producto             | Marca         | Precio con Oferta (CLP) |
|---------------------|---------------|-------------------------|
| Bicarbonato 30 g     | Cuisine & Co  | 87                      |
| Ají color 15 g       | Cuisine & Co  | 127                     |
| Aliño completo 15 g  | Cuisine & Co  | 135                     |
| Ajo en polvo 15 g    | Cuisine & Co  | 151                     |
| Merquén 15 g         | Cuisine & Co  | 191                     |

### Categorías Más Frecuentes

- Top 10 subcategorías:  
  conservas, lacteos, aderezos y salsas, pastas y salsas, aceites sal y condimentos, arroz y legumbres, coctel, congelados, desayuno y dulces, belleza y cuidado personal.

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

### Resultados del Modelo

- **R² Score:** 0.89  
- **RMSE:** 614.29 CLP  

Este modelo demuestra un buen ajuste para predecir precios con oferta basándose en las variables mencionadas.

---

## Aplicación Web - Sistema Recomendador

La aplicación fue desarrollada en **Streamlit** para proporcionar una interfaz sencilla y rápida donde el usuario puede ingresar el nombre de un producto y obtener recomendaciones similares.

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

| Producto                           | Marca    | Precio Normal | Precio con Oferta |
|----------------------------------|----------|---------------|-------------------|
| Cepillo dental plus suave 2 un.  | Dento    | $2,690        | $2,690            |
| Cepillo dental Twister Fresh 2 un.| Colgate | $2,690        | $2,690            |
| Cepillo dental doble acción 6N 2 un.| Duralón | $2,690       | $2,690            |
| Cepillo dental doble acción 6M 2 un.| Duralón | $2,690       | $2,690            |
| Pasta dental Triple Acción menta  | Colgate  | $2,690        | $2,690            |

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

### Instalación rápida

Clonar este repositorio y luego instalar dependencias:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
pip install -r requirements.txt
