
# define where the csv goes to
DESTINATION_ENV = "DESTINATION_FILE"

# the constants lst
ASSETS = [
    ("Bitcoin", "BTC-USD", "BITCOIN_DATES"),
    ("Amazon",  "AMZN",    "AMAZON_DATES"),
    ("Google",  "GOOGL",   "GOOGLE_DATES"),
]

# define columns
CSV_COLUMNS   = ("hour", "stock_type", "pct_change")

#define padding range
PADDING_HOURS = 2