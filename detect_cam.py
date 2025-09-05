from ultralytics import YOLO
import cv2

# Load model YOLOv8 custom
model = YOLO("best.pt")  # pastikan best.pt ada di folder yang sama

# Buka Arducam HawkEye pakai GStreamer pipeline
# resolusi bisa kamu sesuaikan (contoh: 1920x1080)
cap = cv2.VideoCapture(
    "libcamerasrc ! video/x-raw,width=1920,height=1080,framerate=30/1 ! "
    "videoconvert ! appsink",
    cv2.CAP_GSTREAMER,
)

if not cap.isOpened():
    print("❌ Gagal membuka kamera Arducam. Coba cek libcamera.")
    exit()

print("✅ Kamera Arducam berhasil dibuka.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Gagal membaca frame dari kamera.")
        break

    # Inference YOLOv8
    results = model(frame, stream=True)

    # Ambil hasil + gambar bounding box
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("YOLOv8 Arducam Detection", annotated_frame)

    # Tekan "q" untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
