# Sequence-Validator
![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Sequence-Validator)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 --- CAN YOU SOLVE THIS - EXCEL CHALLENGE 801 ---
- 🌟 * Author: Excel (Vijay A. Verma) BI
 
    - Topic: Align the data as per sequence numbers given after names!.
 
 🔰 Este script toma un archivo Excel con datos desordenados y tabulados, limpia la información, extrae nombres y números secuenciales, los alinea cronológicamente.

 
 🔗 Link to Excel file:
 👉 https://lnkd.in/dQW5gpYW

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Sequence-Validator/blob/main/sequence_validator.py


# 🧩 Sequence Aligner & Validator – pandas + Python

Este script toma un archivo Excel con datos desordenados y tabulados, limpia la información, extrae nombres y números secuenciales, los alinea cronológicamente y valida contra una respuesta esperada. Ideal para limpieza de datos, control de calidad y verificación de secuencias.

## 📦 Datos

- **State**: contiene el nombre de los Estados para alineación.
- **Data**: contiene los nombres y las secuencias asignadas para alinear cronológicamente.

---
## 🧠 Lógica del análisis

1. Lee un archivo Excel desde una URL.
2. Extrae nombres y números secuenciales por estado.
3. Limpia tabuladores y separadores.
4. Ordena los datos por número (`Seq`).
5. Compara con columnas de verificación.
6. Devuelve un DataFrame con datos ordenados y una columna `'Match'` que indica si la fila coincide.

---
## 📊 Resultado

Una tabla con:

- Name, Seq, State: datos procesados y ordenados.
- Columnas de verificación (`test`).
- Columna 'Match': True si la fila coincide, False si hay diferencias.

---
## ✨Output:

|Name   |    Seq | State   |    Name  |     Seq | State  |     Match|
|-|-|-|-|-|-|-|
|James   |     1 | Kansas    |  James    |    1 | Kansas    |  True|
|Susan   |     2 | California|  Susan    |    2 | California|  True|
|James   |     3 | Kansas    |  James    |    3 | Kansas    |  True|
|James   |     4 | Ohio      |  James    |    4 | Ohio      |  True|
|John    |     5 | California|  John     |    5 | California|  True|
|James   |     6 | Kansas    |  James    |    6 | Kansas    |  True|
|James   |     7 | Texas     |  James    |    7 | Texas     |  True|
|Linda   |     8 | California|  Linda    |    8 | California|  True|
|David   |     9 | Kansas    |  David    |    9 | Kansas    |  True|
|James   |    10 | New York  |  James    |   10 | New York  |  True|
|William |    11 | California|  William  |   11 | California|  True|
|Susan   |    12 | New York  |  Susan    |   12 | New York  |  True|
|David   |    13 | New York  |  David    |   13 | New York  |  True|
|Susan   |    14 | California|  Susan    |   14 | California|  True|
|David   |    15 | New York  |  David    |   15 | New York  |  True|
|David   |    16 | New York  |  David    |   16 | New York  |  True|
|Susan   |    17 | Ohio      |  Susan    |   17 | Ohio      |  True|
|Sarah   |    18 | Kansas    |  Sarah    |   18 | Kansas    |  True|

---
## 🛠️ Requisitos

- Python 3.8+
- pandas
- Archivo Excel

---
## 🚀 Ejecución
```bash
pip install pandas openpyxl
```
```python
sequence_validator.py
```
