#!/usr/bin/env python3
"""
Test script to validate the subsistence risk analysis setup.
This script checks if all required dependencies are installed and importable.
"""

import sys

def test_imports():
    """Test that all required packages can be imported."""
    required_packages = [
        ('geopandas', 'geopandas'),
        ('folium', 'folium'),
        ('matplotlib', 'matplotlib.pyplot'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('jupyter', 'jupyter'),
        ('requests', 'requests'),
        ('osmnx', 'osmnx'),
        ('shapely', 'shapely.geometry'),
        ('seaborn', 'seaborn'),
        ('rasterio', 'rasterio'),
    ]
    
    print("Testing package imports...")
    print("-" * 50)
    
    failed = []
    for package_name, import_path in required_packages:
        try:
            __import__(import_path)
            print(f"✓ {package_name:<20} - OK")
        except ImportError as e:
            print(f"✗ {package_name:<20} - FAILED: {e}")
            failed.append(package_name)
    
    print("-" * 50)
    
    if failed:
        print(f"\n❌ {len(failed)} package(s) failed to import:")
        for pkg in failed:
            print(f"   - {pkg}")
        print("\nPlease install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    else:
        print(f"\n✅ All {len(required_packages)} required packages are installed!")
        return True

def test_notebook():
    """Test that the notebook file is valid JSON."""
    import json
    
    print("\nTesting notebook structure...")
    print("-" * 50)
    
    try:
        with open('subsistence_risk_analysis.ipynb', 'r') as f:
            notebook = json.load(f)
        
        num_cells = len(notebook.get('cells', []))
        print(f"✓ Notebook is valid JSON")
        print(f"✓ Contains {num_cells} cells")
        
        # Check for essential sections
        cell_texts = []
        for cell in notebook['cells']:
            if cell['cell_type'] == 'markdown':
                cell_texts.append(' '.join(cell['source']))
        
        combined_text = ' '.join(cell_texts)
        
        essential_sections = [
            'Data Collection',
            'Visualization',
            'Risk',
            'Export',
        ]
        
        for section in essential_sections:
            if section in combined_text:
                print(f"✓ Found '{section}' section")
            else:
                print(f"⚠ Warning: '{section}' section not clearly identified")
        
        print("-" * 50)
        print("✅ Notebook structure is valid!")
        return True
        
    except FileNotFoundError:
        print("✗ Notebook file not found!")
        print("-" * 50)
        print("❌ Notebook test failed!")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ Notebook is not valid JSON: {e}")
        print("-" * 50)
        print("❌ Notebook test failed!")
        return False

def check_python_version():
    """Check Python version is suitable."""
    print("Checking Python version...")
    print("-" * 50)
    
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ Python version is suitable (>= 3.8)")
        print("-" * 50)
        return True
    else:
        print("❌ Python version should be 3.8 or higher")
        print("-" * 50)
        return False

def main():
    """Run all tests."""
    print("=" * 50)
    print("Subsistence Risk Analysis - Setup Validation")
    print("=" * 50)
    print()
    
    tests = [
        check_python_version,
        test_notebook,
        test_imports,
    ]
    
    results = []
    for test_func in tests:
        result = test_func()
        results.append(result)
        print()
    
    print("=" * 50)
    if all(results):
        print("🎉 All tests passed! Setup is complete.")
        print("=" * 50)
        print("\nYou can now run the notebook with:")
        print("   jupyter notebook subsistence_risk_analysis.ipynb")
        return 0
    else:
        print("⚠️  Some tests failed. Please fix the issues above.")
        print("=" * 50)
        return 1

if __name__ == '__main__':
    sys.exit(main())
