
# Pose Estimation

Welcome to the Pose Estimation repository! This project leverages computer vision and machine learning techniques to detect human poses from video footage using the MediaPipe library.

## Overview

This repository provides scripts for detecting and analyzing human poses from video footage. The core functionality is built on the MediaPipe library, enabling accurate detection of key landmarks and calculation of angles for various body parts. The project is particularly useful for applications such as gait analysis.

### Key Features

- **Pose Detection**: Identify and visualize key body landmarks.
- **Angle Calculation**: Compute angles between specified landmarks (e.g., elbows, knees, shoulders, hips).
- **CSV Logging**: Save computed angles frame-by-frame for further analysis.
- **Customizable Visualization**: Annotate frames with landmark points and angles.
- **Gait Analysis**: Analyze the gait cycle by tracking and evaluating leg movements.

## Dependencies

- OpenCV
- MediaPipe
- CSV
- Time
- Math

## Setup

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Bilal-Javed-Goraya/PoseEstimation.git
    cd PoseEstimation
    ```

2. **Install Required Packages**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Pose Detection and Angle Calculation

Run the main script to start detecting poses and calculating angles from a video file:

```sh
python find_angle.py
```

This script will read frames from `Zohaib.mp4`, detect poses, calculate angles for specified body parts, and save the results in `angles.csv`.

### Script Details

- **`find_angle.py`**: Main script to process video frames, detect poses, and calculate angles.
- **`PoseModule.py`**: Module containing the `poseDetector` class with methods for pose detection, landmark extraction, and angle calculation.

## Gait Analysis

Gait analysis is a key application of this project. By tracking the movements and angles of the lower body, specifically the knees and hips, this tool can help in studying the gait cycle. The angle calculations can provide insights into walking patterns, identify abnormalities, and aid in rehabilitation processes.

## Example Output

Here is an example of the pose estimation output:

![PoseEstimation](https://github.com/Bilal-Javed-Goraya/PoseEstimation/blob/main/Output.jpg)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [MediaPipe](https://google.github.io/mediapipe/) by Google for the powerful pose detection solution.
- [OpenCV](https://opencv.org/) for computer vision functionalities.
