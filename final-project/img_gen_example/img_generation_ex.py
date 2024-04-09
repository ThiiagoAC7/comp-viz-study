import torch
from torch import autocast
from PIL import Image
from diffusers import DiffusionPipeline

pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", use_safetensors=True)

def image_grid(imgs, rows, cols):
    "src: https://huggingface.co/blog/stable_diffusion"
    assert len(imgs) == rows*cols

    w, h = imgs[0].size
    grid = Image.new('RGB', size=(cols*w, rows*h))
    grid_w, grid_h = grid.size
    
    for i, img in enumerate(imgs):
        grid.paste(img, box=(i%cols*w, i//cols*h))
    return grid

# pipeline.to("cuda")

N = 5
prompt = ["temple in ruines, forest, stairs, columns, cinematic, detailed, Matte painting, mist"]*N

# with autocast("cuda"):
images = pipeline(prompt).images
    
grid = image_grid(images, rows=1, cols=3)
