# sdxl-clip-interrogator Cog model

This is an implementation of the model [pharmapsychotic/clip-interrogator](https://github.com/pharmapsychotic/clip-interrogator) as a Cog model for SDXL. [Cog packages machine learning models as standard containers.](https://github.com/replicate/cog)

First, download the pre-trained weights:

    cog run script/download-weights

Then, you can run predictions:

    cog predict -i image=@turtle.jpg
