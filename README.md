# Setup & Usage

## Prerequisites
- **CUDA 12.8** installed and working (for GPU build).
- **Poetry 2.x** installed.
- **Python 3.9+**.

> Check your GPU/driver:
```bash
nvidia-smi
```




# (1) Install Poetry if needed
```bash
curl -sSL https://install.python-poetry.org | python3 -
export PATH="$HOME/.local/bin:$PATH"
```
# (2) Install project deps
```bash
poetry install
```
# (3) Activate venv


```bash
poetry self add poetry-plugin-shell
```

```bash
poetry shell
```


# (4a) Install PyTorch (GPU, CUDA 12.8)
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu128
```
# (4b) OR CPU-only (choose one)

```bash
# pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```


# (5) Verify
```bash
poetry run python -c "import torch; print('CUDA available:', torch.cuda.is_available()); print('Device:', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CPU')"
```
Example of output:

CUDA available: True
Device: NVIDIA GeForce RTX 3060

# (6) Run
```bash
python test.py
```
# or:
```bash
exit
poetry run python test.py
```




