import cv2
import torch
import matplotlib.pyplot as plt
import os


# @brief Generates depth maps from a video using the MiDaS model
# @param video_path: Path to the input video file.
# @param output_path: Path to the output folder where the generated depth maps will be saved
def videoDepthEstimation(video_path, output_path, model_type = 'DPT_Large'):
    # Load the MiDaS model
    midas = torch.hub.load('intel-isl/MiDaS', model_type)
    
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    midas.to(device)
    midas.eval()
    
    # Load the MiDaS transforms
    midas_transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
    
    # Choose the appropriate transform based on the model type
    if model_type == 'DPT_Large' or model_type == 'DPT_Hybrid':
        transform = midas_transforms.dpt_transform
    elif model_type == 'MiDaS_small' :
        transform = midas_transforms.small_transform
    
    # Open the video file
    video = cv2.VideoCapture(video_path)
    
    # Create the output folder path
    os.makedirs(output_path, exist_ok=True)
    
    # Initialize frame counter
    frame_count = 0
    
    # Iterate over frames in the video
    while True:
        # Read the next frame from the video
        ret, frame = video.read()
    
        # Break the loop if no more frames are available
        if not ret:
            break
    
        # Convert the frame to RGB color space
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
        # Apply the MiDaS transform to preprocess the frame
        input_batch = transform(frame_rgb).to(device)
    
        with torch.no_grad():
            # Pass the preprocessed frame through the MiDaS model
            prediction = midas(input_batch)
    
            # Resize the predicted depth map to match the frame size
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=frame.shape[:2],
                mode='bicubic',
                align_corners=False,
            ).squeeze()
    
        # Convert the predicted depth map to numpy array
        depth_map = prediction.cpu().numpy()
    
        # Save the depth map to a file in the output folder
        depth_map_filename = os.path.join(output_path, f'depth_map_{frame_count}.png')
        cv2.imwrite(depth_map_filename, depth_map)
    
        # Increment the frame counter
        frame_count += 1
    
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture and close the windows
    video.release()
    cv2.destroyAllWindows()

