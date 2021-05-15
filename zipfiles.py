# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:43:35 2020

@author: Admin
"""

def zip_given_files(zipped_file_name, file_paths):
    """
    input: 
        path and name of the output '.zip' file as a string ("test.zip")
        paths and names of all the files to be zipped together as list of strings
    output:
        creates the zipped file with the given name and path
    """
    import zipfile
    
    try:
    	zip_file = zipfile.ZipFile(zipped_file_name, 'w')
    	for path in file_paths:
        	zip_file.write(path, compress_type=zipfile.ZIP_DEFLATED)
    except Exception as e:
	zip_file.close()
    
    zip_file.close()	


