import pandas as pd
import plotly.graph_objects as go

# === Step 1: 加载数据 ===
df = pd.read_csv(r"D:\研究生\RM\data\Results_21Mar2022.csv")

# === Step 2: 基础清洗 ===
df.dropna(inplace=True)  # 删除缺失值
df.drop_duplicates(inplace=True)  # 删除重复值
df = df[df['n_participants'] > 50]  # 只保留参与人数大于50的记录
df['diet_group'] = df['diet_group'].str.lower()  # 统一为小写

# === Step 3: 指标和饮食类型设定 ===
metrics = ['mean_ghgs', 'mean_land', 'mean_watscar', 'mean_watuse',
           'mean_acid', 'mean_bio', 'mean_eut']
all_diets = ['vegan', 'veggie', 'fish', 'meat', 'meat50', 'meat100']

# === Step 4: 异常值处理（IQR 方法）===
Q1 = df[metrics].quantile(0.25)
Q3 = df[metrics].quantile(0.75)
IQR = Q3 - Q1

# 识别异常值
outliers_iqr = ((df[metrics] < (Q1 - 1.5 * IQR)) | (df[metrics] > (Q3 + 1.5 * IQR))).any(axis=1)
df = df[~outliers_iqr]  # 删除异常值

# === Step 5: 分组求均值 + 归一化 ===
radar_data = df.groupby('diet_group')[metrics].mean()
radar_data = radar_data.loc[radar_data.index.isin(all_diets)]  # 只保留目标饮食组
radar_norm = (radar_data - radar_data.min()) / (radar_data.max() - radar_data.min())

# === Step 6: 雷达图设置 ===
categories = metrics + [metrics[0]]

# 自定义颜色
custom_colors = {
    'vegan': '#2ca02c',
    'veggie': '#ff7f0e',
    'fish': '#1f77b4',
    'meat': '#d62728',
    'meat50': '#9467bd',
    'meat100': '#8c564b'
}

# 创建图表
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

# 图表样式
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

# 显示 + 保存
fig.show()
fig.write_html(r"D:\研究生\RM\data\interactive_radar_outliers_removed.html")





