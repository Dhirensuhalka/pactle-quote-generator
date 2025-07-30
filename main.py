from flask import Flask, request, jsonify
import os
import csv

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return jsonify({"message": "Quote Generator API Running"})

@app.route('/upload', methods=['POST'])
def upload_file():
    print("✅ /upload endpoint hit")

    if 'file' not in request.files:
        print("❌ No file part in request")
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        print("❌ No selected file")
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    print(f"📁 File saved to: {filepath}")

    try:
        mapped_skus = []
        with open(filepath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(f"🔍 Processing row: {row}")
                if row:
                    item = row[0].strip()
                    # Dummy mapping
                    if '20mm' in item:
                        mapped_skus.append('NFC20')
                    elif '10mm' in item:
                        mapped_skus.append('NFC10')
                    else:
                        mapped_skus.append('UNKNOWN')

        output_file_path = os.path.join(OUTPUT_FOLDER, 'quote.csv')
        with open(output_file_path, 'w', newline='') as outfile:
            writer = csv.writer(outfile)
            for sku in mapped_skus:
                writer.writerow([sku])

        print("✅ Mapping complete")
        return jsonify({
            "status": "success",
            "mapped_skus": mapped_skus,
            "output_file": output_file_path
        }), 200

    except Exception as e:
        print(f"❌ Exception: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
