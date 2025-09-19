import csv, sys
import matplotlib.pyplot as plt

episodes, mean_scores = [], []
with open('scores.csv', newline='') as f:
    r = csv.DictReader(f)
    for row in r:
        episodes.append(int(row['episode']))
        mean_scores.append(float(row['mean']))

plt.plot(episodes, mean_scores)
plt.xlabel('episode'); plt.ylabel('score (mean)')
plt.title('Mean score over training')
plt.tight_layout()


# ✅ 自動存成 PNG
plt.savefig("scores.png", dpi=150, bbox_inches="tight")
print("Saved: scores.png")

plt.show()