DeepAnimalToolkit: A toolkit for studying animal behavior
==========================================================================================

## High Preformance Computing Setup Instructions

If you would like to use the Toolkit on a computing cluster with slurm, 
We recommend using Anaconda or Miniconda, you can get it from [Conda download site](https://conda.io/docs/user-guide/install/download.html).

Then, Clone the repository, create a conda environment and install all dependencies:

```bash

git clone https://github.com/gauravkaul7/DAT
conda create -n DAT python=3.9
conda activate DAT
python -m pip install -r requirements.txt

```
### High Preformance Single Animal Tracking

Once you have setup the codebase on your computing cluster we will add all of the 
videos you want to analyze to the ``/hpc/videos_to_analyze`` directory. we will then require the following to run our analysis: 

1. A Detection model (a .pth file)
2. The Detection model type (either detection/mask/keypoint)
3. A Slurm Account (who is running jobs)
4. A Slurm Partition (where are we running jobs)

once we have everything we can run the following command with your values filled in: 

```bash

python hpc/launch_sinlge_instance_tracking.py \
    --model-file {your .pth file}
    --model-type {type of model}
    --account {your Slurm Account name}
    --partition {type of model}

```
  

## Dataset format (for modules that require training data)


### Detection Models (Models that predict bounding boxes, Segmentation Masks, and Keypoints/Pose)

Our detection moduel is located in ``/detection`` and contains the relevent code for training 
models that predict bounding boxes, Segmentation Masks, and Keypoints/Pose.


our system is very flexabile and in order to train detection models(and their 
associated segmentation and keypoint/pose Heads) we expect data to be in the following format.

```
data/datasets/
        └── annotations/
            ├── annotation_1.json
            ├── annotation_2.json
            ├── ...
            ├── annotation_N.json
            └── ...
        └── images/
            ├── image_1.jpeg
            ├── image_2.jpeg
            ├── ...
            ├── image_N.json
            └── ...
```
