# pyinstaller --onefile main.py
import os
import xml.etree.ElementTree as ET
import time

def search_xml():
    dir_name = input('Enter the XML directory-path to be searched: ')
    search_string = input('Enter the String you want to search in all files: ')
    
    # Iterate through all files in the directory
    for filename in os.listdir(dir_name):
        # Only consider XML files
        if filename.endswith('.xml'):
            # Parse the XML file
            tree = ET.parse(os.path.join(dir_name, filename))
            # Search for the string in the file
            if search_string in ET.tostring(tree.getroot()).decode():
                print('Found in file:', filename)
            else:
                continue
                
    print('\nDone searching')
                    
if __name__ == '__main__':
    print('''
        __   ____  __ _         _____                                
        \ \ / /  \/  | |       / ____|                               
         \ V /| \  / | |      | (___   ___ _ __ __ _ _ __   ___ _ __ 
          > < | |\/| | |       \___ \ / __| '__/ _` | '_ \ / _ \ '__|
         / . \| |  | | |____   ____) | (__| | | (_| | |_) |  __/ |   
        /_/ \_\_|  |_|______| |_____/ \___|_|  \__,_| .__/ \___|_|   
                                             | |              
                                             |_|       
                                                                    
                                                                                                                  
                made by Jonas Miersch & ChatGPT AI 2022
                
          ''')

    search_xml()
    
    # Search again?
    while True:
        search_again = input('Search again? (Y/N) \n')   
        if search_again == 'Y':  
            search_xml()
        else:
            print('Thank you for using my tool!')
            time.sleep(2)
            quit()
