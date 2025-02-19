from flask import Flask, render_template_string, jsonify
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.utils
import json

app = Flask(__name__)

# Homepage HTML template
HOME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Data Analytics Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <style>
        body { padding: 2rem; background: #f0f2f6; }
        .container { background: white; padding: 2rem; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-4">Data Analytics Dashboard 📊</h1>
        <div id="chart"></div>
        <div class="mt-4">
            <h3>Sample Data Analysis</h3>
            <p>This is a simple data visualization dashboard showing random data patterns.</p>
        </div>
    </div>
    <script>
        // Load the initial chart
        fetch('/get_chart_data')
            .then(response => response.json())
            .then(data => {
                Plotly.newPlot('chart', data.data, data.layout);
            });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/get_chart_data')
def get_chart_data():
    # Generate sample data
    np.random.seed(42)
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    values = np.random.normal(loc=100, scale=15, size=len(dates))
    df = pd.DataFrame({'Date': dates, 'Value': values})
    
    # Create the plot
    fig = px.line(df, x='Date', y='Value', title='Time Series Analysis')
    fig.update_layout(
        template='plotly_white',
        title_x=0.5,
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    # Convert the plot to JSON
    chart_json = json.loads(fig.to_json())
    
    return jsonify(chart_json)

if __name__ == '__main__':
    app.run()
