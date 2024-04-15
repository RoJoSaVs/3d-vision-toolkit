import cv2
import torch
import os

# ==========================================================================================
# Model examples to infer the depth estimation
# modelType = 'DPT_Large' # MiDaS v3 - Large (highest accuracy, slowest inference speed)
# modelType = 'DPT_Hybrid' # MiDaS v3 - Hybrid (medium accuracy, medium inference speed)
# modelType = 'MiDaS_small' # MiDaS v2.1 - Small (lowest accuracy, highest inference speed)
# ==========================================================================================


class DepthEstimation():
    def __init__(self, modelType = 'DPT_Large'):
        self.modelType = modelType
        self.midas = torch.hub.load('intel-isl/MiDaS', modelType)
        self.device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        self.midas.to(self.device)
        self.midas.eval()

        midasTransforms = torch.hub.load('intel-isl/MiDaS', 'transforms')
        if ((modelType == 'DPT_Large') or (modelType == 'DPT_Hybrid')):
            self.transform = midasTransforms.dpt_transform
        else:
            self.transform = midasTransforms.small_transform


    # ==========================================================================================
    # Code snippet taken from https://pytorch.org/hub/intelisl_midas_v2/
    # ==========================================================================================
    # @brief Function to get the depth estimation of an image using the MiDaS model
    # @param imagePath: Name of the image to get the depth estimation
    # @return outputImage: Numpy array with the image depth estimation result
    def imageDepth(self, imagePath = ''):
        try:
            sourceFile = cv2.imread(imagePath)
            outputImage = self.__prediction__(sourceFile)
            return outputImage

        except NameError:
            raise NameError


    # ==============================================================================================================================
    # Code taken from https://medium.com/@daython3/exploring-depth-estimation-in-videos-using-midas-pre-trained-models-200e22276467
    # ==============================================================================================================================
    # @brief Generates depth maps from a video using the MiDaS model
    # @param videoPath: Path to the input video file.
    # @param outputVideoPath: Path to the output folder where the generated depth maps will be saved
    def videoDepth(self, videoPath = '', outputVideoPath = ''):
        try:
            video = cv2.VideoCapture(videoPath) # Open the video file
            os.makedirs(outputVideoPath, exist_ok=True) # Create the output folder path
            frameCount = 0 # Initialize frame counter

            # Iterate over frames in the video
            while True:
                ret, sourceFile = video.read() # Read the next frame from the video

                # Break the loop if no more frames are available
                if not ret:
                    break

                depthMap = self.__prediction__(sourceFile)

                # Save the depth map to a file in the output folder
                depthMapFilename = os.path.join(outputVideoPath, f'depthMap_{frameCount}.png')
                cv2.imwrite(depthMapFilename, depthMap)

                frameCount += 1 # Increment the frame counter

            # Release the video capture and close the windows
            video.release()
            cv2.destroyAllWindows()
        except NameError:
            raise NameError


    # @param sourceFile: Source element to apply the prediction of the IA model
    def __prediction__(self, sourceFile):
        # Convert the sourceFile to RGB color space
        sourcePrediction = cv2.cvtColor(sourceFile, cv2.COLOR_BGR2RGB)

        # Apply the MiDaS transform to preprocess the sourceFile
        inputBatch = self.transform(sourcePrediction).to(self.device)
        with torch.no_grad():
            # Pass the preprocessed frame through the MiDaS model
            prediction = self.midas(inputBatch)

            # Resize the predicted depth map to match the sourceFile size
            prediction = torch.nn.functional.interpolate(prediction.unsqueeze(1), size=sourcePrediction.shape[:2], mode='bicubic', align_corners=False,).squeeze()

        # Convert the predicted depth map to numpy array
        predictionResult = prediction.cpu().numpy()
        return predictionResult
