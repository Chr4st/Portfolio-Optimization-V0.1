import yfinance as yf
import pandas as pd
import os

tickers = [
    "SCHD", "SWPPX", "SCHG", "QQQM",
    "PLTR", "MSTR", "SOFI", "MSFT", "BRK-B",
    "GOOG", "JPM", "MRK", "LULU", "UNH"
]

print("📥 Downloading data...")

raw_data = yf.download(
    tickers,
    start="1999-01-01",
    end="2024-01-01",
    group_by="ticker",
    auto_adjust=False,
    progress=True,
)

print("🔎 Processing data...")

# Try to pull "Adj Close" if possible, else fallback to "Close"
final_data = pd.DataFrame()

for ticker in tickers:
    try:
        df = raw_data[ticker]
        if "Adj Close" in df.columns:
            final_data[ticker] = df["Adj Close"]
        elif "Close" in df.columns:
            print(f"⚠️  {ticker}: No 'Adj Close' found, using 'Close'")
            final_data[ticker] = df["Close"]
        else:
            print(f"❌  {ticker}: No 'Adj Close' or 'Close' column found.")
    except KeyError:
        print(f"❌  {ticker}: Not present in the downloaded data.")

# Show a preview
print("\n📊 Final data preview:")
print(final_data.head())
print("📏 Shape:", final_data.shape)

# Only save if data is valid
if not final_data.empty:
    os.makedirs("data/raw/", exist_ok=True)
    final_data.to_csv("data/raw/my_actual_portfolio.csv")
    print("✅ Data saved to 'data/raw/my_actual_portfolio.csv'")
else:
    print("⚠️  Final data is empty — nothing was saved.")
