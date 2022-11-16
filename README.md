# DRIVE: Digital Retinal Images for Vessel Extraction

## Preparation

The DRIVE dataset was already download from this [challenge page](https://drive.grand-challenge.org/).

All the images already been proccessed and save in file data.
- `afterMask_all`: Images which mask out the background.
- `afterMask_blue`: The blue channel of images in afterMask_all.
- `afterMask_green`: The green channel of images in afterMask_all.
- `afterMask_red`: The red channel of images in afterMask_all.
- `GB_image_large`: The blue and green channel of images in image_large.
- `image_large`: Oringal DRIVE dataset
- `mask`: The Ground truth of the vessel segmentation
- `mask_crop`: The Ground truth of the vessel segmentation which mask out the background

## Training

- For quickly start, you can simply use the following command to train:

  ```console
  CUDA_VISIBLE_DEVICES=0,1,2,3 python main.py 
  ```

## UNet Segmentation Result

<img width="860" alt="截圖 2022-11-16 上午11 55 53" src="https://user-images.githubusercontent.com/83267883/202079794-6a9f5696-b989-4518-891d-12fdcbe58fa5.png">

<img width="639" alt="截圖 2022-11-16 上午11 54 22" src="https://user-images.githubusercontent.com/83267883/202079727-26737b2a-1cb8-454e-8351-9bb56ca9f8ff.png">


## Acknowledgements

This code refers to the following projects:

1. [Retina blood vessel segmentation with a convolution neural network (U-net)](https://github.com/orobix/retina-unet)
