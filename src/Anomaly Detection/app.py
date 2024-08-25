from flask import Flask, render_template, request, jsonify, send_file
import pandas as pd
import joblib
from pycaret.anomaly import *
import io

app = Flask(__name__, static_url_path='/static')

model = joblib.load('knn_pipeline1.pkl')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/multiple_transactions')
def multiple_transactions():
    return render_template('multi.html')

@app.route('/predict', methods=['POST'])
def predict():

    fiscal_year = request.form.get('fiscalYear')
    fiscal_month = request.form.get('fiscalMonth')
    div_name = request.form.get('divName')
    merchant = request.form.get('merchant')
    cat_desc = request.form.get('catDesc')
    trans_date = request.form.get('transDate')
    amount = int(float(request.form['amount']))

    data = {
        'FISCAL_YR': [fiscal_year],
        'FISCAL_MTH': [fiscal_month],
        'DIV_NAME': [div_name],
        'MERCHANT': [merchant],
        'CAT_DESC': [cat_desc],
        'TRANS_DT': [trans_date],
        'AMT': [amount]
    }

    df = pd.DataFrame(data)

    df['TRANS_DT'] = pd.to_datetime(df['TRANS_DT'], format='%Y-%m-%d', errors='coerce')

    prediction = model.predict(df)

    if prediction == 1:
        result = "This transaction might be fraudulent and should be investigated!"
    else:
        result = "This transaction is approved."

    return render_template('result.html',
                           fiscal_yr=fiscal_year,
                           fiscal_mth=fiscal_month,
                           div_name=div_name,
                           merchant=merchant,
                           cat_desc=cat_desc,
                           trans_dt=trans_date,
                           amount=amount,
                           result=result)

@app.route('/predict_multiple', methods=['POST'])
def predict_multiple():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    if file and file.filename.endswith('.csv'):
        df = pd.read_csv(file)
        
        if not {'FISCAL_YR', 'FISCAL_MTH', 'DIV_NAME', 'MERCHANT', 'CAT_DESC', 'TRANS_DT', 'AMT'}.issubset(df.columns):
            return jsonify({"error": "CSV file must contain the required columns."})

        df['TRANS_DT'] = pd.to_datetime(df['TRANS_DT'], errors='coerce')

        predictions = model.predict(df)
        
        df['Anomaly'] = ['fraudulent' if pred == 1 else 'legitimate' for pred in predictions]
        
        # Save updated DataFrame to a CSV file
        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)
        
        # Send the file as a download
        return send_file(
            io.BytesIO(output.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name='predictions_with_anomalies.csv'
        )
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV file."})
    
@app.route('/api_documentation')
def api_documentation():
    return render_template('api_doc.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
