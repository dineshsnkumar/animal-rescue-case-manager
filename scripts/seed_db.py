import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "animal_rescue.db"

conn = sqlite3.connect(DB_PATH)

intakes = pd.read_csv("data/raw/aac_intakes.csv")
outcomes = pd.read_csv("data/raw/aac_outcomes.csv")

intakes.to_sql("intakes", conn, if_exists="replace", index=False)
outcomes.to_sql("outcomes", conn, if_exists="replace", index=False)

conn.close()

print("Database seeded successfully!")
