# Project README

This project is organized into two main folders:
1. **Baseline Folder**: Contains the original baseline code with unnecessary files removed.
2. **Folder 2**: Contains our modified code.

## Installation Instructions
Before running both the baseline and modified code, please install `mmcv`, `mmdet`, and `opera` as follows:

### Step 1: Install MMCV
```bash
cd /ROOT/Opera/third_party/mmcv
MMCV_WITH_OPS=1 pip install -e .
```
### Step 2: Install mmdet
```bash
cd /ROOT/Opera/third_party/mmdet
MMCV_WITH_OPS=1 pip install -e .
```
### Step 3: Install opera:In the home directory
```bash
pip install -r requirements.txt
pip install -e .
```
Note that our team uses cuda11.1, you can modify it according to your own cuda, if the direct installation of 11.1 fails, you can replace the installation source to install 11.1

## Possible problems
If the baseline installation is successful but our project fails to install, you can manually replace the file to modify it:
First replace the baseline of the opera/models/utils/transformer. Py files into our project of the transformer. Py, Add copy contrastive_loss.py in the opera/models/losses/ folder Modify the opera/models/losses/__init__.py file to add  loss_contrastive. Finally, in the config file you want to run,  change the data-root address in configs/_base_/datasets/wifi_keypoint.py to the local dataset address. Modify the  work_dir address in configs/wifi/MSEloss_64x2_lr_1e_5.py. You can run the code using tools/ train.py +  configs/wifi/MSEloss_64x2_lr_1e_5.py in the terminal. Some of the more complex and detailed methods and bug fixes are  described in the readme.
