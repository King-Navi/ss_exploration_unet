import os
import pandas as pd
import matplotlib.pyplot as plt

# Asegurar que la carpeta output existe
os.makedirs("output", exist_ok=True)

# Cargar CSV desde output
df = pd.read_csv("output/training_metrics.csv")

# Graficar pérdidas
plt.figure()
plt.plot(df["epoch"], df["train_loss"], label="train_loss")
plt.plot(df["epoch"], df["val_loss"], label="val_loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("UNet Loss (train vs val)")
plt.legend()
plt.savefig("output/loss_plot.png", dpi=160)
plt.close()

# Graficar BCE
plt.figure()
plt.plot(df["epoch"], df["train_bce"], label="train_bce")
plt.plot(df["epoch"], df["val_bce"], label="val_bce")
plt.xlabel("Epoch")
plt.ylabel("BCE")
plt.title("UNet BCE (train vs val)")
plt.legend()
plt.savefig("output/bce_plot.png", dpi=160)
plt.close()

# Graficar Dice
plt.figure()
plt.plot(df["epoch"], df["train_dice"], label="train_dice")
plt.plot(df["epoch"], df["val_dice"], label="val_dice")
plt.xlabel("Epoch")
plt.ylabel("Dice")
plt.title("UNet Dice (train vs val)")
plt.legend()
plt.savefig("output/dice_plot.png", dpi=160)
plt.close()

# Graficar LR
plt.figure()
plt.plot(df["epoch"], df["lr"], label="lr")
plt.xlabel("Epoch")
plt.ylabel("Learning Rate")
plt.title("Learning Rate per Epoch")
plt.legend()
plt.savefig("output/lr_plot.png", dpi=160)
plt.close()

print("Gráficas guardadas en la carpeta output/:")
print(" - output/loss_plot.png")
print(" - output/bce_plot.png")
print(" - output/dice_plot.png")
print(" - output/lr_plot.png")
