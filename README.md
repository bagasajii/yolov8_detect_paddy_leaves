# Paddy Leaf Detection with YOLOv8 🍃

This project uses **YOLOv8** to detect and classify rice leaf conditions 
(Healthy, N-deficiency, P-deficiency, K-deficiency) using an **Arducam HawkEye 64MP (B3099)** camera 
on a **Raspberry Pi 5**.

## 🚀 Setup on Raspberry Pi

1. Clone repository:
   ```bash
   git clone https://github.com/<username>/yolov8_detect_paddy_leaves.git
   cd yolov8_detect_paddy_leaves
2. Install Dependencies

pip install -r requirements.txt

3. Run Detect camera
python3 detect_cam.py

4. Run detection on a single images : 
python3 detect_img.py --source test.jpg

📝 Notes

Use YOLOv8n (nano) for better performance on Raspberry Pi.

For faster inference, consider exporting model to ONNX.
