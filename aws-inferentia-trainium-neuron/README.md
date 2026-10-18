# instance types

inf2, inf1, trn1

# pip libraries

`pip3 install transformers-neuronx --extra-index-url https://pip.repos.neuron.amazonaws.com`

# neuron CLI

`neuron-top` check usage

`neuron-ls` look at available cores

# libnrt.so missing

```
# Install Python venv 
sudo apt-get install -y python3.10-venv g++ 

# Create Python venv
python3.10 -m venv aws_neuron_venv_pytorch 

# Activate Python venv 
source aws_neuron_venv_pytorch/bin/activate 
python -m pip install -U pip 

# Install Jupyter notebook kernel
pip install ipykernel 
python3.10 -m ipykernel install --user --name aws_neuron_venv_pytorch --display-name "Python (torch-neuronx)"
pip install jupyter notebook
pip install environment_kernels

# Set pip repository pointing to the Neuron repository 
python -m pip config set global.extra-index-url https://pip.repos.neuron.amazonaws.com

# Install wget, awscli 
python -m pip install wget 
python -m pip install awscli 

# Install Neuron Compiler and Framework
python -m pip install neuronx-cc==2.* torch-neuronx torchvision
```


# setup on ubuntu 22.04

https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/setup/neuron-setup/pytorch/neuronx/ubuntu/torch-neuronx-ubuntu22.html#setup-torch-neuronx-ubuntu22

# ref

https://github.com/aws-neuron/aws-neuron-samples/blob/master/torch-neuronx/transformers-neuronx/inference/mistralai-Mistral-7b-Instruct-v0.2.ipynb

