# 🧾 Pactle Quote Generator

A mini project to help generate quotes from messy RFQs (Request for Quotations) using fuzzy logic and basic pricing rules.

🛠️ This was built as part of a hiring assignment and is perfect for showcasing basic data parsing, mapping, and PDF generation — even without advanced coding skills.

---

## 📁 Folder Structure

.
├── main.py # Main script to run everything
├── api.py # (Optional) API layer if needed
├── input/
│ └── sample_rfq.csv # Example input data (raw product names)
├── data/
│ ├── sku_aliases.csv # Maps messy names to clean product SKUs
│ ├── price_master.csv # Product prices and details
│ └── freight_rules.json # Freight or shipping logic
├── output/
│ ├── quote.csv # Final structured CSV quote
│ ├── quote.json # JSON version
│ ├── quote.pdf # Printable quote file
│ └── log.txt # Matching + pricing steps log
├── logs.txt # Debug info
├── requirements.txt # Python dependencies
└── README.md # You're reading it!

yaml
Copy
Edit

---

## ⚙️ How to Run 

> 🐍 Make sure you have Python 3.10+ installed  
> ✅ Works on Windows, Mac, or Linux

1. **Install required packages:**

```bash
pip install -r requirements.txt
Run the program:

bash
Copy
Edit
python main.py
Check your results:

Go to the output/ folder and open:

quote.pdf for a nice visual quote

quote.csv or quote.json for structured formats

🧠 How It Works (Simple View)
Step	What it Does
1. Input Parsing	Reads messy product names from input file
2. Fuzzy Matching	Matches names like "steel bolt" to standard SKUs like "ss-bolt"
3. Pricing Logic	Adds base price, GST, discount, shipping from rule files
4. Output Gen	Creates downloadable quote in PDF, JSON, and CSV formats

💡 Notes
Useful for small manufacturers or B2B teams making frequent manual quotes.

You can easily customize the price list, aliases, and rules from data/.


📫 Contact
Made by Dhiren Suhalka
GitHub: @Dhirensuhalka
