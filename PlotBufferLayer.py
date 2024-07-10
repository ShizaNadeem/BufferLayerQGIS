import sys
from qgis.core import QgsApplication, QgsVectorLayer
from qgis.gui import QgsMapCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

#Setup QGIS environment
QgsApplication.setPrefixPath('/usr', True)
app = QApplication(sys.argv)
QgsApplication.initQgis()

# Create and configure the map canvas
canvas = QgsMapCanvas()
canvas.setCanvasColor(Qt.white)

# Path to the shapefile
pak_map = r"D:\CENTAIC WORK (AI BDA)\GIS\2 july\2 july\testpyqt\poc shapefile\PAK_adm2.shp"
buffer_layer = r"D:\CENTAIC WORK (AI BDA)\GIS\BufferLayer (8th July)\buffer.shp"

# Load the vector layers
pak_layer = QgsVectorLayer(pak_map, "PAK Layer", "ogr")
buffer_layer1 = QgsVectorLayer(buffer_layer, "Buffer Layer", "ogr")

if not pak_layer.isValid():
    print("PAK Layer failed to load!")
if not buffer_layer1.isValid():
    print("Buffer Layer failed to load!")

pak_layer.setOpacity(0.8)
buffer_layer1.setOpacity(0.8)

# Set up the main window
main_window = QMainWindow()
main_window.setCentralWidget(canvas)
main_window.setFixedSize(800, 600)
main_window.show()

# Set the extent of the map to focus on the vector layer
canvas.setExtent(pak_layer.extent())
canvas.setLayers([pak_layer, buffer_layer1])

# Display the canvas
canvas.show()

# Start the application event loop
sys.exit(app.exec_())