# Quick Start Guide

## 5-Minute Setup

Get started with subsistence risk analysis in just 5 minutes!

### Step 1: Install Python (if needed)
Download Python 3.8+ from [python.org](https://www.python.org/downloads/)

### Step 2: Clone and Setup
```bash
# Clone the repository
git clone https://github.com/fowlertc/subsistencerisk.git
cd subsistencerisk

# Install dependencies (may take 2-3 minutes)
pip install -r requirements.txt
```

### Step 3: Run the Notebook
```bash
jupyter notebook subsistence_risk_analysis.ipynb
```

### Step 4: Execute Analysis
In Jupyter:
- Click "Cell" → "Run All"
- Wait 2-5 minutes for data collection and processing
- Review the interactive maps and visualizations

### Step 5: View Results
Check the generated files:
- `subsistence_risk_map.html` - Open in browser for interactive map
- `subsistence_risk_layer.geojson` - Use in web mapping apps
- `subsistence_risk_summary.csv` - View in Excel/spreadsheet

---

## What You Get

### Interactive Maps
- **Tree Coverage Map**: Shows vegetation distribution
- **Building Density Map**: Displays infrastructure layout
- **Soil Properties Heatmap**: Visualizes soil characteristics
- **Risk Layer Map**: Combined risk assessment with color coding

### Risk Analysis
The system calculates risk based on:
- 🌳 Tree proximity (root damage potential)
- 🏢 Building density (infrastructure at risk)
- 🌍 Soil properties (shrink-swell, clay content, moisture)

### Risk Categories
- 🟢 **Low Risk** (< 0.3): Minimal subsistence concern
- 🟡 **Medium Risk** (0.3-0.6): Moderate monitoring recommended
- 🔴 **High Risk** (> 0.6): Significant subsistence potential

### Output Formats
1. **GeoJSON** - For Leaflet, Mapbox, web apps
2. **Shapefile** - For QGIS, ArcGIS, GIS software
3. **HTML** - Standalone interactive web map
4. **CSV** - Data analysis in Excel, Python, R

---

## Customization Options

### Change Study Area
Edit the bounds in the notebook:
```python
BRISTOL_BOUNDS = {
    'north': 51.5200,  # Your northern boundary
    'south': 51.4000,  # Your southern boundary
    'east': -2.5000,   # Your eastern boundary
    'west': -2.7000    # Your western boundary
}
```

### Adjust Risk Weights
Modify the risk calculation:
```python
risk_score = (
    avg_soil_risk * 0.5 +    # Adjust these weights
    tree_risk * 0.3 +         # to match your
    building_density * 0.2    # priorities
)
```

### Change Grid Resolution
For more detailed analysis:
```python
# Smaller = more detail, but slower
risk_layer = calculate_subsistence_risk(
    soil_data, tree_data, building_data,
    grid_size=0.005  # Default is 0.01
)
```

---

## Common Use Cases

### 1. Property Assessment
Check subsistence risk for a specific address:
```python
risk_info = query_risk_at_location(
    lat=51.4545, 
    lon=-2.5879, 
    risk_layer=risk_layer
)
print(risk_info)
```

### 2. Planning Applications
Export risk layer for planning documents:
```python
# High-resolution export
risk_layer.to_file('planning_risk_assessment.shp')
```

### 3. Insurance Analysis
Generate risk reports for specific zones:
```python
high_risk_areas = risk_layer[
    risk_layer['risk_category'] == 'High'
]
high_risk_areas.to_csv('high_risk_zones.csv')
```

### 4. Research & Monitoring
Track changes over time:
```python
# Run analysis periodically
# Compare risk_layer_2024 with risk_layer_2023
# Identify emerging high-risk areas
```

---

## Publishing Your Results

### As Web Map
1. Open `subsistence_risk_map.html` in browser
2. Upload to web hosting (GitHub Pages, Netlify, etc.)
3. Share the URL with stakeholders

### In GIS Software
1. Open QGIS or ArcGIS
2. Import `subsistence_risk_layer.shp`
3. Style by 'risk_category' field
4. Create custom map layouts

### As API
Serve the GeoJSON via REST API:
```python
from flask import Flask, send_file
app = Flask(__name__)

@app.route('/risk-layer')
def risk_layer():
    return send_file('subsistence_risk_layer.geojson')
```

---

## Troubleshooting

### Problem: Installation fails
**Solution**: Try installing packages individually:
```bash
pip install geopandas
pip install folium
pip install osmnx
```

### Problem: Memory error during analysis
**Solution**: Reduce study area or increase grid size:
```python
grid_size=0.02  # Coarser grid uses less memory
```

### Problem: API rate limiting
**Solution**: Wait a few minutes or reduce area size:
```python
# Analyze smaller area
BRISTOL_BOUNDS = {
    'north': 51.4700,  # Smaller area
    'south': 51.4400,
    'east': -2.5700,
    'west': -2.6000
}
```

### Problem: Notebook won't start
**Solution**: Check Jupyter installation:
```bash
pip install --upgrade jupyter
jupyter notebook
```

---

## Next Steps

1. ✅ Complete basic setup
2. 📊 Run example analysis for Bristol
3. 🗺️ Customize for your study area
4. 🔧 Adjust risk parameters
5. 📤 Export and share results
6. 🔄 Integrate real data sources (BGS, etc.)
7. 🚀 Publish your risk layers

---

## Support

- 📖 Full documentation: See `README.md`
- 🛠️ Setup issues: See `SETUP.md`
- ⚙️ Configuration: See `config_example.py`
- 🧪 Test setup: Run `python test_setup.py`
- 🐛 Report bugs: Open GitHub issue

---

## Example Output Preview

After running the notebook, expect:

```
Collected 1,234 tree/vegetation features
Collected 5,678 building features
Generated 840 soil data points
Subsistence risk layer created with 840 grid cells

Risk category distribution:
High      156 (18.6%)
Medium    348 (41.4%)
Low       336 (40.0%)

Files created:
✓ subsistence_risk_map.html
✓ subsistence_risk_layer.geojson
✓ subsistence_risk_layer.shp
✓ subsistence_risk_summary.csv
✓ soil_statistics.png
```

---

**Ready to start? Run the setup commands above and you'll be analyzing subsistence risk in minutes!** 🚀
