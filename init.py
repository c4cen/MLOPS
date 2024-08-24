from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__, static_url_path='/static')

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

    data = {
        'FISCAL_YR': [fiscal_year],
        'FISCAL_MTH': [fiscal_month],
        'DIV_NAME': [div_name],
        'MERCHANT': [merchant],
        'CAT_DESC': [cat_desc],
        'TRANS_DT': [trans_date]
    }

    df = pd.DataFrame(data)

    # Perform prediction logic here
    result = "This transaction might be fraudulent and should be investigated!"  # Replace with actual prediction result

    return render_template('result.html',
                           fiscal_yr=fiscal_year,
                           fiscal_mth=fiscal_month,
                           div_name=div_name,
                           merchant=merchant,
                           cat_desc=cat_desc,
                           trans_dt=trans_date,
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
        # Here you can add code to make predictions using your model
        # For now, let's just return the DataFrame as JSON for demonstration
        return jsonify(df.to_dict(orient='records'))
    else:
        return jsonify({"error": "Invalid file format. Please upload a CSV file."})

if __name__ == '__main__':
    app.run(debug=True)