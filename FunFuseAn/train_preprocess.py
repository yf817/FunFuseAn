#############This script preprocesses the training data ##############

#import the relevant packages
import os
import natsort
import glob
import numpy as np
import imageio
from FunFuseAn.init_param import init_param

image_length, image_width, gray_channels, batch_size, epoch, lr, images_pet, images_mri = init_param()

def train_preprocess_mri(image_width, image_length):
    filenames = os.listdir('/home/...../Training/MRI/')
    dataset = os.path.join(os.getcwd(), '/home/...../Training/MRI/')
    data = []
    for ext in ('*.gif', '*.png', '*.jpg','*.tif'):
        data.extend(glob.glob(os.path.join(dataset, ext)))
    data = natsort.natsorted(data,reverse=False)
    train_mri = np.zeros((len(data), image_width,image_length),dtype=float)
    for i in range(len(data)):
        train_mri[i,:,:] =(imageio.imread(data[i]))
        train_mri[i,:,:] =(train_mri[i,:,:] - np.min(train_mri[i,:,:])) / (np.max(train_mri[i,:,:]) - np.min(train_mri[i,:,:]))
        train_mri[i,:,:] = np.float32(train_mri[i,:,:])
    
    train_mri = train_mri[:,:,:,np.newaxis]
    return train_mri
    
 
def train_preprocess_pet(image_width, image_length):    
    filenames = os.listdir('/home/...../Training/PET/')
    dataset = os.path.join(os.getcwd(), '/home/...../Training/PET/')
    data = []
    for ext in ('*.gif', '*.png', '*.jpg','*.tif'):
        data.extend(glob.glob(os.path.join(dataset, ext)))
    data = natsort.natsorted(data,reverse=False)
    train_pet = np.zeros((len(data),image_width,image_length),dtype=float)
    for i in range(len(data)):
        train_pet[i,:,:] =(imageio.imread(data[i]))
        train_pet[i,:,:] =(train_pet[i,:,:] - np.min(train_pet[i,:,:])) / (np.max(train_pet[i,:,:]) - np.min(train_pet[i,:,:]))
        train_pet[i,:,:] = np.float32(train_pet[i,:,:])
        
    train_pet = train_pet[:,:,:,np.newaxis]
    return train_pet
    
    
  
