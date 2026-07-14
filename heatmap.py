import json
from datetime import date, timedelta
import matplotlib.pyplot as plt
import numpy as np

def load_data():
    with open("habits.json", "r") as f:
        return json.load(f)

import json
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def load_data():
    with open("habits.json", "r") as f:
        return json.load(f)

def draw_heatmap(habit_name, weeks=26):
    data = load_data()
    dates_done = set(data.get(habit_name, []))

    today = date.today()
    start = today - timedelta(days=weeks * 7)

    fig, ax = plt.subplots(figsize=(weeks / 2.2, 2.2))

    empty_color = "#EBEDF0"
    done_color = "#40C463"

    current = start
    month_labels = {}

    for week in range(weeks):
        for day in range(7):
            color = done_color if str(current) in dates_done else empty_color
            rect = patches.FancyBboxPatch(
                (week, 6 - day), 0.8, 0.8,
                boxstyle="round,pad=0,rounding_size=0.15",
                linewidth=0, facecolor=color
            )
            ax.add_patch(rect)

            if current.day <= 7 and current.month not in month_labels:
                month_labels[current.month] = week

            current += timedelta(days=1)

    month_names = ["", "Jan", "Feb", "Mar", "Apr", "May", "Jun",
                    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    for month_num, week_pos in month_labels.items():
        ax.text(week_pos, 7.3, month_names[month_num], fontsize=8, color="#57606a")

    ax.set_xlim(-0.5, weeks + 0.5)
    ax.set_ylim(-0.5, 8)
    ax.set_title(f"{habit_name}", loc="left", fontsize=11, fontweight="bold")
    ax.axis("off")

    plt.tight_layout()
    plt.savefig(f"{habit_name}_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved {habit_name}_heatmap.png")



if __name__ == "__main__":
    data = load_data()
    for habit_name in data:
        draw_heatmap(habit_name)