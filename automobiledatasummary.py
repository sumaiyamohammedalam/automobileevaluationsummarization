import pandas as pd

# -----------------------------
# Example Automobile Evaluation Data
# -----------------------------
data = {
    "manufacturer_country": [
        "Japan", "USA", "Germany", "Japan", "France",
        "Japan", "Germany", "USA", "France", "Japan"
    ],
    "buying_cost": [
        "low", "med", "high", "low", "med",
        "vhigh", "high", "low", "med", "low"
    ],
    "luggage": [
        "small", "med", "big", "small", "med",
        "big", "small", "med", None, "small"
    ],
    "doors": [
        "2", "4", "5more", "4", "2",
        "5more", "4", "2", "5more", "4"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# 1. Frequency of manufacturer_country
# -----------------------------
freq_country = df["manufacturer_country"].value_counts()
print("Manufacturer Frequency:\n", freq_country)
print("Modal category:", freq_country.idxmax())
print("4th most frequent:", freq_country.index[3])

# -----------------------------
# 2. Proportion of countries
# -----------------------------
prop_country = df["manufacturer_country"].value_counts(normalize=True) * 100
print("\nCountry Proportions (%):\n", prop_country)
print("Percentage of cars from Japan:", prop_country.get("Japan", 0))

# -----------------------------
# 3. Possible values of buying_cost
# -----------------------------
print("\nBuying cost values:", df["buying_cost"].unique())

# -----------------------------
# 4. Ordered buying cost categories
# -----------------------------
buying_cost_categories = ["low", "med", "high", "vhigh"]
df["buying_cost"] = pd.Categorical(df["buying_cost"], categories=buying_cost_categories, ordered=True)

# -----------------------------
# 5. Median buying cost
# -----------------------------
median_buying_cost = df["buying_cost"].median()
print("\nMedian Buying Cost:", median_buying_cost)

# -----------------------------
# 7. Luggage proportions
# -----------------------------
luggage_prop = df["luggage"].value_counts(normalize=True)
print("\nLuggage Proportions:\n", luggage_prop)

# -----------------------------
# 8. Including missing values
# -----------------------------
luggage_prop_with_nan = df["luggage"].value_counts(dropna=False, normalize=True)
print("\nLuggage Proportions Including Missing Values:\n", luggage_prop_with_nan)

# -----------------------------
# 9. Count table without normalize=True
# -----------------------------
luggage_counts = df["luggage"].value_counts()
print("\nLuggage Counts:\n", luggage_counts)

# -----------------------------
# 10. Cars with 5+ doors
# -----------------------------
doors_5more = df[df["doors"] == "5more"].shape[0]
print("\nNumber of cars with 5+ doors:", doors_5more)

# -----------------------------
# 11. Proportion of cars with 5+ doors
# -----------------------------
doors_5more_prop = doors_5more / len(df)
print("Proportion of cars with 5+ doors:", doors_5more_prop)
