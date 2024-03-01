import cv2
import torch
import matplotlib.pyplot as plt
import os


# ==========================================================================================
# Code snippet taken from https://pytorch.org/hub/intelisl_midas_v2/
# ==========================================================================================
# Model examples to infer the depth estimation
# model_type = 'DPT_Large' # MiDaS v3 - Large (highest accuracy, slowest inference speed)
# model_type = 'DPT_Hybrid' # MiDaS v3 - Hybrid (medium accuracy, medium inference speed)
# model_type = 'MiDaS_small' # MiDaS v2.1 - Small (lowest accuracy, highest inference speed)
# ==========================================================================================


# @brief Function to get the depth estimation of an image using the MiDaS model
# @param filename: Name of the image to get the depth estimation
# @param model_type: MiDaS model to use for the estimation
# @return outputImage: Numpy array with the image depth estimation result
def depthImageEstimation(filename = '', model_type = 'DPT_Large', displayResult = False):
    try:
        midas = torch.hub.load('intel-isl/MiDaS', model_type)

        device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
        midas.to(device)
        midas.eval()

        midas_transforms = torch.hub.load('intel-isl/MiDaS', 'transforms')

        if ((model_type == 'DPT_Large') or (model_type == 'DPT_Hybrid')):
            transform = midas_transforms.dpt_transform
        else:
            transform = midas_transforms.small_transform

        img = cv2.imread(filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        input_batch = transform(img).to(device)
        with torch.no_grad():
            prediction = midas(input_batch)
            prediction = torch.nn.functional.interpolate(prediction.unsqueeze(1), size=img.shape[:2], mode='bicubic', align_corners=False,).squeeze()

        outputImage = prediction.cpu().numpy()

        if (displayResult):
            plt.imshow(outputImage)
            plt.show()

        return outputImage

    except NameError:
        raise NameError


