#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lars Cremean
# DATE CREATED: 2019-12-04                       
# REVISED DATE: 2019-12-10
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
##
# Imports python modules
from os import listdir

# Define get_pet_labels function below please be certain to replace None
# in the return statement with results_dic dictionary that you create 
# with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    filename_list = listdir(image_dir)
    
    # Creates empty dictionary named results_dic
    results_dic = dict()
    
    # Adds new key-value pairs to dictionary ONLY when key doesn't already exist. 
    # This dictionary's value is a List that contains only one item - the pet image label
    for filename in filename_list:
        
        # Skip file if starts with . (like .DS_Store of Mac OSX) because it isn't a pet image file
        if filename[0] == ".":
            print("** Info: Skipping hidden file {}".format(filename))
        
        elif filename not in results_dic:
            
            pet_name = ""
            # account for possibility of single word filename without underscore
            last_dot_index = filename.rfind(".")
            filename_without_ext = filename[:last_dot_index]
            filename_words = filename_without_ext.lower().split("_")
            
            # Loops to check if word in pet name is only
            # alphabetic characters - if true append word
            # to pet_name separated by trailing space 
            for word in filename_words:
                if word.isalpha():
                    pet_name += word + " "
                    
            # Strip off starting/trailing whitespace characters 
            pet_name = pet_name.strip()
            
            pet_name_list = []
            pet_name_list.append(pet_name)
            
            # Add to dictionary
            results_dic[filename] = pet_name_list
            
        else:
            print("** Warning: Key=", filename, "already exists in results_dic with value", results_dic[filename])
    
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
