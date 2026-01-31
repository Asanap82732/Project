import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load dataset
data = pd.read_csv("Unemployment_India.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Convert Date column (fix warning)
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)

print("Dataset Preview:")
print(data.head())

print("\nDataset Info:")
print(data.info())

# -------------------------------
# Overall Unemployment Trend
# -------------------------------
plt.figure(figsize=(10,5))
plt.plot(
    data['Date'],
    data['Estimated Unemployment Rate (%)'],
    color='red'
)
plt.title("Unemployment Rate Trend During COVID-19")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.show()

# -------------------------------
# Region-wise Unemployment
# -------------------------------
plt.figure(figsize=(12,6))
sns.barplot(
    x='Region',
    y='Estimated Unemployment Rate (%)',
    data=data
)
plt.xticks(rotation=90)
plt.title("Region-wise Unemployment Rate")
plt.show()

# -------------------------------
# Before vs After COVID Analysis
# -------------------------------
before_covid = data[data['Date'] < '2020-03-01']
after_covid = data[data['Date'] >= '2020-03-01']

before_avg = before_covid['Estimated Unemployment Rate (%)'].mean()
after_avg = after_covid['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate:")
print("Before COVID:", round(before_avg, 2))
print("After COVID:", round(after_avg, 2))

# Comparison Graph
labels = ['Before COVID', 'After COVID']
values = [before_avg, after_avg]

plt.figure(figsize=(6,4))
plt.bar(labels, values)
plt.title("Impact of COVID-19 on Unemployment")
plt.ylabel("Unemployment Rate (%)")
plt.show()

print("\nConclusion:")
print("- COVID-19 caused a sharp increase in unemployment.")
print("- Lockdown severely affected employment across regions.")
print("- Data analysis helps understand economic impact clearly.")


