import pandas as pd
import plotly.graph_objects as go

# Loading data
df = pd.read_csv(r"D:\研究生\RM\RM\data\Results_21Mar2022.csv")

# Basic cleaning
df.dropna(inplace=True)  # Remove missing values
df.drop_duplicates(inplace=True)  # Remove duplicate values
df = df[df['n_participants'] > 50]  # Only keep records with more than 50 participants
df['diet_group'] = df['diet_group'].str.lower()  # Unified to lowercase

# Indicators and diet type settings
metrics = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_watuse',
           'mean_acid', 'mean_bio', 'mean_eut']
all_diets = ['vegan', 'veggie', 'fish', 'meat', 'meat50', 'meat100']

# Outlier handling (IQR method)
Q1 = df[metrics].quantile(0.25)
Q3 = df[metrics].quantile(0.75)
IQR = Q3 - Q1

# Identifying outliers
outliers_iqr = ((df[metrics] < (Q1 - 1.5 * IQR)) | (df[metrics] > (Q3 + 1.5 * IQR))).any(axis=1)
df = df[~outliers_iqr]  # Remove outliers

# Group mean + normalization
radar_data = df.groupby('diet_group')[metrics].mean()
radar_data = radar_data.loc[radar_data.index.isin(all_diets)]  # Only the target diet group was retained
radar_norm = (radar_data - radar_data.min()) / (radar_data.max() - radar_data.min())

# Radar chart settings
categories = metrics + [metrics[0]]

# Custom Colors
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
    if diet in radar_norm.index:
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

# Chart Style
fig.update_layout(
    title='Interactive Radar Chart: Environmental Impact by Diet Type (Cleaned & Outliers Removed)',
    font=dict(size=20),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1],
            tickvals=[0.2, 0.4, 0.6, 0.8, 1.0],
            tickfont=dict(size=20)
        ),
        angularaxis=dict(
            tickfont=dict(size=20)
        )
    ),
    legend=dict(font=dict(size=20)),
    title_font=dict(size=25)
)

# Show + Save
fig.show()
fig.write_html(r"D:\研究生\RM\RM\data\interactive_radar_outliers_removed.html")





