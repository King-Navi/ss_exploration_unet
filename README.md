For usage:
- You must have 12.8 CUDA
- You must have poetry 

Poetry instal

Poetry run python test.py


¿No 12.8 CUDA ?

Other version: 
poetry source remove pytorch_cuda
poetry source add --priority explicit pytorch_cuda https://download.pytorch.org/whl/cu121
poetry add --source pytorch_cuda torch torchvision

CPU version:
poetry source remove pytorch_cuda
poetry add torch torchvision # CPU version


Only one time for X.X CUDA

poetry source add --priority explicit pytorch_cuda https://download.pytorch.org/whl/cu128


poetry add --source pytorch_cuda torch torchvision
