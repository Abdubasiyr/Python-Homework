import pandas as pd
import sqlite3

# ───────────────────────────────────────────
# Homework 1: Analyzing Sales Data
# ───────────────────────────────────────────
sales_df = pd.read_csv(r"task\sales_data.csv")

# 1. Группировка по категории: сумма, средняя цена, макс. количество
category_stats = sales_df.groupby("Category").agg({
    "Quantity": ["sum", "max"],
    "Price": "mean"
}).rename(columns={"sum": "Total Quantity", "max": "Max Quantity", "mean": "Average Price"})

# 2. Топ‑продукт в каждой категории по сумме продаж
top_products = sales_df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
top_selling_product_per_category = top_products.groupby("Category").first().reset_index()

# 3. Дата с наибольшей выручкой (Quantity * Price)
sales_df["Total"] = sales_df["Quantity"] * sales_df["Price"]
sales_by_date = sales_df.groupby("Date")["Total"].sum()
top_sales_date = sales_by_date.idxmax()
top_sales_amount = sales_by_date.max()

# ───────────────────────────────────────────
# Homework 2: Examining Customer Orders
# ───────────────────────────────────────────
orders_df = pd.read_csv(r"task\customer_orders.csv")

# 1. Клиенты с ≥ 20 заказами
customer_order_counts = orders_df.groupby("CustomerID")["OrderID"].nunique()
customers_20plus = customer_order_counts[customer_order_counts >= 20].index
filtered_customers_20plus = orders_df[orders_df["CustomerID"].isin(customers_20plus)]

# 2. Клиенты с средней ценой заказа > $120
avg_price_per_customer = orders_df.groupby("CustomerID")["Price"].mean()
customers_gt_120 = avg_price_per_customer[avg_price_per_customer > 120].index
filtered_customers_gt_120 = orders_df[orders_df["CustomerID"].isin(customers_gt_120)]

# 3. Группировка по продуктам — сумма количества и цены, фильтр < 5
product_stats = orders_df.groupby("Product").agg({
    "Quantity": "sum",
    "Price": "sum"
}).reset_index()
product_stats_filtered = product_stats[product_stats["Quantity"] >= 5]

# ───────────────────────────────────────────
# Homework 3: Population Salary Analysis
# ───────────────────────────────────────────
# 1. Чтение из БД SQLite
conn = sqlite3.connect(r"task\population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# 2. Чтение Excel со шкалой зарплат
salary_bands = pd.read_excel(r"task\population salary analysis.xlsx")

# Ожидается: столбцы 'Min', 'Max', 'Salary Band'
# Добавим каждому человеку категорию по зарплате
def assign_salary_band(salary):
    row = salary_bands[(salary_bands["Min"] <= salary) & (salary <= salary_bands["Max"])]
    return row["Salary Band"].values[0] if not row.empty else "Unknown"

population_df["Salary Band"] = population_df["Salary"].apply(assign_salary_band)

# 3. Метрики по Salary Band
band_stats = population_df.groupby("Salary Band").agg(
    Population_Count=("Salary", "count"),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
)
band_stats["Percentage"] = round(100 * band_stats["Population_Count"] / band_stats["Population_Count"].sum(), 2)

# 4. Метрики по Salary Band в каждом штате
state_band_stats = population_df.groupby(["State", "Salary Band"]).agg(
    Population_Count=("Salary", "count"),
    Average_Salary=("Salary", "mean"),
    Median_Salary=("Salary", "median")
).reset_index()

total_population_per_state = population_df.groupby("State")["Salary"].count().reset_index(name="State_Population")
state_band_stats = state_band_stats.merge(total_population_per_state, on="State")
state_band_stats["Percentage"] = round(100 * state_band_stats["Population_Count"] / state_band_stats["State_Population"], 2)
state_band_stats.drop("State_Population", axis=1, inplace=True)

# ───────────────────────────────────────────
# Пример вывода результатов
# ───────────────────────────────────────────
print("\nHomework 1:")
print("Агрегация по категориям:\n", category_stats)
print("\nТоп‑продукты в категориях:\n", top_selling_product_per_category)
print(f"\nДата с наибольшей выручкой: {top_sales_date}, сумма: {top_sales_amount:.2f}")

print("\nHomework 2:")
print("Клиенты с ≥20 заказами:", len(filtered_customers_20plus["CustomerID"].unique()))
print("Клиенты со средней ценой > $120:", len(filtered_customers_gt_120["CustomerID"].unique()))
print("Продукты с ≥5 ед.:", len(product_stats_filtered))

print("\nHomework 3:")
print("\nДоля населения по Salary Band:\n", band_stats)
print("\nПо Salary Band в каждом штате:\n", state_band_stats.head(10))  # показываем только первые 10 строк
