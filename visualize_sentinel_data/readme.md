# Display Sentinel 2 Data in Natural Color
### Prerequisites (Assuming use of conda environment DSen2cr_env):

Install important libraries:
```bash
conda install -c conda_forge gdal
```
(extra libraries if needed):
```bash
conda install -c conda-forge matplotlib numpy==1.19.5
```

Add data filepath to beginning of view_s2.py

### Run the script:
```bash
python view_s2.py
```

This displays the sentinel-2 images in natural color by selecting bands b4 (Red light), b3 (Green light), b2 (Blue light). Adjust the Gain slider if the image appears too light or dark.