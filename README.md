# Subsidence Risk Analysis for Bristol

A geospatial analysis tool for assessing **building-level subsidence risk** based on soil type and tree proximity.

## Overview

This project calculates subsidence risk scores (0-10) for individual buildings by combining:

- **🌍 Soil Data** - From British Geological Survey (BGS) WMS service
- **🌳 Tree Data** - From Bristol City Council API (55,000+ trees)
- **🏠 Building Data** - From OpenStreetMap (227,000+ buildings)

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv subsidence
.\subsidence\Scripts\Activate.ps1  # Windows
source subsidence/bin/activate      # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### 2. Run the Notebook

```bash
jupyter notebook subsidence_risk_analysis.ipynb
```

Run cells sequentially. The notebook will:
1. Fetch tree data from Bristol City Council API
2. Fetch building footprints from OpenStreetMap
3. Fetch soil data from BGS WMS service (tiled for large areas)
4. Calculate risk scores for each building using spatial indexing
5. Generate interactive map with toggleable layers

## Risk Scoring

### Combined Score (0-10)

```
Combined Score = (Soil Score × 0.4) + (Tree Score × 0.6)
```

- **40% Soil Risk** - Based on soil shrink-swell potential
- **60% Tree Risk** - Based on proximity to tree root zones

### Soil Risk Scores

| Soil Type | Score | Risk Level |
|-----------|-------|------------|
| Heavy Clay | 10 | Highest |
| Clay | 8 | High |
| Clay Loam | 6 | Medium-High |
| Loam | 4 | Medium |
| Sandy Loam | 2 | Low |
| Sand | 1 | Minimal |
| Unknown | 0 | No data |

### Tree Proximity Scoring

Trees within root zone contribute significantly to risk:
- **Root zone** (1.5× crown width): 3-5 points per tree
- **Very close** (< 5m): +2 point bonus
- **Outside root zone**: Linear decay to 0 at 30m

**Species risk factors:**
| Species | Factor | Water Uptake |
|---------|--------|--------------|
| Willow | 1.8× | Very High |
| Poplar | 1.7× | High |
| Oak | 1.5× | Medium-High |
| Ash | 1.3× | Medium |
| Birch | 0.9× | Lower |

## Output Files

| File | Description |
|------|-------------|
| `bristol_buildings_scored.geojson` | Buildings with full risk attributes |
| `subsidence_risk_buildings.html` | Interactive map with layers |

## Study Areas

The notebook includes three predefined study areas:

| Area | Size | Buildings | Use Case |
|------|------|-----------|----------|
| TINY | ~0.25 km² | ~600 | Quick testing |
| TEST | ~4 km² | ~5,000 | Development |
| FULL | ~180 km² | ~227,000 | Production |

Change `BRISTOL_BOUNDS = BRISTOL_BOUNDS_FULL` in cell 2 to switch areas.

## Performance

The analysis uses several optimizations:
- **Tiled WMS fetching** - Handles large areas by splitting into ~1.6km × 1.5km tiles
- **R-tree spatial index** - ~40× faster tree proximity queries
- **Parallel API requests** - Faster building data collection

| Area | Buildings | Scoring Time |
|------|-----------|--------------|
| TINY | 600 | ~10 seconds |
| TEST | 5,000 | ~1 minute |
| FULL | 227,000 | ~5-10 minutes |

## Data Sources

- **Trees**: [Bristol City Council Open Data](https://maps2.bristol.gov.uk/)
- **Buildings**: [OpenStreetMap](https://www.openstreetmap.org/) via Overpass API
- **Soil**: [British Geological Survey WMS](https://map.bgs.ac.uk/arcgis/services/UKSO/UKSO_BGS/MapServer/WMSServer)

## Requirements

- Python 3.10+
- See `requirements.txt` for full dependencies

Key packages:
- `geopandas` - Geospatial data handling
- `folium` - Interactive maps
- `owslib` - WMS service access
- `osmnx` - OpenStreetMap data
- `shapely` - Geometry operations

## Project Structure

```
subsistencerisk/
├── subsidence_risk_analysis.ipynb  # Main analysis notebook
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── config_example.py               # Example configuration
└── outputs/
    ├── bristol_buildings_scored.geojson
    └── subsidence_risk_buildings.html
```

## License

Open data sources used under their respective licenses:
- BGS data: Open Government Licence
- OSM data: ODbL
- Bristol Council data: Open Government Licence


## Contact

For questions or collaboration opportunities, please open an issue on GitHub.