#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_summary_results.py
#                                              
# PROGRAMMER: Lars Cremean
# DATE CREATED: 2019-12-08                      
# REVISED DATE: 
# PURPOSE: Reads the file "summary_results_dic.txt" and prints the output.
##

from os import path
import ast

def main():
    print_summary_results()

def print_summary_results():

    summary_results_filename = "summary_results_dic.txt"
    # https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    dir_path = path.dirname(path.realpath(__file__))
    abs_path = dir_path + "/" + summary_results_filename

    with open(abs_path) as fp:
        summary_results_str = fp.read()
        summary_results_dic = ast.literal_eval(summary_results_str)

    print("Here is a summary of latest results collected to date for each folder and CNN architecture...")
    print("(N = # total images, D = # Dog images, B = Breed, C = Correct)")
    print("{:>25}    N   D  !D    %DC   %!DC    %BC     %C    TIME".format("folder_arch"))
    for key in summary_results_dic:
        print("{:>25}: {:3} {:3} {:3}  {:5}  {:5}  {:5}  {:5}  {:6}".format(
            key, 
            summary_results_dic[key][0], summary_results_dic[key][1], 
            summary_results_dic[key][2], round(summary_results_dic[key][3], 2),
            round(summary_results_dic[key][4], 2), round(summary_results_dic[key][5], 2),
            round(summary_results_dic[key][6], 2), round(summary_results_dic[key][7], 3)))

# Call to main function to run the program
if __name__ == "__main__":
    main()