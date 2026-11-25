# Загрузка событий ИБ из JSON и график по типам событий.
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE = Path(__file__).parent

with open(BASE / "events.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print("Первые строки:")
print(df.head())
print()
print("Количество событий по типам:")
counts = df["signature"].value_counts()
print(counts)
print()
print("Всего событий:", len(df))

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, y="signature", order=counts.index, color="steelblue")
plt.title("Распределение событий ИБ по типам")
plt.xlabel("Количество событий")
plt.ylabel("Тип события")
plt.tight_layout()
plt.savefig(BASE / "event_types.png", dpi=150)
plt.show()
