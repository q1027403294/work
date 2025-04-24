
# COMP4037 Coursework 2: Environmental Impact Visualization

This repository contains the full implementation of a radar chart-based data visualization project for COMP4037 - Research Methods. The focus is on comparing environmental impacts of various diet types using Python and Plotly.

## Project Summary

This project investigates the environmental consequences of six diet types using a cleaned dataset with over 70,000 records. The analysis includes multiple ecological indicators, grouped and visualized using radar charts to show cross-dimensional comparisons.

## Visualization Approach

A **Radar Chart** is used to represent normalized environmental metrics across six distinct diet types:

- Vegan
- Vegetarian
- Fish-eater
- Meat-eater
- Moderate meat-eater (meat50)
- High meat-intake (meat100)

Environmental indicators included:

- Greenhouse gas emissions (mean_ghgs)
- Land usage (mean_land)
- Water scarcity (mean_watscar)
- Water usage (mean_watuse)
- Acidification potential (mean_acid)
- Biodiversity impact (mean_bio)
- Eutrophication (mean_eut)

## Data Processing Pipeline

1. Load and inspect dataset (`Results_21Mar2022.csv`)
2. Remove null values and duplicates
3. Filter out diet groups with fewer than 50 participants
4. Remove outliers using IQR method
5. Group data by `diet_group` and calculate mean environmental scores
6. Normalize each indicator using min-max scaling
7. Generate radar chart using Plotly
8. Export both interactive `.html` and static

## Project Structure

```
.
├── data/
│   └── Results_21Mar2022.csv
├── code/
│   └── radar_chart.py
├── figures/
│   ├── radar_bold_static.png
│   └── interactive_radar_bold.html
├── docs/
│   └── Environmental_Impact_Radar_Report.docx
└── README.md
```

## Key Insights

- The **meat100** group consistently shows the highest environmental impact across all indicators.
- **Vegan** and **vegetarian** diets exhibit the lowest environmental footprint.
- Fish diets rank in the middle but show relatively higher water-related stress.
- A clear gradient appears from vegan → veggie → meat50 → meat100, reflecting diet-driven ecological load.

## Technologies Used

- Python 3.11
- pandas
- plotly
- kaleido (for saving PNG)
- Word (for reporting)

## License

Academic use only, for COMP4037 coursework submission.

---

Created by Jinxu Qi
