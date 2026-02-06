from flask import Flask, render_template_string
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

app = Flask(__name__)

# Path to dataset (change if needed)
DATA_PATH = r"C:\Users\Valluri Suresh\Downloads\archive (1)\IOT_NETWORK_DATA.csv"

# Folder to save plots
PLOT_DIR = "static/plots"
os.makedirs(PLOT_DIR, exist_ok=True)

def generate_plots():
    df = pd.read_csv(DATA_PATH)

    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)

    plots = []

    # 1. Device type distribution
    plt.figure()
    sns.countplot(data=df, x='device_type', palette='Set2')
    plt.title('Distribution of Device Types')
    path = f"{PLOT_DIR}/device_type.png"
    plt.savefig(path)
    plt.close()
    plots.append(path)

    # 2. Protocol usage pie chart
    plt.figure()
    df['protocol_type'].value_counts().plot(
        kind='pie', autopct='%1.1f%%',
        colors=['#ff9999','#66b3ff','#99ff99']
    )
    plt.title('Protocol Usage Share')
    plt.ylabel('')
    path = f"{PLOT_DIR}/protocol_usage.png"
    plt.savefig(path)
    plt.close()
    plots.append(path)

    # 3. Energy usage by device
    plt.figure()
    sns.barplot(data=df, x='device_type', y='energy_usage', ci=None)
    plt.title('Average Energy Usage by Device Type')
    path = f"{PLOT_DIR}/energy_usage.png"
    plt.savefig(path)
    plt.close()
    plots.append(path)

    # 4. Latency vs Jitter
    plt.figure()
    sns.scatterplot(
        data=df.sample(1000),
        x='latency', y='jitter',
        hue='device_type', alpha=0.6
    )
    plt.title('Latency vs Jitter')
    path = f"{PLOT_DIR}/latency_jitter.png"
    plt.savefig(path)
    plt.close()
    plots.append(path)

    # 5. Packet loss distribution
    plt.figure()
    sns.histplot(df['packet_loss_rate'], bins=30, kde=True, color='red')
    plt.title('Packet Loss Rate Distribution')
    path = f"{PLOT_DIR}/packet_loss.png"
    plt.savefig(path)
    plt.close()
    plots.append(path)

    return plots

@app.route("/")
def index():
    plots = generate_plots()
    return render_template_string("""
        <h1>IoT Network Data Analysis</h1>
        {% for plot in plots %}
            <div style="margin-bottom:30px;">
                <img src="{{ plot }}" width="800">
            </div>
        {% endfor %}
    """, plots=plots)

if __name__ == "__main__":
    app.run(debug=True)
