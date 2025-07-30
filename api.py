from flask import Flask, request, jsonify
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Load the CSV for processing
    try:
        df = pd.read_csv(filepath)
        print("CSV content:")
        print(df.head())
        
        # 🛠️ PLACEHOLDER: call your quote generation logic here
        # For now, just return row count
        num_items = len(df)
        return jsonify({
            'message': f"File {filename} processed.",
            'rows': num_items
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
