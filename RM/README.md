
# 🌱 Environmental Impact by Diet Type (Radar Visualization Project)

This project explores the environmental impact of different diet types based on multi-dimensional indicators. Using a dataset of 70,000+ participants, we compare six diet groups across seven ecological metrics with both static and interactive radar charts.

## 📊 Visualization Overview

We created radar charts using **Plotly** in Python to visually compare the following diet types:

- 🟢 **vegan**
- 🟠 **veggie**
- 🔵 **fish**
- 🔴 **meat**
- 🟣 **meat50**
- 🟤 **meat100**

### Indicators visualized:

- mean_ghgs (Greenhouse Gases)
- mean_land (Land Use)
- mean_watscar (Water Scarcity)
- mean_watuse (Water Use)
- mean_acid (Acidification)
- mean_bio (Biodiversity Impact)
- mean_eut (Eutrophication)

## 📁 File Structure

| File | Description |
|------|-------------|
| `radar_chart.py` | Python source code for data processing and radar plot generation |
| `interactive_radar_bold.html` | Interactive Plotly radar chart |
| `radar_bold_static.png` | Static radar chart image (suitable for reports or presentations) |
| `Environmental_Impact_Radar_Report.docx` | Full report with visualization and template descriptions (Word) |

## 🧼 Data Preprocessing

- Removed null and duplicate records
- Filtered participants with `n < 50`
- Grouped by `diet_group`
- Normalized indicators (min-max) to allow visual comparison

## 🔍 Key Observations

- `meat100` diet group has the highest environmental impact across all metrics.
- `vegan` diet shows consistently minimal environmental footprint.
- A gradient pattern is observed: vegan → veggie → meat → meat50 → meat100.
- Fish diets are moderate but show higher water use impacts.

## ▶️ How to Run

To run the visualization:

```bash
python radar_chart.py
```

To view interactive radar chart, open `interactive_radar_bold.html` in your browser.

## ✍️ Author

Created by [Your Name] for COMP4037 Research Methods project.

## 🌐 License

This project is shared for academic purposes only.
