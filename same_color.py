import os
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# Setting seed for reproducibility
np.random.seed(42)

# Number of charts
num_charts = 100
num_bars = 5

# Generating random heights for the bars
heights_same_color = np.random.uniform(5, 20, size=(num_charts, num_bars))

# Color for the charts with the same color
color_same_color = '#0C356A'

# Label names for the x-axis
bar_labels = ['Facebook', 'Instagram', 'WhatsApp', 'LinkedIn', 'Twitter']

# Creating a folder named 'same_color_charts' if it doesn't exist
folder_path = 'same_color_charts'
os.makedirs(folder_path, exist_ok=True)

# Defining the adjusted start date
start_date = datetime(2014, 10, 1)
end_date = start_date + timedelta(days=(num_charts * 30))
date_list = [start_date + timedelta(days=i * 30) for i in range(num_charts)]

# Plotting and saving the bar charts with the same color, labeled x-axis, and formatted dates
for i in range(num_charts):
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(bar_labels, heights_same_color[i], color=color_same_color)

    # Formatting the date as "01-month-year"
    formatted_date = date_list[i].strftime('%d-%m-%Y')

    ax.set_title(f'Redirected URLs - {formatted_date}')
    ax.set_ylim(0, 25)

    # Saving the figure inside the 'same_color_charts' folder
    file_path = os.path.join(folder_path, f'chart_{formatted_date}.png')
    plt.savefig(file_path, bbox_inches='tight')
    plt.close()

print(f'Charts with the same color, {num_bars} bars, labeled x-axis, and formatted dates saved in the {folder_path} folder.')
