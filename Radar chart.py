import pandas as pd
import plotly.graph_objects as go

# Loading data
df = pd.read_csv(r"D:\研究生\RM\data\Results_21Mar2022.csv")

# Data cleaning
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df = df[df['n_participants'] > 50]
df['diet_group'] = df['diet_group'].str.lower()

# Indicators and diet types
metrics = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_watuse',
           'mean_acid', 'mean_bio', 'mean_eut']
all_diets = ['vegan', 'veggie', 'fish', 'meat', 'meat50', 'meat100']

# Aggregation + Normalization
radar_data = df.groupby('diet_group')[metrics].mean()
radar_data = radar_data.loc[radar_data.index.isin(all_diets)]
radar_norm = (radar_data - radar_data.min()) / (radar_data.max() - radar_data.min())

# Radar chart configuration
categories = metrics + [metrics[0]]

# Custom colors
custom_colors = {
    'vegan': '#2ca02c',
    'veggie': '#ff7f0e',
    'fish': '#1f77b4',
    'meat': '#d62728',
    'meat50': '#9467bd',
    'meat100': '#8c564b'
}

# Create a chart
fig = go.Figure()

for diet in all_diets:
    values = radar_norm.loc[diet].tolist()
    values += values[:1]
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name=diet,
        line=dict(color=custom_colors[diet], width=5),
        marker=dict(size=6),
        opacity=0.6
    ))

# Graphic style settings with bigger fonts
fig.update_layout(
    title='Interactive Radar Chart: Environmental Impact by Diet Type (Cleaned Data)',
    font=dict(size=20),  # Set the global font size
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1],
            tickvals=[0.2, 0.4, 0.6, 0.8, 1.0],
            tickfont=dict(size=20)  # Set radial coordinate font size
        ),
        angularaxis=dict(
            tickfont=dict(size=20)  # Set the angle label font
        )
    ),
    legend=dict(font=dict(size=20)),  # Legend font size
    title_font=dict(size=25)  # Title Font Size
)

# Show and save
fig.show()
fig.write_html(r"D:\研究生\RM\data\interactive_radar_bold.html")





