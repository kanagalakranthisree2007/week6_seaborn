import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import os

# Ensure visualizations folder exists
os.makedirs("visualizations", exist_ok=True)

# Load dataset
df = pd.read_csv(r"C:\Users\kanag\OneDrive\Desktop\intenship\customer_sales_analysis\notebooks\sales_data.csv")

# Seaborn Visualizations (Static)
# Box Plot: Price by Product
plt.figure(figsize=(6,4))
sns.boxplot(x='Product', y='Price', data=df, palette="Set2")
plt.title("Price Distribution by Product")
plt.savefig("visualizations/boxplot.png")
plt.close()

# Violin Plot: Sales by Region
plt.figure(figsize=(6,4))
sns.violinplot(x='Region', y='Sales', data=df, palette="muted")
plt.title("Sales Spread by Region")
plt.savefig("visualizations/violinplot.png")
plt.close()

# Heatmap: Correlation
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("visualizations/heatmap.png")
plt.close()

# Bar Plot: Average Sales by Product
plt.figure(figsize=(6,4))
sns.barplot(x='Product', y='Sales', data=df, palette="pastel")
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.savefig("visualizations/barplot.png")
plt.close()

# Line Plot: Sales Trend Over Time
plt.figure(figsize=(6,4))
sns.lineplot(x='Date', y='Sales', data=df, marker="o")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.savefig("visualizations/lineplot.png")
plt.close()

# Plotly Interactive Dashboard
# Line Chart with Hover
fig_line = px.line(df, x="Date", y="Sales", color="Region",
                   hover_data=["Product"], title="Interactive Sales Trend")

# Bar Chart
fig_bar = px.bar(df, x="Product", y="Sales", color="Region",
                 title="Product Sales by Region")

# Animated Chart (Sales over Time)
fig_anim = px.scatter(df, x="Price", y="Sales", animation_frame="Date",
                      size="Sales", color="Region", hover_name="Product",
                      title="Sales Animation Over Time")

# Combine into Subplot Dashboard
fig = make_subplots(rows=2, cols=2,
                    subplot_titles=("Sales Trend", "Product Sales", "Correlation Heatmap", "Sales Scatter"))

# Add traces
fig.add_trace(go.Scatter(x=df["Date"], y=df["Sales"], mode="lines+markers", name="Sales Trend"), row=1, col=1)
fig.add_trace(go.Bar(x=df["Product"], y=df["Sales"], name="Product Sales"), row=1, col=2)
fig.add_trace(go.Heatmap(z=df.corr(numeric_only=True).values,
                         x=df.corr(numeric_only=True).columns,
                         y=df.corr(numeric_only=True).columns,
                         colorscale="Viridis"), row=2, col=1)
fig.add_trace(go.Scatter(x=df["Price"], y=df["Sales"], mode="markers", name="Sales Scatter"), row=2, col=2)

fig.update_layout(title_text="Interactive Sales Dashboard", height=800, width=1000)
fig.show()
