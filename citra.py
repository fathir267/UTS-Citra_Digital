import matplotlib.pyplot as plt
import numpy as np
from skimage import io, color, img_as_float, img_as_ubyte
from skimage.util import random_noise
from skimage.filters import rank
from skimage.morphology import disk
from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim

# 1. Baca foto pribadi
# Pastikan file foto berada di folder yang sama dengan script ini
image = io.imread('cake.jpg')

# Jika foto berwarna, ubah ke grayscale
if image.ndim == 3:
    image = color.rgb2gray(image)

# Konversi ke float [0,1]
image = img_as_float(image)

# 2. Tambahkan noise (misal: salt & pepper)
noisy = random_noise(image, mode='s&p', amount=0.1)

# 3. Filtering: mean, min, median, max
noisy_ubyte = img_as_ubyte(noisy)

mean_filtered = rank.mean(noisy_ubyte, footprint=disk(3))
min_filtered = rank.minimum(noisy_ubyte, footprint=disk(3))
median_filtered = rank.median(noisy_ubyte, footprint=disk(3))
max_filtered = rank.maximum(noisy_ubyte, footprint=disk(3))

# Kembalikan ke float untuk evaluasi
mean_filtered_float = img_as_float(mean_filtered)
min_filtered_float = img_as_float(min_filtered)
median_filtered_float = img_as_float(median_filtered)
max_filtered_float = img_as_float(max_filtered)

# 4. Evaluasi: PSNR & SSIM
metrics = {
    "Noisy": {
        "PSNR": psnr(image, noisy),
        "SSIM": ssim(image, noisy, data_range=1.0)
    },
    "Mean Filtered": {
        "PSNR": psnr(image, mean_filtered_float),
        "SSIM": ssim(image, mean_filtered_float, data_range=1.0)
    },
    "Min Filtered": {
        "PSNR": psnr(image, min_filtered_float),
        "SSIM": ssim(image, min_filtered_float, data_range=1.0)
    },
    "Median Filtered": {
        "PSNR": psnr(image, median_filtered_float),
        "SSIM": ssim(image, median_filtered_float, data_range=1.0)
    },
    "Max Filtered": {
        "PSNR": psnr(image, max_filtered_float),
        "SSIM": ssim(image, max_filtered_float, data_range=1.0)
    }
}

# 5. Visualisasi hasil
fig, axes = plt.subplots(1, 6, figsize=(15, 5))
ax = axes.ravel()

titles = ["Original", "Noisy", "Mean Filter", "Min Filter", "Median Filter", "Max Filter"]
images = [image, noisy, mean_filtered, min_filtered, median_filtered, max_filtered]

for i in range(6):
    ax[i].imshow(images[i], cmap='gray')
    ax[i].set_title(titles[i])
    ax[i].axis('off')

plt.tight_layout()
plt.show()

# 6. Cetak hasil evaluasi
for name, vals in metrics.items():
    print(f"{name} -> PSNR: {vals['PSNR']:.2f}, SSIM: {vals['SSIM']:.4f}")
