import json
import calendar
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def load_data():
    with open("habits.json", "r") as f:
        return json.load(f)


def draw_grid(month=None, year=None):
    data = load_data()
    today = date.today()
    month = month or today.month
    year = year or today.year
    days_in_month = calendar.monthrange(year, month)[1]

    habits = list(data.keys())

    bg_color = "#0d0d0d"
    empty_color = "#1a1a1a"
    done_color = "#8b5cf6"
    border_color = "#333333"
    text_color = "#e5e5e5"

    fig, ax = plt.subplots(figsize=(days_in_month * 0.4 + 2, len(habits) * 0.5 + 1.5))
    fig.patch.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    for row, habit in enumerate(habits):
        y = len(habits) - row
        dates_done = set(data.get(habit, []))

        ax.text(-0.3, y + 0.4, habit, fontsize=9, color=text_color,
                ha="right", va="center")

        for day in range(1, days_in_month + 1):
            date_str = f"{year}-{month:02d}-{day:02d}"
            color = done_color if date_str in dates_done else empty_color
            rect = patches.FancyBboxPatch(
                (day, y), 0.75, 0.75,
                boxstyle="round,pad=0,rounding_size=0.12",
                linewidth=0.8, edgecolor=border_color, facecolor=color
            )
            ax.add_patch(rect)

    for day in range(1, days_in_month + 1):
        ax.text(day + 0.35, len(habits) + 0.6, str(day), fontsize=6,
                 color=text_color, ha="center")

    ax.set_xlim(-6, days_in_month + 1.5)
    ax.set_ylim(0, len(habits) + 1.5)
    ax.axis("off")

    month_name = calendar.month_name[month]
    ax.set_title(f"{month_name} {year}", loc="left", fontsize=13,
                 color=text_color, fontweight="bold")

    plt.tight_layout()
    plt.savefig("habit_grid.png", dpi=150, facecolor=bg_color, bbox_inches="tight")
    plt.close()
    print("Saved habit_grid.png")


if __name__ == "__main__":
    draw_grid()