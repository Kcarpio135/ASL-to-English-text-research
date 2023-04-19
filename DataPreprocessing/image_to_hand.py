import mediapipe as mp

# The image_to_hand output contains three components. Each component is an array, where each element contains the following results for a single detected hand:

# Handedness

# Handedness represents whether the detected hands are left or right hands.

# Landmarks
def image_to_hand(numpy_image):
    BaseOptions = mp.tasks.BaseOptions
    HandLandmarker = mp.tasks.vision.HandLandmarker
    HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
    VisionRunningMode = mp.tasks.vision.RunningMode

    # Create a hand landmarker instance with the image mode:
    options = HandLandmarkerOptions(
        base_options=BaseOptions(model_asset_path='/path/to/model.task'),
        running_mode=VisionRunningMode.IMAGE)
    with HandLandmarker.create_from_options(options) as landmarker:
        return landmarker.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=numpy_image))
    


def video_to_hand(video):
    return [image_to_hand(image) for image in video]
