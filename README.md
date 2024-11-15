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

Step 2: Install MMDET
```bash
cd /ROOT/Opera/third_party/mmdet
MMCV_WITH_OPS=1 pip install -e .

### Step 3: Install OPERA In the home directory
```bash
pip install -r requirements.txt
pip install -e .
