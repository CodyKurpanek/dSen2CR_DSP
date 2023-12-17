# Cloud Removal from Satellite Imagery

![Patch Images](https://github.com/ameraner/dsen2-cr/blob/main/doc/paper.JPG)

This repository is a modification of DSen2-CR, the cloud removal model proposed by Andrea Meraner and Patrick Ebel and Xiao Xiang Zhu and Michael Schmitt. See more information about this model in their [open-access paper](https://www.sciencedirect.com/science/article/pii/S0924271620301398?via%3Dihub) and [github](https://github.com/ameraner/dsen2-cr). We do not have any affiliation with the authors and a large majority of our code is from their repository.

The **dsen2-cr** folder contains a replica of their code with some new modifications that we have made and documented. We add scripts for downloading and extracting the data 

The **visualize_sentinel_data** folder is our code we have created to visualize the dataset of satellite imagery quickly and effectively. This requires extrating and displaying the correct bands from sentinel imagery, adding modifications for visual aid, and providing an easy way to access and iterate through specific images. 

The **latent-diffusion-inpainting** folder is built off of the fork [github](https://github.com/nickyisadog/latent-diffusion-inpainting/tree/main/ldm), which was a starting spot for cloud inapainting as a preprocessing step to the dsen2-CR model. 


<p align="center">
  <img src="https://ars.els-cdn.com/content/image/1-s2.0-S0924271620301398-gr2.jpg"/>
</p>

<font size="1"> *Images are from dsen2-cr paper and github </font>




