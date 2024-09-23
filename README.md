# License Plate Detection Server

Welcome to the **License Plate Detection Server**! This repository features a Flask-based server that leverages OpenCV and EasyOCR to detect and read license plates from a video feed. The system captures license plates and performs Optical Character Recognition (OCR) to extract the text, utilizing a Haar Cascade model for plate detection and providing a simple API for interaction.

## Key Features

- **Real-time License Plate Detection**: Utilizes OpenCV and Haar Cascade to identify license plates in live video frames.
- **Optical Character Recognition (OCR)**: Employs EasyOCR to extract text from detected license plates with high accuracy.
- **API Endpoints**: Includes endpoints to start and manage plate detection, view captured images, and retrieve OCR results.
- **Concurrency Control**: Implements a locking mechanism to ensure that only one detection operation occurs at a time, preventing conflicts.

## Requirements

To run this project, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-CORS
- OpenCV (`cv2`)
- EasyOCR
- A compatible camera device for video input

## Installation

Follow these steps to set up the project on your local machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/alien2112/iot-flask.git
   cd iot-flask
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Haar Cascade XML file** and place it in the `model` directory:
   - Haar Cascade file: [Haar Cascade for Russian Plate Number](https://github.com/opencv/opencv/tree/master/data/haarcascades)

4. **Run the server**:
   ```bash
   python app.py
   ```

## API Endpoints

The server exposes the following API endpoints:

- **`GET /`**: Serves the main page of the application.
- **`POST /start_detection`**: Initiates the license plate detection process.
- **`GET /plates/<filename>`**: Retrieves the images of detected license plates from the server.

## Configuration

You can customize the following configurations in your application:

- **`SAVE_DIRECTORY`**: Specify the directory where detected plate images will be stored.
- **`HARCASCADE_PATH`**: Set the path to the Haar Cascade model used for plate detection.

## Usage

1. Start the server by running:
   ```bash
   python app.py
   ```

2. Use a tool like Postman or your web browser to interact with the API.

3. Access detected plates and OCR results through the provided API endpoints.

## Additional Information

For more details, including client-side code, microcontroller integration, and Firebase setup, please refer to the full project repository: [IOT Client Project](https://github.com/alien2112/iot-client).


