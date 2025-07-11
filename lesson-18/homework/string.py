"""
Один скрипт для Home­work 2 и Home­work 3
— читает оба CSV‑файла;
— формирует DataFrame‑ы по всем заданным условиям;
— выводит краткие итоги (кол‑во строк) и при необходимости сохраняет результаты в отдельные файлы.

Файлы должны лежать в каталоге `task\`.
"""

import pandas as pd

# ────────────────────────────────
# Homework 2 — StackOverflow Q&A
# ────────────────────────────────
df = pd.read_csv(r"task\stackoverflow_qa.csv", parse_dates=["creationdate"])

q_before_2014 = df[df["creationdate"] < "2014-01-01"]

q_score_gt50 = df[df["score"] > 50]

q_score_50_100 = df[df["score"].between(50, 100)]

q_ans_scott = df[df["ans_name"] == "Scott Boston"]

five_users = ["unutbu", "jezrael", "DSM", "Warren Weckesser", "unutbu"]  # замените по‑своему
q_ans_5users = df[df["ans_name"].isin(five_users)]

mask_period = df["creationdate"].between("2014-03-01", "2014-10-31")
q_unutbu_low = df[mask_period & (df["ans_name"] == "unutbu") & (df["score"] < 5)]

q_mid_or_popular = df[(df["score"].between(5, 10)) | (df["viewcount"] > 10_000)]

q_not_scott = df[df["ans_name"] != "Scott Boston"]

# ────────────────────────────────
# Homework 3 — Titanic
# ────────────────────────────────
titanic_df = pd.read_csv(r"task\titanic.csv")

female_class1_20_30 = titanic_df[
    (titanic_df["Sex"] == "female") &
    (titanic_df["Pclass"] == 1) &
    (titanic_df["Age"].between(20, 30))
]

fare_gt_100 = titanic_df[titanic_df["Fare"] > 100]

survived_alone = titanic_df[
    (titanic_df["Survived"] == 1) &
    (titanic_df["SibSp"] == 0) &
    (titanic_df["Parch"] == 0)
]

embarked_c_fare_gt50 = titanic_df[
    (titanic_df["Embarked"] == "C") &
    (titanic_df["Fare"] > 50)
]

with_family = titanic_df[
    (titanic_df["SibSp"] > 0) &
    (titanic_df["Parch"] > 0)
]

kids_not_survived = titanic_df[
    (titanic_df["Age"] <= 15) &
    (titanic_df["Survived"] == 0)
]

cabin_and_fare_gt200 = titanic_df[
    titanic_df["Cabin"].notna() & (titanic_df["Fare"] > 200)
]

odd_passenger_id = titanic_df[titanic_df["PassengerId"] % 2 == 1]

unique_tickets = titanic_df[
    titanic_df["Ticket"].map(titanic_df["Ticket"].value_counts()) == 1
]

miss_class1 = titanic_df[
    titanic_df["Name"].str.contains(r"\bMiss\b") &
    (titanic_df["Sex"] == "female") &
    (titanic_df["Pclass"] == 1)
]

# ────────────────────────────────
# Итоговый вывод (по желанию)
# ────────────────────────────────
print("StackOverflow Q&A selections:")
print("  До 2014 года:", len(q_before_2014))
print("  Score > 50:", len(q_score_gt50))
print("  Score 50–100:", len(q_score_50_100))
print("  Ответил Scott Boston:", len(q_ans_scott))
print("  Ответили 5 users:", len(q_ans_5users))
print("  Unutbu, 03‑10/2014, score <5:", len(q_unutbu_low))
print("  Score 5–10 или views >10k:", len(q_mid_or_popular))
print("  Не Scott Boston:", len(q_not_scott))

print("\nTitanic selections:")
print("  Женщины 1 класс 20–30:", len(female_class1_20_30))
print("  Fare > $100:", len(fare_gt_100))
print("  Выжили и одни:", len(survived_alone))
print("  Embarked C и Fare > $50:", len(embarked_c_fare_gt50))
print("  С семьёй на борту:", len(with_family))
print("  Возраст ≤15, не выжили:", len(kids_not_survived))
print("  Cabin указан и Fare > $200:", len(cabin_and_fare_gt200))
print("  PassengerId нечётный:", len(odd_passenger_id))
print("  Уникальный Ticket:", len(unique_tickets))
print("  'Miss' в имени, класс 1:", len(miss_class1))

# При необходимости сохраняем любой из результатов:
# female_class1_20_30.to_csv("female_class1_20_30.csv", index=False)
# q_before_2014.to_csv("q_before_2014.csv", index=False)
