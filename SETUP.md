# Setup Guide for Subsistence Risk Analysis

## System Requirements

- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB, recommended 8GB+
- **Disk Space**: 2GB free space for dependencies and data

## Step-by-Step Installation

### 1. Install Python

If Python is not installed:

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- During installation, check "Add Python to PATH"

**macOS:**
```bash
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### 2. Install Git (if not installed)

**Windows:**
- Download from [git-scm.com](https://git-scm.com/downloads)

**macOS:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt install git
```

### 3. Clone Repository

```bash
git clone https://github.com/fowlertc/subsistencerisk.git
cd subsistencerisk
```

### 4. Create Virtual Environment (Recommended)

**All Platforms:**
```bash
python3 -m venv venv
```

**Activate on Windows:**
```bash
venv\Scripts\activate
```

**Activate on macOS/Linux:**
```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This will install all required packages including:
- geopandas (geospatial data handling)
- folium (interactive maps)
- osmnx (OpenStreetMap data)
- jupyter (notebook interface)
- matplotlib, seaborn (plotting)
- And all their dependencies

### 6. Launch Jupyter Notebook

```bash
jupyter notebook
```

This will open your web browser with the Jupyter interface.

### 7. Open and Run the Analysis Notebook

1. In Jupyter, navigate to `subsistence_risk_analysis.ipynb`
2. Click to open the notebook
3. Run cells sequentially using Shift+Enter, or run all with Cell → Run All

## Troubleshooting

### Issue: GDAL/Fiona Installation Fails

**Windows:**
Download pre-compiled wheels from [Christoph Gohlke's page](https://www.lfd.uci.edu/~gohlke/pythonlibs/):
```bash
pip install GDAL‑3.x.x‑cpxx‑cpxxm‑win_amd64.whl
pip install Fiona‑1.x.x‑cpxx‑cpxxm‑win_amd64.whl
```

**macOS:**
```bash
brew install gdal
pip install gdal==$(gdal-config --version)
```

**Linux:**
```bash
sudo apt-get install gdal-bin libgdal-dev
pip install gdal==$(gdal-config --version)
```

### Issue: Memory Errors

- Reduce the study area bounds
- Increase the `grid_size` parameter for coarser analysis
- Close other applications to free up RAM

### Issue: API Rate Limiting

OpenStreetMap may rate-limit requests. If this occurs:
- Wait a few minutes between runs
- Reduce the study area size
- Consider caching downloaded data

### Issue: Jupyter Kernel Crashes

- Restart the kernel: Kernel → Restart
- Clear all outputs: Cell → All Output → Clear
- Try running cells one at a time

## Advanced Configuration

### Using Custom API Keys

If you integrate paid APIs, create a `.env` file:

```bash
BGS_API_KEY=your_key_here
METOFFICE_API_KEY=your_key_here
```

Then load in notebook:
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('BGS_API_KEY')
```

### Performance Optimization

For large study areas:

1. **Use spatial indexing:**
```python
tree_data.sindex  # Creates spatial index
```

2. **Process in chunks:**
```python
for chunk in np.array_split(soil_data, 10):
    process_chunk(chunk)
```

3. **Use multiprocessing:**
```python
from multiprocessing import Pool
with Pool(4) as p:
    results = p.map(process_function, data_chunks)
```

## Data Storage

The notebook generates output files in the working directory:
- `.geojson` files: ~1-10MB depending on area
- `.shp` files: Similar to GeoJSON
- `.html` maps: 1-5MB with embedded data
- `.png` plots: ~100KB-1MB

## Next Steps

After successful installation:

1. Review the example outputs
2. Modify study area bounds for your region of interest
3. Customize risk calculation weights
4. Integrate additional data sources
5. Export and publish your risk layers

## Getting Help

- Check the main README.md for usage examples
- Review notebook comments for detailed explanations
- Open GitHub issues for bugs or questions
- Consult library documentation:
  - [GeoPandas](https://geopandas.org/)
  - [Folium](https://python-visualization.github.io/folium/)
  - [OSMnx](https://osmnx.readthedocs.io/)

## Updates

Keep your installation up to date:

```bash
git pull origin main
pip install --upgrade -r requirements.txt
```
