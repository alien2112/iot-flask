# License Plate Detection Server

This repository contains a Flask-based server that utilizes OpenCV and EasyOCR to detect and read license plates from a video feed. The system captures plates and performs Optical Character Recognition (OCR) to extract the text. It is designed to work with a Haar Cascade model for plate detection and uses a simple API to interact with the detection process.

## Features

- **Real-time License Plate Detection**: Uses OpenCV and Haar Cascade to detect plates in video frames.
- **Optical Character Recognition (OCR)**: Extracts text from detected license plates using EasyOCR.
- **API Endpoints**: Start and manage plate detection, view captured images, and retrieve OCR results.
- **Concurrency Control**: Ensures single detection operation at a time using a lock mechanism.

## Requirements

- Python 3.x
- Flask
- Flask-CORS
- OpenCV (`cv2`)
- EasyOCR
- A compatible camera device

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/plate-detection-server.git
   cd plate-detection-server
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Haar Cascade XML file and place it in the `model` directory:
   - Haarcascade file: [Haar Cascade for Russian Plate Number](https://github.com/opencv/opencv/tree/master/data/haarcascades)

4. Run the server:
   ```bash
   python app.py
   ```

## API Endpoints

- **`GET /`**: Serves the main page.
- **`POST /start_detection`**: Initiates the license plate detection process.
- **`GET /plates/<filename>`**: Retrieves the detected plate images from the server.

## Configuration

- **`SAVE_DIRECTORY`**: Directory where detected plate images are stored.
- **`HARCASCADE_PATH`**: Path to the Haar Cascade model used for plate detection.

## Usage

- Start the server using the command: `python app.py`.
- Use a tool like Postman or your browser to interact with the API.
- Access detected plates and OCR results through the API endpoints.

## Additional Information

For more details, including client-side code, microcontroller integration, and Firebase setup, please refer to the full project repository: [IOT Client Project](https://github.com/alien2112/iot-client).
