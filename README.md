# VHP: A bioinformatics tool to predict the potential hosts of viruses using deep learning techniques

* [Introduction](#introduction)
* [Version](#version)
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage](#usage)
* [Output](#output)
* [Citation](#citation)
* [Contact](#contact)
    

## Introduction

VHP is designed to prediction the potential host types (plant, germ, invertebrate, vertebrate, human) of a given virus, which is represented by its nucleotide sequences. The tool will provide five scores and the corresponding p-values which reflect the propobilities of the virus infecting each host type. In addition, the score pattern and the p-value pattern reflect the infectivity pattern of the given virus. The program is also available at http://cqb.pku.edu.cn/ZhuLab/VHP/.

## Version
+ VHP 1.1 (Tested on Ubuntu 16.04)

## Requirements
### 1. To run the physical host version of VHP, you need to install:
+ [Python 3.6.7](https://www.python.org/)
+ [numpy 1.17.5](http://www.numpy.org/)
+ [h5py 2.10.0](http://www.h5py.org/)
+ [pandas 0.25.3](https://pandas.pydata.org/)
+ [TensorFlow 2.0.0](https://www.tensorflow.org/)
+ [Keras 2.3.1](https://keras.io/)
+ [MATLAB Component Runtime (MCR) R2018a](https://www.mathworks.com/products/compiler/matlab-runtime.html) or [MATLAB R2018a](https://www.mathworks.com/products/matlab.html)

  **Note:**
(1) VHP should be run under Linux operating system.
(2) For compatibility, we recommend installing the tools with the similar version as described above.
(3) If GPU is available in your machine, we recommend installing a GPU version of the TensorFlow to speed up the program.
(4) VHP can be run with either an executable file or a MATLAB script. If you run VHP through the executable file, you need to install the MCR (for free) while MATLAB is not necessary. If you run VHP through the MATLAB script, MATLAB is required.

### 2. If you are non-computer professionals who unfamiliar with the Linux operating system, we recommend using the virtual machine of VHP. In this way, you do not need to install any dependant packages as mentioned above.



## Installation

### 1. Physical host version
  #### 1.1 Prerequisites
  
  First, please install **numpy, h5py, pandas, TensorFlow** and **Keras** according to their manuals. All of these are python packages, which can be installed with ``pip``. If “pip” is not already installed in your machine, use the command “sudo apt-get install python-pip python-dev” to install “pip”. Here are example commands of installing the above python packages using “pip”.
    
    pip install numpy
    pip install h5py
    pip install pandas
    pip install tensorflow==2.0.0  #CPU version
    pip install tensorflow-gpu==2.0.0  #GPU version
    pip install keras==2.3.1
    
  If you are going to install a GPU version of the TensorFlow, specified NVIDIA software should be installed. See https://www.tensorflow.org/install/install_linux to know whether your machine can install TensorFlow with GPU support.  
  
  When running VHP through the executable file, MCR should be installed. See https://www.mathworks.com/help/compiler/install-the-matlab-runtime.html to install MCR. On the target computer, please append the following to your LD_LIBRARY_PATH environment variable according to the tips of MCR:
  
    <MCR_installation_folder>/v94/runtime/glnxa64
    <MCR_installation_folder>/v94/bin/glnxa64
    <MCR_installation_folder>/v94/sys/os/glnxa64
    <MCR_installation_folder>/v94/extern/bin/glnxa64
    
  When  running  VHP  through  the MATLAB script, please  see https://www.mathworks.com/support/ to install the MATLAB.  
  
  #### 1.2 Install VHP using git
  
  Clone VHP package
  
    git clone https://github.com/zhenchengfang/VHP.git
    
  Change directory to VHP:
  
    cd VHP
    
  The executable file and all scripts are under the folder
  
  #### 1.3 Install VHP from zipped file
  
  VHP can also download as a zipped file:
  
    wget http://cqb.pku.edu.cn/ZhuLab/VHP/VHP_v_1_0.zip
    
  Unpack the zipped file:
  
    unzip VHP_v_1_0.zip
    
  Change directory to VHP
  
    cd VHP_v_1_0
    
  The executable file and all scripts are under the folder
  
### 2. Virtual machine version

The installation of the virtual machine is much easier. Please refer to [Manual.pdf](http://cqb.pku.edu.cn/ZhuLab/PPR_Meta/Manual.pdf) for a step by step guide with screenshot to see how to install the vertual machine. Also, you can refer to a breaf [video guide](http://cqb.pku.edu.cn/ZhuLab/PPR_Meta/Video_Guide.mp4) to see how to install the virtual machine.

## Usage

### 1. Run VHP using executable file (in command line)

  Please simply execute the command:
  
    ./VHP <input_file_folder>/input_file.fna <output_file_folder>/output_file.csv
    
  The input file must be in fasta format containing the sequences to be identified. For example, users can use the file "example.fna" in the folder to test VHP by simply executing the command:
  
    ./VHP example.fna result.csv
    
### 2. Run VHP using MATLAB script (in MATLAB GUI)

  Please execute the following command directly in MATLAB command window:
  
    VHP('<input_file_folder>/input_file.fna','<output_file_folder>/output_file.csv')
    
  For example, if you want to identify the sequences in "example.fna", please execute:
  
    VHP('example.fna','result.csv')
    
  Please remember to set the working path of MATLAB to VHP folder before running the programe.

  
## Output

The output of VHP consists of six columns:

Header | plant_s | germ_s | invertebrate_s | vertebrate_s | human_s | plant_p |
------ | ------- | ------ | -------------- | ------------ | ------- | ------- |

The content in `Header` column is the same with the header of corresponding sequence in the input file. With the input of viral nucleotide sequence, VHP will output five scores for each host type, reflecting the infectivity within each host type respectively. Furthermore, VHP provides five p-values, statistical measures of how distinct the infections are compared with non-infection events.



# Citation
+ [article name.](link)


# Contact
Any question, please do not hesitate to contact me: qianguo@pku.edu.cn
