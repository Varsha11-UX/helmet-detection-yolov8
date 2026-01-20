from ultralytics import YOLO
import pandas as pd

# Load trained model
model = YOLO("runs/detect/train/weights/best.pt")

# Run detection on test images
results = model("test/images", save=False)

rows = []

for r in results:
    image_name = r.path.split("\\")[-1]

    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        confidence = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0]
        width = float(x2 - x1)
        height = float(y2 - y1)
        area = width * height

        rows.append({
            "image": image_name,
            "class": label,
            "confidence": confidence,
            "bbox_width": width,
            "bbox_height": height,
            "bbox_area": area
        })

df = pd.DataFrame(rows)
df.to_csv("detections.csv", index=False)

print("detections.csv created successfully")
