import matplotlib.pyplot as plt
import view_sentinel as vs
import os

filepath = "ROIs1158_spring_15_p30.tif"
# rgb_image = vs.get_rgb(filepath)

# fig, ax = plt.subplots(ncols=3, nrows=1)
# vs.display_rgb_image(rgb_image, fig, ax[0])


test = vs.view_sentinel_2("", os.listdir("s2_cloudy"))
# test.display_images(35)


# use gdalinfo to see metadata about an image


