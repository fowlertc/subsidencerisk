# Example Outputs and Use Cases

This document shows example outputs and use cases for the Subsistence Risk Analysis system.

## Sample Output Files

When you run the notebook, you'll generate these files:

### 1. Interactive Risk Map (HTML)
**File**: `subsistence_risk_map.html`

A fully interactive web map with:
- Zoom and pan controls
- Risk layer color-coded by severity
- Clickable cells showing detailed risk scores
- Legend for risk categories
- Multiple base map options

**How to use**: 
- Open in any web browser
- Zoom to areas of interest
- Click on grid cells to see detailed information
- Share via web hosting

### 2. GeoJSON Risk Layer
**File**: `subsistence_risk_layer.geojson`

Standard GeoJSON format containing:
```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Polygon",
        "coordinates": [[[lon, lat], ...]]
      },
      "properties": {
        "risk_score": 0.65,
        "risk_category": "High",
        "soil_risk": 0.72,
        "tree_risk": 0.58,
        "building_density": 0.45
      }
    },
    ...
  ]
}
```

**How to use**:
- Import into Leaflet, Mapbox, or Google Maps
- Use with JavaScript mapping libraries
- Convert to other formats with GDAL

### 3. Shapefile
**Files**: `subsistence_risk_layer.shp`, `.shx`, `.dbf`, `.prj`

Standard ESRI Shapefile format for:
- QGIS
- ArcGIS
- MapInfo
- Other desktop GIS software

**How to use**:
1. Open QGIS/ArcGIS
2. Add Vector Layer
3. Select the .shp file
4. Style by 'risk_category' attribute

### 4. Summary CSV
**File**: `subsistence_risk_summary.csv`

Tabular data with columns:
```csv
risk_score,risk_category,soil_risk,tree_risk,building_density,centroid_lon,centroid_lat
0.65,High,0.72,0.58,0.45,-2.5879,51.4545
0.42,Medium,0.45,0.38,0.42,-2.5869,51.4555
...
```

**How to use**:
- Open in Excel or Google Sheets
- Import into R or Python for further analysis
- Create custom reports and charts
- Join with other datasets by location

### 5. Statistical Plots
**File**: `soil_statistics.png`

Visual summary including:
- Soil type distribution (bar chart)
- Clay content distribution (histogram)
- Shrink-swell potential (histogram)
- Moisture content distribution (histogram)

**How to use**:
- Include in reports and presentations
- Use for quality control and validation
- Compare across different study areas

### 6. Analysis Report
**File**: `subsistence_risk_report.txt`

Text summary containing:
- Study area information
- Risk distribution statistics
- Analysis parameters
- List of generated outputs

---

## Use Case Examples

### Use Case 1: Property Development Planning

**Scenario**: A developer wants to assess subsistence risk before building new homes.

**Process**:
1. Run analysis for the development site area
2. Identify high-risk zones
3. Adjust building placement to avoid high-risk areas
4. Include risk assessment in planning application

**Code**:
```python
# Focus on development site
SITE_BOUNDS = {
    'north': 51.4650,
    'south': 51.4550,
    'east': -2.5750,
    'west': -2.5850
}

# Run analysis with fine resolution
risk_layer = calculate_subsistence_risk(
    soil_data, tree_data, building_data,
    grid_size=0.002  # ~200m resolution
)

# Export for planning documents
risk_layer.to_file('development_site_risk.shp')
```

**Output**: Detailed risk map showing where buildings can be safely placed.

---

### Use Case 2: Insurance Risk Assessment

**Scenario**: An insurance company needs to assess risk for properties in a portfolio.

**Process**:
1. Load property addresses
2. Query risk score for each address
3. Calculate risk-adjusted premiums
4. Generate risk report by postcode

**Code**:
```python
# Load property portfolio
properties = pd.read_csv('property_portfolio.csv')

# Query risk for each property
for idx, row in properties.iterrows():
    risk = query_risk_at_location(
        row['latitude'], 
        row['longitude'],
        risk_layer
    )
    properties.loc[idx, 'risk_score'] = risk['risk_score']
    properties.loc[idx, 'risk_category'] = risk['risk_category']

# Calculate risk-adjusted premiums
properties['base_premium'] = 500  # £500 base
properties['risk_multiplier'] = 1 + properties['risk_score']
properties['total_premium'] = (
    properties['base_premium'] * 
    properties['risk_multiplier']
)

# Export results
properties.to_csv('risk_adjusted_premiums.csv')
```

**Output**: CSV file with risk scores and calculated premiums for each property.

---

### Use Case 3: Local Authority Planning Policy

**Scenario**: A council needs to update planning policies based on subsistence risk.

**Process**:
1. Run analysis for entire council area
2. Identify high-risk zones
3. Create planning zones with different requirements
4. Publish risk map for public consultation

**Code**:
```python
# Analyze entire council area
COUNCIL_BOUNDS = {
    'north': 51.5500,
    'south': 51.4000,
    'east': -2.5000,
    'west': -2.7000
}

# Generate risk layer
risk_layer = calculate_subsistence_risk(
    soil_data, tree_data, building_data
)

# Define planning zones
high_risk_zones = risk_layer[
    risk_layer['risk_category'] == 'High'
].copy()

# Calculate total area at risk
high_risk_zones['area_km2'] = (
    high_risk_zones.geometry.area * 12100  # degrees to km²
)
total_high_risk = high_risk_zones['area_km2'].sum()

print(f"Total high-risk area: {total_high_risk:.2f} km²")

# Export for policy documents
high_risk_zones.to_file('planning_policy_high_risk_zones.shp')
risk_map.save('public_consultation_map.html')
```

**Output**: Shapefile of high-risk zones and public-facing web map.

---

### Use Case 4: Infrastructure Maintenance Planning

**Scenario**: A utility company plans maintenance priorities based on ground conditions.

**Process**:
1. Overlay utility network with risk layer
2. Identify assets in high-risk areas
3. Prioritize inspection and maintenance
4. Plan preventative measures

**Code**:
```python
# Load utility network
utility_network = gpd.read_file('utility_assets.shp')

# Spatial join with risk layer
utility_risk = gpd.sjoin(
    utility_network,
    risk_layer,
    how='left',
    predicate='intersects'
)

# Calculate priority scores
utility_risk['priority'] = (
    utility_risk['risk_score'] * 
    utility_risk['asset_value'] / 1000
)

# Sort by priority
maintenance_plan = utility_risk.sort_values(
    'priority', 
    ascending=False
)

# Export high-priority assets
high_priority = maintenance_plan[
    maintenance_plan['priority'] > 50
]
high_priority.to_csv('high_priority_maintenance.csv')
```

**Output**: Prioritized list of assets requiring maintenance.

---

### Use Case 5: Research and Monitoring

**Scenario**: Researchers study how subsistence risk changes over time.

**Process**:
1. Run analysis for multiple time periods
2. Compare risk layers
3. Identify areas with increasing risk
4. Analyze contributing factors

**Code**:
```python
# Analyze two time periods
risk_2023 = calculate_subsistence_risk(
    soil_data_2023, tree_data_2023, building_data_2023
)

risk_2024 = calculate_subsistence_risk(
    soil_data_2024, tree_data_2024, building_data_2024
)

# Calculate change
risk_change = risk_2024.copy()
risk_change['risk_change'] = (
    risk_2024['risk_score'] - 
    risk_2023['risk_score']
)

# Identify increasing risk areas
increasing_risk = risk_change[
    risk_change['risk_change'] > 0.1
]

print(f"Areas with increasing risk: {len(increasing_risk)}")

# Visualize changes
plt.figure(figsize=(12, 6))
plt.hist(risk_change['risk_change'], bins=50)
plt.xlabel('Risk Score Change')
plt.ylabel('Frequency')
plt.title('Distribution of Risk Changes (2023-2024)')
plt.savefig('risk_change_analysis.png')
```

**Output**: Analysis of temporal changes in subsistence risk.

---

## Integration Examples

### Web Application Integration

```javascript
// Example: Leaflet map with risk layer
const map = L.map('map').setView([51.4545, -2.5879], 12);

// Load risk layer
fetch('subsistence_risk_layer.geojson')
  .then(response => response.json())
  .then(data => {
    L.geoJSON(data, {
      style: feature => ({
        fillColor: getRiskColor(feature.properties.risk_score),
        weight: 1,
        fillOpacity: 0.6
      }),
      onEachFeature: (feature, layer) => {
        layer.bindPopup(`
          <b>Risk:</b> ${feature.properties.risk_category}<br>
          <b>Score:</b> ${feature.properties.risk_score.toFixed(2)}
        `);
      }
    }).addTo(map);
  });

function getRiskColor(score) {
  return score < 0.3 ? '#2ecc71' :
         score < 0.6 ? '#f39c12' : '#e74c3c';
}
```

### Python Analysis Integration

```python
# Example: Load and analyze risk data
import geopandas as gpd
import pandas as pd

# Load risk layer
risk_layer = gpd.read_file('subsistence_risk_layer.geojson')

# Statistical analysis
print("Risk Statistics:")
print(risk_layer.groupby('risk_category')['risk_score'].agg([
    'count', 'mean', 'min', 'max', 'std'
]))

# Spatial queries
def get_nearby_high_risk(lat, lon, radius_km=1):
    """Find high-risk areas near a location."""
    from shapely.geometry import Point
    
    point = Point(lon, lat)
    buffer = point.buffer(radius_km / 111)  # Approximate degrees
    
    nearby = risk_layer[risk_layer.intersects(buffer)]
    high_risk = nearby[nearby['risk_category'] == 'High']
    
    return high_risk

# Example query
result = get_nearby_high_risk(51.4545, -2.5879, radius_km=2)
print(f"Found {len(result)} high-risk areas within 2km")
```

---

## Performance Benchmarks

Typical performance on a standard laptop (i5, 8GB RAM):

| Study Area Size | Grid Resolution | Processing Time | Output Size |
|----------------|-----------------|-----------------|-------------|
| 5 km × 5 km    | 0.01° (~1km)    | 1-2 minutes     | 2-5 MB      |
| 10 km × 10 km  | 0.01° (~1km)    | 3-5 minutes     | 8-15 MB     |
| 20 km × 20 km  | 0.01° (~1km)    | 10-15 minutes   | 30-50 MB    |
| 5 km × 5 km    | 0.005° (~500m)  | 5-8 minutes     | 10-20 MB    |

*Times include data collection from OpenStreetMap API*

---

## Tips for Best Results

1. **Start small**: Begin with a small study area to test the workflow
2. **Adjust weights**: Tune risk calculation weights based on local conditions
3. **Validate results**: Compare with known subsistence events
4. **Use real data**: Replace synthetic soil data with real API data when possible
5. **Cache data**: Save downloaded data to avoid repeated API calls
6. **Document assumptions**: Record all parameters and assumptions
7. **Regular updates**: Re-run analysis periodically to capture changes

---

## Further Resources

- [GeoPandas Documentation](https://geopandas.org/)
- [Folium Examples](https://python-visualization.github.io/folium/)
- [OpenStreetMap Wiki](https://wiki.openstreetmap.org/)
- [British Geological Survey](https://www.bgs.ac.uk/)
- [QGIS Tutorials](https://www.qgistutorials.com/)
