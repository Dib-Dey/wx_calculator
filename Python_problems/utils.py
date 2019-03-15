"""
module having all utility functions

    >>> from Python_problems import utils

"""
import os
import shutil
def copy_all_files_to_destination(source='', destination= ''):
    """
    copy all files inside all directories in source directory and paste in destination directory

        >>> from Python_problems import utils
        >>> utils.copy_all_files_to_destination(r"C:\Users\ddey\Downloads\photos_and_videos")

    :param source: string of source path
    :param destination: string of destination path
    :return: path where files have been copied
    """
    if not destination:
        destination = source
    for dir in os.listdir(source):
        files_dir = os.path.join(source, dir)
        try:
            total_files_in_files_directory = os.listdir(files_dir)
        except:
            total_files_in_files_directory = []
        if total_files_in_files_directory:
            for files in total_files_in_files_directory:
                path_each_file = os.path.join(files_dir, files)
                shutil.copy(path_each_file, destination)
    return("Please check the files have ben copied in ({})".format(destination))