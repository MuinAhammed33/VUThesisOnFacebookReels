import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
df = pd.read_csv("datasetFinal.csv")

# Create folder to save charts
output_folder = "charts"
os.makedirs(output_folder, exist_ok=True)

for col in df.columns:
    print(f"\n===== {col} =====")
    
    # Frequency & percentage
    freq = df[col].value_counts(dropna=False).sort_index()
    percent = df[col].value_counts(normalize=True, dropna=False).sort_index() * 100
    
    # Summary table
    summary = pd.DataFrame({
        'Frequency': freq,
        'Percentage (%)': percent.round(2)
    })
    
    print(summary)
    
    # Plot
    plt.figure(figsize=(5, 3))
    freq.plot(kind='bar', width=0.4)
    
    plt.title(col, fontsize=10)
    plt.xlabel('')
    plt.ylabel('Frequency', fontsize=9)
    
    plt.xticks(rotation=0, fontsize=9)
    plt.yticks(fontsize=9)
    
    # Add labels (frequency + percentage)
    for i, (val, pct) in enumerate(zip(freq, percent)):
        plt.text(i, val, f"{val}\n({pct:.1f}%)",
                 ha='center', va='bottom', fontsize=7)
    
    plt.tight_layout()
    
    # Save chart
    filename = f"{output_folder}/{col}.png"
    plt.savefig(filename, dpi=300)
    
    plt.show()