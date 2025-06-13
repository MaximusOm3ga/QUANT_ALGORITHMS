import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 🔍 Load results from CSV
print("🔍 Loading results from CSV...")
try:
    results_df = pd.read_csv("./trading/partial_results.csv")
    print("✅ Results loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load CSV: {e}")
    results_df = None

# 🧠 Process and plot if data is available
if results_df is not None:
    # 🌟 Show top 20 strategies
    top20 = results_df.sort_values('total_return', ascending=False).head(20)
    print("\n🌟 Top 20 Best Performing Combinations (across all stocks):")
    print(top20)

    # 📊 Buy Z vs Sell Z heatmaps for each stock
    print("\n📈 Generating Buy Z vs Sell Z heatmaps...")
    unique_stocks = results_df['stock'].unique()
    for stock in unique_stocks:
        stock_df = results_df[results_df['stock'] == stock]
        if not stock_df.empty:
            pivot = stock_df.pivot_table(index='buy_z', columns='sell_z', values='total_return', aggfunc='max')
            plt.figure(figsize=(10, 6))
            sns.heatmap(pivot, annot=False, cmap='RdYlGn', center=0)
            plt.title(f'Returns Heatmap for {stock}\n(Buy Z vs Sell Z)')
            plt.xlabel('Sell Z-Score')
            plt.ylabel('Buy Z-Score')
            plt.tight_layout()
            plt.savefig(f"heatmap_buy_sell_zscore_{stock.replace('.', '_')}.png")
            plt.close()

    # 🎯 Top 3 stocks based on best single return (not frequency)
    top3_rows = results_df.sort_values('total_return', ascending=False).drop_duplicates('stock').head(3)
    top3_stocks = top3_rows['stock'].tolist()

    print("\n🎯 Top 3 Stocks by Highest Individual Returns:")
    for i, s in enumerate(top3_stocks, 1):
        print(f"{i}. {s}")

    # 💹 Buy % vs Sell % heatmaps for top 3
    print("\n💹 Generating Buy % vs Sell % heatmaps for top 3...")
    for stock in top3_stocks:
        best_stock_df = results_df[results_df['stock'] == stock]
        if best_stock_df.empty:
            continue
        pivot_pct = best_stock_df.pivot_table(index='buy_pct', columns='sell_pct', values='total_return', aggfunc='max')
        plt.figure(figsize=(10, 6))
        sns.heatmap(pivot_pct, annot=False, cmap='RdYlGn', center=0)
        plt.title(f'Returns Heatmap for {stock}\n(Buy % vs Sell %)')
        plt.xlabel('Sell Percentage')
        plt.ylabel('Buy Percentage')
        plt.tight_layout()
        plt.savefig(f"heatmap_buy_sell_percent_{stock.replace('.', '_')}.png")
        plt.close()

    print("\n✅ All heatmaps generated and saved successfully!")
else:
    print("⚠️ Skipping visualization due to missing or unreadable CSV.")
