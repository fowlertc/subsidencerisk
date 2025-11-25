# Configuration File for Subsistence Risk Analysis
# Copy this file to config.py and add your API keys and settings

# Study Area Configuration
STUDY_AREA = {
    'name': 'Bristol',
    'center': (51.4545, -2.5879),
    'bounds': {
        'north': 51.5200,
        'south': 51.4000,
        'east': -2.5000,
        'west': -2.7000
    }
}

# Analysis Parameters
ANALYSIS_CONFIG = {
    'grid_size': 0.01,  # Grid cell size in degrees (~1km at UK latitude)
    'tree_proximity_threshold': 0.01,  # Distance threshold for tree risk (degrees)
    'max_trees_for_visualization': 1000,  # Limit for tree visualization
    'max_buildings_for_visualization': 500,  # Limit for building visualization
}

# Risk Calculation Weights (must sum to 1.0)
RISK_WEIGHTS = {
    'soil_risk': 0.5,      # 50% weight for soil factors
    'tree_risk': 0.3,       # 30% weight for tree proximity
    'building_density': 0.2 # 20% weight for building density
}

# Soil Risk Sub-weights (must sum to 1.0)
SOIL_WEIGHTS = {
    'shrink_swell': 0.5,   # 50% of soil risk
    'clay_content': 0.3,    # 30% of soil risk
    'moisture': 0.2         # 20% of soil risk
}

# Risk Category Thresholds
RISK_THRESHOLDS = {
    'low': 0.3,      # Below this is low risk
    'medium': 0.6,   # Between low and this is medium risk
    # Above medium is high risk
}

# API Configuration
# Add your API keys here (DO NOT commit this file with real keys!)
API_KEYS = {
    'bgs': None,              # British Geological Survey
    'metoffice': None,        # Met Office Weather API
    'environment_agency': None, # UK Environment Agency
}

# API Endpoints
API_ENDPOINTS = {
    'bgs_geology': 'https://api.bgs.ac.uk/geology/v1',
    'metoffice_weather': 'https://api.metoffice.gov.uk/v1',
    'osm_overpass': 'https://overpass-api.de/api/interpreter',
}

# Data Cache Settings
CACHE_CONFIG = {
    'enabled': True,
    'directory': './cache',
    'expiry_hours': 24,  # Cache data for 24 hours
}

# Visualization Settings
VIS_CONFIG = {
    'map_zoom': 12,
    'map_tiles': 'OpenStreetMap',  # Options: 'OpenStreetMap', 'CartoDB positron', 'Stamen Terrain'
    'color_scheme': {
        'low_risk': '#2ecc71',    # Green
        'medium_risk': '#f39c12',  # Orange
        'high_risk': '#e74c3c'     # Red
    },
    'heatmap_radius': 15,
    'heatmap_blur': 20,
}

# Export Settings
EXPORT_CONFIG = {
    'formats': ['geojson', 'shapefile', 'html', 'csv'],
    'output_directory': './',
    'filename_prefix': 'subsistence_risk',
}

# Logging Settings
LOGGING_CONFIG = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'analysis.log',
}

# Data Source Preferences
DATA_SOURCES = {
    'trees': 'osm',           # Options: 'osm', 'local', 'api'
    'buildings': 'osm',       # Options: 'osm', 'local', 'api'
    'soil': 'synthetic',      # Options: 'synthetic', 'bgs', 'esdac', 'local'
}

# Example of how to use this configuration in the notebook:
"""
import config

# Access study area
bounds = config.STUDY_AREA['bounds']

# Access risk weights
soil_weight = config.RISK_WEIGHTS['soil_risk']

# Access API keys (if configured)
bgs_key = config.API_KEYS['bgs']
"""
