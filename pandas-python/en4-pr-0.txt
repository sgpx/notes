### Problem: **"The Coffee Shop Daily Sales Tracker"**

**Context:**  
You own a small coffee shop. You want to track the number of coffees sold each day for one week (Monday–Sunday) using a `pandas.Series`. You will practice creating the series, accessing data, doing math on the whole series at once, and answering simple business questions.

---

### 📋 The Data
| Day | Coffees Sold |
|-----|--------------|
| Mon | 45 |
| Tue | 52 |
| Wed | 38 |
| Thu | 60 |
| Fri | 75 |
| Sat | 90 |
| Sun | 65 |

---

## 🛠️ Step-by-Step Tasks

### **Level 1: Creation & Inspection**
1.  Create a `pandas.Series` named `sales` using the data above.
    *   *Hint: Use a Python dictionary so the days become the **index**.*
2.  Print the series. What is the **index**? What are the **values**?
3.  Check the data type (`dtype`) of the values.

### **Level 2: Accessing Data (Indexing)**
4.  How many coffees were sold on **Friday**? (Access by label: `sales['Fri']`)
5.  Which days had sales **greater than 50**? (Boolean indexing: `sales[sales > 50]`)
6.  Get the sales for the **weekend** (Sat & Sun) using a list of labels: `sales[['Sat', 'Sun']]`.

### **Level 3: Vectorized Operations (Math on the whole Series)**
7.  You make **$3.50 profit per coffee**. Create a new Series `profits` by multiplying `sales * 3.5`.
8.  You had a "Buy 1 Get 1 Free" promo on **Wednesday**. Update Wednesday's sales to be double the original value (38 → 76).
    *   *Hint: `sales['Wed'] = 76`*

### **Level 4: Basic Analytics**
9.  Calculate the **Total**, **Average (mean)**, **Maximum**, and **Minimum** coffees sold for the week.
    *   *Hint: `.sum()`, `.mean()`, `.max()`, `.min()`*
10. Which day had the **highest sales**? (Hint: `.idxmax()`)
11. Sort the series from **highest to lowest** sales. (Hint: `.sort_values(ascending=False)`)

---

## ✅ Solution Code (Copy & Run)

```python
import pandas as pd

# ---------------------------------------------------------
# LEVEL 1: CREATION
# ---------------------------------------------------------
data = {
    'Mon': 45, 'Tue': 52, 'Wed': 38, 
    'Thu': 60, 'Fri': 75, 'Sat': 90, 'Sun': 65
}

sales = pd.Series(data, name="Coffees_Sold")

print("--- 1. The Series ---")
print(sales)
print(f"\nIndex: {sales.index.tolist()}")
print(f"Values: {sales.values}")
print(f"Dtype: {sales.dtype}")

# ---------------------------------------------------------
# LEVEL 2: ACCESSING DATA
# ---------------------------------------------------------
print("\n--- 2. Accessing Data ---")
# 4. Friday sales
print(f"Friday Sales: {sales['Fri']}") 

# 5. Days > 50 (Boolean Masking)
busy_days = sales[sales > 50]
print(f"Days > 50 sales:\n{busy_days}")

# 6. Weekend sales (List of labels)
weekend = sales[['Sat', 'Sun']]
print(f"Weekend Sales:\n{weekend}")

# ---------------------------------------------------------
# LEVEL 3: VECTORIZED MATH
# ---------------------------------------------------------
print("\n--- 3. Vectorized Math ---")
# 7. Profit calculation
profits = sales * 3.5
print(f"Daily Profits:\n{profits}")

# 8. Update Wednesday (Promo correction)
print(f"\nOriginal Wed: {sales['Wed']}")
sales['Wed'] = 76 # Double the original 38
print(f"Updated Wed:  {sales['Wed']}")

# ---------------------------------------------------------
# LEVEL 4: ANALYTICS
# ---------------------------------------------------------
print("\n--- 4. Analytics ---")
print(f"Total Sold:   {sales.sum()}")
print(f"Average/Day:  {sales.mean():.1f}")
print(f"Best Day:     {sales.max()} (on {sales.idxmax()})")
print(f"Slowest Day:  {sales.min()} (on {sales.idxmin()})")

print("\n--- Ranked Best to Worst ---")
print(sales.sort_values(ascending=False))
```

---

## 🧠 Key Concepts Learned
| Concept | Code Used | Why it matters |
| :--- | :--- | :--- |
| **Custom Index** | `pd.Series(dict)` | Labels (Mon, Tue) are better than 0, 1, 2 for time data. |
| **Label Indexing** | `sales['Fri']` | Fast, readable lookup by name. |
| **Boolean Indexing** | `sales[sales > 50]` | Filter data *without* writing `for` loops. |
| **Vectorization** | `sales * 3.5` | Math applies to **every element instantly** (C-speed). |
| **Mutability** | `sales['Wed'] = 76` | Series are mutable; you can fix dirty data in place. |
| **Aggregations** | `.sum()`, `.mean()` | Built-in stats optimized for speed. |
| **Sorting** | `.sort_values()` | Essential for ranking / top-N analysis. |

---

## 🚀 Extension Challenges (Try these next!)
1.  **Reindexing:** Create a new series for *next week* where you only have data for Mon, Wed, Fri. Use `reindex` to align it to Mon-Sun (missing days become `NaN`).
2.  **Plotting:** Add `%matplotlib inline` (if in Jupyter) and run `sales.plot(kind='bar', title='Weekly Coffee Sales')`.
3.  **Rolling Average:** Calculate a 3-day rolling average: `sales.rolling(window=3).mean()`. (Introduces `NaN` for the first 2 days).
