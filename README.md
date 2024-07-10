# QGIS Map Canvas Application

## Overview
This project utilizes PyQt5 and QGIS Python API to create a desktop application for visualizing geographic data. It loads and displays vector layers (shapefiles) within a QGIS map canvas, allowing users to view and interact with spatial data layers.

## Components
### Main Application (`main.py`)
- **QGIS Environment Setup**: Initializes QGIS environment settings and PyQt5 application.
- **Map Canvas Configuration**: Creates a QGIS map canvas with a customizable background color.
- **Layer Loading**: Loads vector layers (shapefiles) from specified file paths.
- **Layer Validation**: Checks if loaded layers are valid for display.
- **Main Window Setup**: Configures the main application window with a fixed size and sets the map canvas as the central widget.
- **Map Canvas Display**: Sets the extent of the map to focus on the loaded vector layers and displays them with adjusted opacity.

### Dependencies
- Python 3.x
- PyQt5
- QGIS Python API

## Usage
1. **Setup Environment**:
   - Install Python 3.x, PyQt5, and QGIS.
   - Ensure all dependencies are properly configured.

2. **Run Application**:
   - Execute `main.py` to launch the QGIS map canvas application.
   - The application window will display the configured vector layers within the map canvas.

3. **Customization**:
   - Modify file paths (`pak_map`, `buffer_layer`) to load different shapefiles.
   - Adjust canvas settings, layer properties, and window size as per project requirements.

## Example Scenario
- The application loads and displays administrative boundary data (`PAK_adm2.shp`) and a buffer zone layer (`buffer.shp`) for visualization and spatial analysis purposes.
