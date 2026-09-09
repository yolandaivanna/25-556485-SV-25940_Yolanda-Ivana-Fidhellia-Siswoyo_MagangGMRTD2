import cv2
from ultralytics import YOLO

# 1. Muat model YOLOv8n
model = YOLO('yolov8n.pt')

# 2. Tentukan 3 objek target yang tersedia di YOLO COCO
TARGET_CLASSES = ['person', 'book', 'cell phone']

# Dapatkan ID kelas untuk objek target YOLO
target_class_ids = [id_ for id_, name in model.names.items() if name in TARGET_CLASSES]

print(f"Mendeteksi objek: {TARGET_CLASSES}")

# 3. Buka webcam laptop (ID 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Kamera tidak dapat dibuka.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Gagal mengambil frame dari kamera.")
        break

    # 4. Jalankan deteksi YOLOv8 khusus 3 kelas target
    results = model(frame, classes=target_class_ids, conf=0.5, verbose=False)

    # 5. Visualisasikan Bounding Box, Nama Objek, dan Confidence Score
    for result in results:
        boxes = result.boxes
        for box in boxes:
            # Koordinat Bounding Box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Confidence Score & Nama Objek
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            # Warna bounding box sesuai objek
            if class_name == 'person':
                color = (255, 0, 0)      # Biru
            elif class_name == 'book':
                color = (0, 255, 255)    # Kuning
            elif class_name == 'cell phone':
                color = (0, 0, 255)      # Merah
            else:
                color = (0, 255, 0)      # Hijau default

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

            # Buat teks label
            label = f"{class_name} {confidence:.2f}"

            # Latar belakang teks agar mudah dibaca
            (text_width, text_height), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame, (x1, y1 - text_height - 10), (x1 + text_width, y1), color, -1)

            # Tuliskan nama objek & score (Teks warna hitam)
            cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    # 6. Tampilkan jendela video
    cv2.imshow("YOLOv8n 3 Object Detection - Webcam", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 7. Tutup sumber daya
cap.release()
cv2.destroyAllWindows()