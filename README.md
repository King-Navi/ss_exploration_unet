# Setup & Usage

## Prerequisites
- **CUDA 12.8** installed and working (for GPU build).
- **Poetry 2.x** installed.
- **Python 3.9+**.

> Check your GPU/driver:
```bash
nvidia-smi




# (1) Install Poetry if needed
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"

# (2) Install project deps
poetry install

# (3) Activate venv
source "$(poetry env info --path)/bin/activate"

# (4a) Install PyTorch (GPU, CUDA 12.8)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128

# (4b) OR CPU-only (choose one)
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# (5) Verify
<h1>Check if all is good</h1>

poetry run python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"


Output:

CUDA available: True
Device: NVIDIA GeForce RTX 3060

# (6) Run
python test.py
# or:
exit
poetry run python test.py




