# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 10:09:28 2023

@author: Daaff
"""

from PIL import Image
from pillow_heif import register_heif_opener


def takes_input():
    while True:
        try:
            heic_file = input("Please enter the input HEIC image file name: ")
            jpeg_file_name = input("Please enter the output JPEG image file name: ")
            
            # Check if the file names are valid
            with open(heic_file):
                pass
            with open(jpeg_file_name, 'w'):
                pass
            
            return heic_file, jpeg_file_name
        except FileNotFoundError:
            print("File not found. Please enter valid file names.")
        except PermissionError:
            print("Permission denied. Please enter valid file names.")
        except Exception as e:
            print("An error occurred:", str(e))


def heic_to_jpg(heic_file:str,jpeg_file_name:str):
    try:
        register_heif_opener()

        image = Image.open(heic_file)
        image.save(jpeg_file_name)
        print("Image saved successfully ...")
    except Exception as e:
        print("An error occurred:", str(e))


def main():
    heic_file,jpeg_file_name = takes_input()
    heic_to_jpg(heic_file, jpeg_file_name)
    
    
if __name__ == "__main__":
    main()