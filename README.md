# 🪖 Helmet Violation Detection using YOLOv8  
### My Entry into Computer Vision

This repository represents my **first hands-on exploration into Computer Vision**.  
I built this project as a learning exercise to understand how **object detection systems work end-to-end**, beyond just theory or model training.

More than the final output, this project reflects the **process I went through while learning** — from confusion and debugging to gradually understanding how different pieces of a computer vision pipeline come together.

---

## 🌱 Why I Built This Project

I wanted to move from:
- “I know the theory”  
to  
- “I understand how things work in practice”

Through this project, I aimed to learn:
- How object detection differs from image classification  
- How datasets and annotations affect model performance  
- How to evaluate models meaningfully  
- What happens after a model makes predictions  
- How ML systems can be made more user-oriented  

---

## 🔍 What This Project Does

This project implements an **end-to-end helmet violation detection pipeline**:

- Trains a YOLOv8 object detection model
- Detects:
  - 🪖 With Helmet  
  - ❌ Without Helmet
- Runs inference on unseen images
- Extracts model outputs into structured data
- Performs automated exploratory data analysis (AutoEDA)
- Allows users to ask questions about detection results
- Returns answers in structured JSON format
- Provides a simple user-facing interface for interaction

---

## 🧠 Tech Stack

- Python  
- YOLOv8 (Ultralytics) – Object Detection  
- OpenCV (conceptual usage)  
- Pandas – Data handling  
- YData Profiling – Automated EDA  
- Streamlit – Simple web interface  
helmet-detection-yolov8/
├── train/ # Training dataset
├── valid/ # Validation dataset
├── test/ # Test dataset
├── runs/ # YOLO outputs
├── extract_results.py # Extract detection results to CSV
├── detections.csv # Structured detection data
├── autoeda.py # AutoEDA report generation
├── qa_json.py # User-oriented Q&A system
├── app.py # Streamlit web app
└── README.md

---

## 🚀 How the Pipeline Works

### 1️⃣ Dataset Preparation  
Images were annotated and organized into train, validation, and test splits in YOLO format.

### 2️⃣ Model Training  
A YOLOv8 object detection model was trained to detect helmet and no-helmet cases.

### 3️⃣ Model Evaluation  
Model performance was evaluated using:
- Precision
- Recall
- mAP@50
- mAP@50–95

### 4️⃣ Inference  
The trained model was used to generate bounding box predictions on unseen test images.

### 5️⃣ Post-Detection Analytics  
Detection outputs (class labels, confidence scores, bounding box sizes) were extracted into a structured CSV file.

### 6️⃣ AutoEDA  
Automated exploratory data analysis was performed to understand:
- Class distribution
- Confidence patterns
- Prediction behavior

### 7️⃣ User Interaction  
A simple Q&A system and Streamlit web interface allow users to ask questions about detection results and receive structured answers.

---

## 💬 Sample Questions Supported

- How many helmet violations are there?  
- How many people are wearing helmets?  
- What is the total number of detections?  
- What is the average confidence score?  

Answers are returned in **JSON format**.

---

## 📊 What I Learned

This project helped me understand:

- How object detection models work in practice  
- The importance of dataset quality and balance  
- How to interpret evaluation metrics meaningfully  
- Why post-processing and analytics matter  
- How to design ML systems with users in mind  
- The value of patience, debugging, and iterative learning  

---

## ⚠️ Limitations & Future Improvements

- Model performance depends on dataset diversity  
- Low-light and occluded cases need improvement  
- Future enhancements could include:
  - Video-based inference  
  - Object tracking to avoid double counting  
  - Edge deployment considerations  

---

## 🌿 Final Note

This project represents a **learning journey**, not a finished product.  
It gave me clarity, confidence, and motivation to continue exploring computer vision and real-world AI applications.

Feedback, suggestions, and discussions are always welcome 😊

---

⭐ If you find this project interesting, feel free to star the repository!


## 📁 Project Structure

