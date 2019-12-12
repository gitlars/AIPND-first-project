#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/add_summary_results.py
#                                              
# PROGRAMMER: Lars Cremean
# DATE CREATED: 2019-12-08                      
# REVISED DATE: 
# PURPOSE: Takes the results statistics and updates or appends these to a
#          dictionary final_results_dic, which is initialized by loading a
#          text file of the same name, updated, and then written back out.
#          Function inputs:
#            - results_stats_dic, the dictionary of statistics results for a single execution of a classifier on a particular data set
#            - folder, the name of the folder of images used in the classifier execution
#            - arch, the architecture of the classifier model used
#            - tot_time, the total execution time in seconds
##

from os import path
import ast

def add_summary_results(results_stats, folder, arch, tot_time):
    """Load summary results to a dictionary and keep in sync with a file of the same name.
    Args:
        results_stats_dic: the dictionary of statistics results for a single execution of a classifier on a particular data set
        folder: the name of the folder of images used in the classifier execution
        arch: the architecture of the classifier model used
        tot_time: the total execution time in seconds
    Returns:
        None
    """
    
    summary_results_filename = "summary_results_dic.txt"
    # https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    dir_path = path.dirname(path.realpath(__file__))
    abs_path = dir_path + "/" + summary_results_filename

    # If the summary dictionary file exists, load it from file, otherwise initialize it
    if path.isfile(summary_results_filename):
        print("\nFound {}".format(summary_results_filename))
        with open(abs_path) as fp:
            summary_results_str = fp.read()
            summary_results_dic = ast.literal_eval(summary_results_str)
    else:
        print("Did not find {}, so initializing it".format(summary_results_filename))
        summary_results_dic = dict()
    
    # Add results to the dictionary
    # The final_results_dic has a string key which is a concatenation of the folder name and architecture
    # It has a list value where the indices of the list contain:
    #     0: n_images - total number of images in set
    #     1: n_dogs_img - number of dog images in set
    #     2: n_notdogs_img - number of not-a-dog images in set
    #     3: pct_correct_dogs - % of dog images correctly classified as dogs
    #     4: pct_correct_notdogs - % of not-a-dog images correctly classified as not-a-dog
    #     5: pct_correct_breed - % of dog images classified with the correct breed
    #     6: pct_match - % of all images correctly classified 
    #     7: tot_time - total time in seconds of the classifier execution
    key = folder.replace("/", "") + "_" + arch
    
    summary_results_dic[key] = [
        results_stats["n_images"],
        results_stats["n_dogs_img"],
        results_stats["n_notdogs_img"],
        results_stats["pct_correct_dogs"],
        results_stats["pct_correct_notdogs"],
        results_stats["pct_correct_breed"],
        results_stats["pct_match"],
        tot_time]

    # Write the dictionary back out to text file
    with open(summary_results_filename, "w") as fp:
        print(summary_results_dic, file=fp)
