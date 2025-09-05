from ultralytics import YOLO
import cv2
import argparse

# Argument parser (supaya bisa pilih gambar via --source)
parser = argparse.ArgumentParser()
parser.add_argument("--source", type=str, required=True, help="Path ke file gambar input")
args = parser.parse_args()

# Load model
model = YOLO("best.pt")  # pastikan best.pt ada di folder yang sama

# Load image
img = cv2.imread(args.source)
if img is None:
    print(f"❌ Gagal membuka gambar {args.source}")
    exit()

# Inference
results = model(img)

# Ambil hasil dan anotasi gambar
annotated_img = results[0].plot()

# Tampilkan hasil deteksi
cv2.imshow("YOLOv8 Image Detection", annotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
