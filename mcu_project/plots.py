import matplotlib.pyplot as plt

def plot_roi(df):
    plt.figure(figsize=(14, 6))
    bars = plt.bar(df['movie'], df['roi'], color='dodgerblue', edgecolor='black')
    plt.title("ROI per Film MCU", fontsize=16, weight='bold')
    plt.xlabel("Film", fontsize=12)
    plt.ylabel("ROI", fontsize=12)
    plt.xticks(rotation=75, ha='right', fontsize=8)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1, f'{height:.2f}', ha='center', fontsize=8)

    plt.tight_layout()
    plt.show()
