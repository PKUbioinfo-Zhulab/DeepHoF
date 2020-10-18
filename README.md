# DeepHoF: Predicting reservoir hosts based on early SARS-CoV-2 samples and analyzing later world-wide pandemic

* [Introduction](#introduction)
* [Version](#version)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Output](#output)
* [Citation](#citation)
* [Contact](#contact)
    

## Introduction

DeepHoF (using deep learning to virus-host finder) is designed to predict the potential host types (plant, germ, invertebrate, vertebrate, human) of a given virus, which is represented by its nucleotide sequences. The tool will provide five scores and the corresponding p-values which reflect the propobilities of the virus infecting each host type. In addition, the infection likelihood profile the given virus is provided.

## Version
+ DeepHoF 1.0 (Tested on Ubuntu 16.04)

## Requirements
### To run the physical host version of DeepHoF, you need to install:
+ [Python 3.6.10](https://www.python.org/)
+ [numpy 1.17.5](http://www.numpy.org/)
+ [h5py 2.10.0](http://www.h5py.org/)
+ [pandas 0.25.3](https://pandas.pydata.org/)
+ [TensorFlow 1.4.0](https://www.tensorflow.org/)
+ [Keras 2.1.3](https://keras.io/)
+ [MATLAB R2018a](https://www.mathworks.com/products/matlab.html)

  **Note:**  
(1) DeepHoF should be run under Linux operating system.  
(2) For compatibility, we recommend installing the tools with the similar version as described above.  
(3) If GPU is available in your machine, we recommend installing a GPU version of the TensorFlow to speed up the program.  


## Installation

### 1. Prerequisites
  
  First, please install **numpy, h5py, pandas, TensorFlow** and **Keras** according to their manuals. All of these are python packages, which can be installed with ``pip``. If ``pip`` is not already installed in your machine, use the command ``sudo apt-get install python-pip python-dev`` to install ``pip``. Here are example commands of installing the above python packages using ``pip``.
    
    pip install numpy
    pip install h5py
    pip install pandas
    pip install tensorflow==1.4.0  #CPU version
    pip install tensorflow-gpu==1.4.0  #GPU version
    pip install keras==2.1.3

  Or you can use the command ``conda env create -p DeepHoF  -f DeepHoF_env.yaml`` to automatically install all the prerequisites of DeepHoF.
    
  If you are going to install a GPU version of the TensorFlow, specified NVIDIA software should be installed. See https://www.tensorflow.org/install/install_linux to know whether your machine can install TensorFlow with GPU support.  

    
  To run DeepHoF, please  see https://www.mathworks.com/support/ to install the MATLAB.  
  
### 2. Install DeepHoF using git
  
  Clone DeepHoF package
  
    git clone https://github.com/PKUbioinfo-ZhuLab/DeepHoF.git
    
  Change directory to DeepHoF:
  
    cd DeepHoF/DeepHoF
    
  All scripts are under the folder.
  

## Usage

### Input

  Nucleotide sequence
  
### Command

  Please execute the following command directly in MATLAB command window:
  
    DeepHoF('<input_file_folder>/input_file.fna','<output_file_folder>/output_file.tsv')
    
  For example, if you want to identify the sequences in "example.fna", please execute:
  
    DeepHoF('example.fna','result.tsv')
    
  Please remember to set the working path of MATLAB to DeepHoF folder before running the programme.
  
### Output

The output of DeepHoF consists of 11 columns:

Header | plant_score | germ_score | invertebrate_score | vertebrate_score | human_score | plant_pvalue | germ_pvalue | invertebrate_pvalue | vertebrate_pvalue | human_pvalue |
------ | ----------- | ---------- | ------------------ | ---------------- | ----------- | ------------ | ----------- | ------------------- | ----------------- | ------------ |

The content in `Header` column is the same with the header of corresponding sequence in the input file. With the input of viral nucleotide sequence, DeepHoF will output five scores for each host type, reflecting the infectivity within each host type respectively. Furthermore, DeepHoF provides five p-values, statistical measures of how distinct the infections are compared with non-infection events.



# Citation
+ [article name.](link)


# Note
DeepHoF is also available at our website http://cqb.pku.edu.cn/ZhuLab/DeepHoF/ and the Dryad git repository https://datadryad.org/stash/share/Rzua1ir-vRpkiUhODvO7Swd8lxEYdVnGwvl7wiYIX9c. If you have some problems downloading DeepHoF from GitHub and if you want to use the big training and test datasets of DeepHoF, you can go to the alternatives. 


# Contact
Please direct your questions to us, hqzhu@pku.edu.cn or qianguo@pku.edu.cn.


