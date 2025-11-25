# Subsistence Risk Analysis for Bristol

A comprehensive geospatial analysis toolkit for assessing subsistence risk based on tree, building, and soil data.

## Overview

This project provides a Jupyter notebook-based workflow for collecting, analyzing, and visualizing subsistence risk data. The analysis combines multiple geospatial datasets to identify areas with potential subsistence risk in the Bristol area.

## Features

- **Multi-source Data Collection**: Integrates with various APIs including OpenStreetMap
- **Comprehensive Analysis**: Combines soil characteristics, tree proximity, and building density
- **Interactive Visualization**: Creates interactive maps using Folium and static plots with Matplotlib
- **Risk Scoring**: Multi-factor risk calculation with customizable weights
- **Multiple Export Formats**: GeoJSON, Shapefile, HTML, CSV
- **Query Tools**: Location-based risk queries and automated reporting
- **Extensible Framework**: Easy to integrate additional data sources and APIs

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook or JupyterLab

### Setup

1. Clone the repository:
```bash
git clone https://github.com/fowlertc/subsistencerisk.git
cd subsistencerisk
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter:
```bash
jupyter notebook subsistence_risk_analysis.ipynb
```

## Usage

### Quick Start

1. Open `subsistence_risk_analysis.ipynb` in Jupyter
2. Run all cells sequentially (Cell → Run All)
3. The notebook will:
   - Collect data from OpenStreetMap
   - Generate synthetic soil data (replace with real API in production)
   - Calculate subsistence risk scores
   - Create interactive visualizations
   - Export results in multiple formats

### Outputs

The notebook generates the following files:

- `subsistence_risk_map.html` - Interactive web map
- `subsistence_risk_layer.geojson` - GeoJSON format for web applications
- `subsistence_risk_layer.shp` (+ .shx, .dbf, .prj) - Shapefile for GIS software
- `subsistence_risk_summary.csv` - Summary statistics and data
- `subsistence_risk_report.txt` - Analysis report
- `soil_statistics.png` - Statistical visualizations
- `leaflet_integration_example.html` - Web integration template

### Customization

#### Study Area

Modify the `BRISTOL_BOUNDS` dictionary in the notebook to analyze different areas:

```python
BRISTOL_BOUNDS = {
    'north': 51.5200,
    'south': 51.4000,
    'east': -2.5000,
    'west': -2.7000
}
```

#### Risk Calculation Weights

Adjust risk factor weights in the `calculate_subsistence_risk()` function:

```python
risk_score = (
    avg_soil_risk * 0.5 +    # Soil factors
    tree_risk * 0.3 +         # Tree proximity
    building_density * 0.2    # Building density
)
```

#### Grid Resolution

Change the `grid_size` parameter for different analysis resolutions:

```python
risk_layer = calculate_subsistence_risk(
    soil_data, 
    tree_data, 
    building_data,
    grid_size=0.01  # Smaller = higher resolution
)
```

## Data Sources

### Current

- **OpenStreetMap (OSM)**: Building and tree data via OSMnx
- **Synthetic Soil Data**: Generated for demonstration

### Recommended Additional Sources

1. **British Geological Survey (BGS) API**
   - Geological data
   - Ground stability information
   - Historical subsidence records

2. **UK Environment Agency**
   - Flood risk data
   - Water table levels

3. **Met Office Weather API**
   - Rainfall patterns
   - Drought conditions

4. **European Soil Data Centre (ESDAC)**
   - Soil composition
   - Moisture content
   - Clay distribution

## Risk Factors

The analysis considers three main factors:

1. **Soil Conditions (50% weight)**
   - Shrink-swell potential
   - Clay content
   - Moisture levels

2. **Tree Proximity (30% weight)**
   - Distance to large trees
   - Vegetation density
   - Root damage potential

3. **Building Density (20% weight)**
   - Infrastructure concentration
   - Building footprints
   - Development patterns

## Publishing Options

The generated risk layers can be published via:

1. **Static Web Hosting**: Upload HTML files to any web server
2. **GIS Platforms**: Import Shapefiles to QGIS, ArcGIS
3. **Web Mapping Services**: 
   - Mapbox
   - ArcGIS Online
   - Carto
   - Google Earth Engine
4. **API Service**: Serve GeoJSON via REST API
5. **Tile Server**: Convert to raster tiles for performance

## API Integration

To integrate additional APIs, use the template in section 9 of the notebook:

```python
def integrate_external_api(api_url, params):
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    return response.json()
```

## Contributing

Contributions are welcome! Areas for improvement:

- Integration with real soil data APIs
- Historical subsidence data incorporation
- Machine learning-based risk prediction
- Real-time data updates
- Additional visualization types
- Mobile app integration

## License

This project is provided as-is for educational and research purposes.

## Acknowledgments

- OpenStreetMap contributors for geospatial data
- OSMnx library for OpenStreetMap integration
- GeoPandas and Folium for geospatial analysis and visualization

## Contact

For questions or collaboration opportunities, please open an issue on GitHub.

## References

- [OpenStreetMap](https://www.openstreetmap.org/)
- [British Geological Survey](https://www.bgs.ac.uk/)
- [GeoPandas Documentation](https://geopandas.org/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [OSMnx Documentation](https://osmnx.readthedocs.io/)
