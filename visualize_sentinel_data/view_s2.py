from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

filepath = "/home/cody/dspath/view_GeoTIFF/ROIs1158_spring_15_p30.tif"

# Open the GeoTIFF file
data = gdal.Open(filepath)
data.GetMetadata()

# Read the Red, Green, and Blue bands
red_band = data.GetRasterBand(4).ReadAsArray()
green_band = data.GetRasterBand(3).ReadAsArray()
blue_band = data.GetRasterBand(2).ReadAsArray()

# Combine the bands to form the RGB image
rgb_image = np.dstack((red_band, green_band, blue_band))

# Normalize the pixel values from 16 bit u-int values to the range 0-1
UINT16_MAX = 65535.0
rgb_image = rgb_image / UINT16_MAX

#set the initial gain
init_gain = 25

# Visualize the RGB image using Matplotlib
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
displayed_image = ax.imshow(rgb_image * init_gain)
# Make a horizontal slider to control the gain of the image
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Gain',
    valmin=1,   
    valmax=100,
    valinit=init_gain,
)
# Update Gain when slider is moved
def update(gain):
    displayed_image.set_data(rgb_image * gain)
    fig.canvas.draw_idle()
freq_slider.on_changed(update)

plt.show()


# Close the data
data = None