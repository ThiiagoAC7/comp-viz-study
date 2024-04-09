# Computer Vision Final Project

## Group

- Laurids Radtke
- Giorgia Iacobellis
- Thiago Costa

## Project Description

The goal of this project is to, first, generate a Raccoon Dataset, made with AI generated images. 
This Dataset was built by doing :

1. Prompt Generation (using a pretrained model based on GPT2)
2. Selection of random prompts generated previously.
3. Generating fixed number of images using a Stable Diffusion model
4. Saving, Labeling and Augmenting the generated images on Roboflow, manually.

The Dataset can be accessed on this [link](https://universe.roboflow.com/racoonsimgenthiagocosta/raccoon-imgen-thiago-costa) 

Then, a few [YOLO v8](https://github.com/ultralytics/ultralytics) models are Retrained with the new datase, 
and a comparison is done to verify if the AI generated dataset is useful for improving previous results.

The code and more explanations can be found on the [Raccoons Image Generator Notebook](./Raccoons_Image_Generator.ipynb) file.
A sample of the Image Generation code can also be found on the [Image Generation Folder](./img_gen_example/img_generation_ex.ipynb)
