# CS_590_HW1
### Scott Delozier

# Assignment-1

**Due Date:** 01/27

## Problem-1: 15 Points

**General description:** Create a repository on GitHub and make it public. Upload two files for this problem: a bash script file and a yml/yaml file.

### Bash Script file

Write a bash script that:
- Updates the system
- Installs the following packages:
  1. htop
  2. screen
  3. miniconda

Installing miniconda:
1. Create the miniconda folder
2. Run the script to install packages
3. Check if `/path/to/miniconda/bin/conda` file exists
4. If it exists, run `/path/to/miniconda/bin/conda init bash`

Installation instructions: [Miniconda Docs](https://docs.conda.io/projects/miniconda/en/latest/index.html) (Click on the linux tab)

### Yml file

Once you download required packages for Jupyter server and functionalities, export the environment to a file called `requirements.yml`. Push this file to your GitHub repo. This file automates your Python environment creation process.

## Problem-2: 10 Points

**General description:** Create a bash script that copies all files inside a folder to another folder. User provides source and destination paths as input.

Example:
```bash
./my_copy_script.sh /users/manasdas/data1 /users/manasdas/output/results


./install.sh
source .bashrc
conda env create --name jupyter -f requirements.yml
conda activate jupyter
conda install pytorch==1.13.0 torchvision==0.14.0 torchaudio==0.13.0 cpuonly -c pytorch
screen -S newScreen
jupyter notebook --no-browser --port=5910

in local terminal:
ssh -L 59000:localhost:5910 sdelozi@xxx

in browser:
http://localhost:59000/tree?token=xxx
(get from jupyter screen, change port)