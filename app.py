from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import cv2
import os
import time
import easyocr
from threading import Lock

app = Flask(__name__)
CORS(app)

# Configuration
SAVE_DIRECTORY = "static/plates"
HARCASCADE_PATH = "model/haarcascade_russian_plate_number.xml"

if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Mutex to ensure single detection process at a time
detection_lock = Lock()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/start_detection', methods=['POST'])
def start_detection():
    if not detection_lock.locked():
        detection_lock.acquire()
        try:
            plates_saved, ocr_results = detect_and_save_plates()
            if not plates_saved:
                return jsonify({'error': 'Could not start detection. Camera may be unavailable.'}), 500
            return jsonify({'plates': plates_saved, 'ocr_results': ocr_results})
        finally:
            detection_lock.release()
    else:
        return jsonify({'error': 'Detection already in progress. Please wait.'}), 429

@app.route('/plates/<filename>')
def get_plate(filename):
    return send_from_directory(SAVE_DIRECTORY, filename)

def detect_and_save_plates():
    print("Initializing detection...")

    if not os.path.exists(HARCASCADE_PATH):
        print(f"Error: Harcascade file not found at {HARCASCADE_PATH}")
        return [], []

    harcascade = HARCASCADE_PATH
    cap = cv2.VideoCapture(1)
    if not cap.isOpened():
        print("Error: Could not open camera at index 1.")
        return [], []

    print("Camera opened successfully.")
    cap.set(3, 640)  # width
    cap.set(4, 480)  # height
    min_area = 500
    plates_saved = []
    ocr_results = []

    try:
        success, img = cap.read()
        if not success:
            print("Error: Could not read frame.")
            return [], []

        print("Frame read successfully.")
        plate_cascade = cv2.CascadeClassifier(harcascade)
        if plate_cascade.empty():
            print("Error: Failed to load cascade classifier.")
            return [], []

        print("Cascade classifier loaded successfully.")
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

        for (x, y, w, h) in plates:
            area = w * h
            if area > min_area:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "Number Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
                img_roi = img[y: y + h, x: x + w]
                timestamp = int(time.time())
                filename = f"plate_{timestamp}.jpg"
                filepath = os.path.join(SAVE_DIRECTORY, filename)
                print(f"Saving detected plate to {filepath}")
                cv2.imwrite(filepath, img_roi)
                plates_saved.append(filename)

                # Perform OCR on the saved image
                ocr_output = reader.readtext(filepath)
                if ocr_output:
                    text = ocr_output[0][-2]
                    print(f"OCR result for {filename}: {text}")
                    ocr_results.append({'filename': filename, 'text': text})

        print(f"Detected and saved plates: {plates_saved}")
        print(f"OCR results: {ocr_results}")
    except Exception as e:
        print(f"An error occurred during detection: {e}")
    finally:
        cap.release()

    return plates_saved, ocr_results

if __name__ == '__main__':
    app.run(debug=True)
