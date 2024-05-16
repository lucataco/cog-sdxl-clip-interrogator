# sdxl-clip-interrogator Cog model

This is an implementation of the model [pharmapsychotic/clip-interrogator](https://github.com/pharmapsychotic/clip-interrogator) as a Cog model for SDXL. [Cog packages machine learning models as standard containers.](https://github.com/replicate/cog)

First, clone blip:

    git clone https://github.com/salesforce/BLIP blip

Then, enable the download script and run it to get pre-trained weights:

    chmod +x script/download-weights.sh
    cog run script/download-weights.sh

Then, you can run predictions:

    cog predict -i image=@turtle.jpg
