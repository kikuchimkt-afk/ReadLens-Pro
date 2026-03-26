from PIL import Image

path = r"g:\マイドライブ\ReadLens Pro\data\kakomon\2022\images\mondai_p30.png"
out_path = r"g:\マイドライブ\ReadLens Pro\data\kakomon\2022\images\mondai_p30_fig1.png"

img = Image.open(path)
w, h = img.size

# Crop from just above "Figure 1." to below the symbols
cropped = img.crop((0, int(h * 0.59), w, int(h * 0.74)))
cropped.save(out_path)
print("Cropped successfully to", out_path)
