"""
Standalone script to collect building data for Bristol using Overpass API.

This script fetches building footprints and saves them to a GeoJSON file.
Run this if you need to refresh the building data cache.

Usage:
    python collect_buildings.py

Output:
    bristol_buildings_tiny.geojson
"""
import geopandas as gpd
import requests
from shapely.geometry import Polygon
import json

# Bristol bounds - TINY area for testing
BRISTOL_BOUNDS = {
    'north': 51.4595,
    'south': 51.4495,
    'east': -2.5829,
    'west': -2.5929
}

def collect_buildings_overpass(north, south, east, west):
    """Collect building data using Overpass API directly"""
    
    print(f"Fetching buildings for area:")
    print(f"  North: {north}, South: {south}")
    print(f"  East: {east}, West: {west}")
    
    # Overpass API mirrors
    mirrors = [
        "https://overpass-api.de/api/interpreter",
        "https://overpass.kumi.systems/api/interpreter",
        "https://overpass.openstreetmap.ru/api/interpreter"
    ]
    
    # Optimized query
    query = f"""
    [out:json][timeout:60];
    (
      way["building"]({south},{west},{north},{east});
      relation["building"]({south},{west},{north},{east});
    );
    out geom;
    """
    
    buildings_data = None
    
    # Try each mirror
    for api_url in mirrors:
        mirror_name = api_url.split('/')[2]
        print(f"\nTrying {mirror_name}...")
        
        try:
            response = requests.post(
                api_url,
                data=query,
                timeout=90,
                headers={'User-Agent': 'SubsidenceRiskAnalysis/1.0'}
            )
            
            if response.status_code == 200:
                buildings_data = response.json()
                print(f"✓ Success! Got data from {mirror_name}")
                break
            else:
                print(f"✗ HTTP {response.status_code}")
                
        except requests.exceptions.Timeout:
            print(f"✗ Timeout")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    if not buildings_data:
        print("\n✗ All mirrors failed")
        return None
    
    # Convert to GeoDataFrame
    elements = buildings_data.get('elements', [])
    print(f"\n✓ Retrieved {len(elements)} building elements")
    
    features = []
    for element in elements:
        if 'geometry' in element:
            coords = [(node['lon'], node['lat']) for node in element['geometry']]
            if len(coords) >= 3:
                poly = Polygon(coords)
                features.append({
                    'geometry': poly,
                    'building': element.get('tags', {}).get('building', 'yes'),
                    'osm_id': element.get('id'),
                    'building_levels': element.get('tags', {}).get('building:levels'),
                    'name': element.get('tags', {}).get('name')
                })
    
    if features:
        gdf = gpd.GeoDataFrame(features, crs='EPSG:4326')
        print(f"✓ Created GeoDataFrame with {len(gdf)} buildings")
        return gdf
    else:
        print("✗ No valid building polygons found")
        return None

if __name__ == "__main__":
    print("=" * 60)
    print("BRISTOL BUILDING DATA COLLECTOR")
    print("=" * 60)
    
    # Collect buildings
    buildings = collect_buildings_overpass(
        BRISTOL_BOUNDS['north'],
        BRISTOL_BOUNDS['south'],
        BRISTOL_BOUNDS['east'],
        BRISTOL_BOUNDS['west']
    )
    
    if buildings is not None:
        # Save to file
        output_file = 'bristol_buildings_tiny.geojson'
        buildings.to_file(output_file, driver='GeoJSON')
        print(f"\n✓ Saved to {output_file}")
        
        # Show summary
        print(f"\nSummary:")
        print(f"  Total buildings: {len(buildings)}")
        print(f"  Columns: {buildings.columns.tolist()}")
        print(f"  Building types: {buildings['building'].value_counts().head()}")
        
        print(f"\nYou can now load this file in your notebook:")
        print(f"  building_data = gpd.read_file('{output_file}')")
    else:
        print("\n✗ Failed to collect building data")
    
    print("\n" + "=" * 60)
