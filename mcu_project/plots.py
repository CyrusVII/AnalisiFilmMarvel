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
    
    
def roi(df):
    # 5. Grafico ROI 
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(16, 8))

    bars = ax.bar(df['movie'], df['roi'], color='#1f77b4', edgecolor='black')
    ax.set_title("Return on Investment (ROI) - Marvel Cinematic Universe", fontsize=18, weight='bold')
    ax.set_xlabel("Film", fontsize=12)
    ax.set_ylabel("ROI", fontsize=12)
    ax.set_xticks(range(len(df)))
    ax.set_xticklabels(df['movie'], rotation=75, ha='right', fontsize=9)
    ax.yaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    ax.set_ylim(0, df['roi'].max() + 1)

    # Aggiunta etichette sopra le barre
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # spostamento in pixel
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

    plt.tight_layout()
    plt.show()
