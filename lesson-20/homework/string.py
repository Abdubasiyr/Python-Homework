# Сохранение результатов (при необходимости)
category_stats.to_csv("results/category_stats.csv")
top_selling_product_per_category.to_csv("results/top_products.csv", index=False)
filtered_customers_20plus.to_csv("results/customers_20plus.csv", index=False)
filtered_customers_gt_120.to_csv("results/customers_gt_120.csv", index=False)
product_stats_filtered.to_csv("results/product_stats_filtered.csv", index=False)
band_stats.to_csv("results/salary_band_stats.csv")
state_band_stats.to_csv("results/state_band_stats.csv", index=False)
