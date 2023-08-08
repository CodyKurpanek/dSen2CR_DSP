from osgeo import gdal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, TextBox
import os

class view_sentinel_2:
    def __init__(self, base_dir, files):
        self.matplotlib_setup()
        self.filelist = files
        self.filedict = dict()
        for i, file in enumerate(files):
            self.filedict[file] = i

        self.base_dir = base_dir
        self.file_idx = 0
        filepath = files[0]
        self.fig, self.ax = plt.subplots(figsize=(25,15), ncols=3, nrows=1)
        self.fig.subplots_adjust(bottom=0.25)
        self.init_gain = 35
        self.get_cloudFree(os.path.join(base_dir, "s2_cloudFree", filepath))
        self.get_cloudy(os.path.join(base_dir, "s2_cloudFree", filepath))
        self.get_SAR(os.path.join(base_dir, "s2_cloudFree", filepath))
        self.display_images(self.init_gain)


    def matplotlib_setup(self):
        plt.rcParams.update({
            'font.size': 15,          # Adjust this value to change the font size
            'axes.labelsize': 12,     # Label font size
            'axes.titlesize': 14,     # Title font size
            'xtick.labelsize': 10,    # X-axis tick label font size
            'ytick.labelsize': 10,    # Y-axis tick label font size
            'legend.fontsize': 12,    # Legend font size
            'figure.titlesize': 18    # Figure title font size
        })

    def get_cloudFree(self, filepath):
        # Open the GeoTIFF file
        data = gdal.Open(filepath)
        if data is None:
            return 1
        data.GetMetadata()

        # Read the Red, Green, and Blue bands
        red_band = data.GetRasterBand(4).ReadAsArray()
        green_band = data.GetRasterBand(3).ReadAsArray()
        blue_band = data.GetRasterBand(2).ReadAsArray()

        # Combine the bands to form the RGB image
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # Normalize the pixel values from 16 bit u-int values (range 0-UINT16_MAX) to the range 0-1
        UINT16_MAX = 65535.0
        rgb_image = rgb_image / UINT16_MAX
        self.cloudFree = rgb_image


    def get_cloudy(self, filepath):
        # Open the GeoTIFF file
        data = gdal.Open(filepath)
        if data is None:
            return 1
        data.GetMetadata()

        # Read the Red, Green, and Blue bands
        red_band = data.GetRasterBand(4).ReadAsArray()
        green_band = data.GetRasterBand(3).ReadAsArray()
        blue_band = data.GetRasterBand(2).ReadAsArray()

        # Combine the bands to form the RGB image
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # Normalize the pixel values from 16 bit u-int values (range 0-UINT16_MAX) to the range 0-1
        UINT16_MAX = 65535.0
        rgb_image = rgb_image / UINT16_MAX
        self.cloudy = rgb_image


    def get_SAR(self, filepath):
        # Open the GeoTIFF file
        data = gdal.Open(filepath)
        if data is None:
            return 1
        data.GetMetadata()

        # Read the Red, Green, and Blue bands
        red_band = data.GetRasterBand(4).ReadAsArray()
        green_band = data.GetRasterBand(3).ReadAsArray()
        blue_band = data.GetRasterBand(2).ReadAsArray()

        # Combine the bands to form the RGB image
        rgb_image = np.dstack((red_band, green_band, blue_band))

        # Normalize the pixel values from 16 bit u-int values (range 0-UINT16_MAX) to the range 0-1
        UINT16_MAX = 65535.0
        rgb_image = rgb_image / UINT16_MAX
        self.SAR = rgb_image


    def display_images(self, gain):
        # Visualize the images using Matplotlib
        self.displayed_cloudy = self.ax[0].imshow(self.cloudy * gain)
        self.displayed_SAR = self.ax[1].imshow(self.SAR * gain)
        self.displayed_cloudFree = self.ax[2].imshow(self.cloudFree * gain)


        #create widgets
        widget_height = 0.07
        #create forward and backwards arrows
        axprev = self.fig.add_axes([0.05, 0.1, 0.05, widget_height])
        prev_button = Button(axprev, "<")
        axnext = self.fig.add_axes([0.1, 0.1, 0.05, widget_height])
        next_button = Button(axnext, ">")
        def update_next(clicked):
            self.file_idx = (self.file_idx + 1) % (len(self.filelist))
            filepath = self.filelist[self.file_idx]
            self.get_cloudFree(os.path.join("s2_cloudFree", filepath))
            self.get_cloudy(os.path.join("s2_cloudFree", filepath))
            self.get_SAR(os.path.join("s2_cloudFree", filepath))
            self.displayed_cloudy.set_data(self.cloudy * gain)
            self.displayed_SAR.set_data(self.SAR * gain)
            self.displayed_cloudFree.set_data(self.cloudFree * gain)
            self.fig.canvas.draw_idle()

        def update_prev(clicked):
            self.file_idx = self.file_idx - 1 if self.file_idx - 1 >= 0 else (len(self.filelist)-1)
            filepath = self.filelist[self.file_idx]
            self.get_cloudFree(os.path.join("s2_cloudFree", filepath))
            self.get_cloudy(os.path.join("s2_cloudFree", filepath))
            self.get_SAR(os.path.join("s2_cloudFree", filepath))
            self.displayed_cloudy.set_data(self.cloudy * gain)
            self.displayed_SAR.set_data(self.SAR * gain)
            self.displayed_cloudFree.set_data(self.cloudFree * gain)
            self.fig.canvas.draw_idle()
        next_button.on_clicked(update_next)
        prev_button.on_clicked(update_prev)


        # Make a horizontal slider to control the gain of the image
        axgain = self.fig.add_axes([0.22, 0.1, 0.2, widget_height])
        gain_slider = Slider(
            ax=axgain,
            label='Gain',
            valmin=1,   
            valmax=100,
            valinit=self.init_gain,
        )
        def update_gain(gain):
            self.displayed_cloudy.set_data(self.cloudy * gain)
            self.displayed_SAR.set_data(self.SAR * gain)
            self.displayed_cloudFree.set_data(self.cloudFree * gain)
            self.fig.canvas.draw_idle()
        gain_slider.on_changed(update_gain)

        axfilepath = self.fig.add_axes([0.55, 0.1, 0.3, widget_height])
        filepath_textbox = TextBox(ax=axfilepath, label='Filepath')
        def update_filepath(path):
            file_index = self.filedict.get(path)
            if(file_index):
                filepath = self.filelist[file_index]
                self.file_idx = file_index
                self.get_cloudFree(os.path.join("s2_cloudFree", filepath))
                self.get_cloudy(os.path.join("s2_cloudFree", filepath))
                self.get_SAR(os.path.join("s2_cloudFree", filepath))
                self.displayed_cloudy.set_data(self.cloudy * gain)
                self.displayed_SAR.set_data(self.SAR * gain)
                self.displayed_cloudFree.set_data(self.cloudFree * gain)
                self.fig.canvas.draw_idle()
            else:
                print("file: ", path, " does not exist")
        filepath_textbox.on_submit(update_filepath)
        plt.show() 