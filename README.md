# 🧾 Pactle Quote Generator

This mini-project helps generate quotes from messy RFQs (Request for Quotations) using simple rules, fuzzy matching, and pricing logic.

🛠️ Built as part of a hiring assignment — it shows how to parse input, match items, apply taxes/shipping, and create downloadable quote files like PDF, CSV, and JSON.

---

## 📁 Folder Structure

.
├── main.py # Main script to run everything
├── api.py # Optional Flask API (for advanced use)
├── input/
│ └── sample_rfq.csv # Example RFQ input with messy item names
├── data/
│ ├── sku_aliases.csv # Maps raw item names to proper SKUs
│ ├── price_master.csv # Pricing data for each SKU
│ └── freight_rules.json# Freight charges or thresholds
├── output/
│ ├── quote.csv # Final structured quote (spreadsheet)
│ ├── quote.json # JSON version for ERP/API use
│ ├── quote.pdf # Printable human-friendly quote
│ └── log.txt # Shows how items were matched & priced
├── logs.txt # Debug log (optional)
├── requirements.txt # Required Python packages
└── README.md # This file!

yaml
Copy
Edit

---

## ⚙️ How to Run (Beginner Friendly)

> 🐍 Make sure Python 3.10 or above is installed  
> ✅ Works on Windows, Mac, or Linux

### Step-by-step:

1. Open your terminal or command prompt in the project folder  
2. Install required packages:

```bash
pip install -r requirements.txt
Run the program:

bash
Copy
Edit
python main.py
After running, check the output/ folder:

quote.pdf → nicely formatted quote

quote.csv or quote.json → machine-readable formats

log.txt → explains how items were matched & priced

🧠 How It Works (Simple View)
Step	What it Does
Input Parsing	Reads messy product names from RFQ CSV
Fuzzy Matching	Maps names like “steel bolt 12mm” → SKU SB12
Pricing Logic	Adds price, GST, discount, shipping using rules
Output Gen	Creates PDF, CSV, and JSON versions of the quote

💡 Notes
No AI or external tools used — just clean Python logic

Rules and pricing are fully editable in the data/ folder

Useful for small businesses doing manual quotes frequently

Easy to extend into a full product with backend/API

