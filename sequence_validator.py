import pandas as pd
from tabulate import tabulate

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=1)
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :2].dropna(how='all')
df_input.columns = ['State', 'Data']

# ✅ Comparacion con la respuesta esperada
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)

# 🧠 Procesar y limpiar
result = []
for state, people_str in df_input.values.tolist():
    entries = people_str.split(';')
    for entry in entries:
        if ':' in entry:
            name, nums = entry.split(':')
            name = name.strip()
            nums = nums.replace('\t', '').strip()
            for num in nums.split(','):
                num = num.strip()
                if num.isdigit():
                    result.append([name, int(num), state])

# 🔀 Ordenar por número
result_sorted = sorted(result, key=lambda x: x[1])

# 📊 Convertir a DataFrame
df_final = pd.DataFrame(result_sorted, columns=['Name', 'Seq', 'State'])

test = df_raw.iloc[:, 3:].copy()
df_final = compare_with_expected(df_final, test)

print(tabulate(df_final.values, headers=df_final.columns, tablefmt='fancy'))
