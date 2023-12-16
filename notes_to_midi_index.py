import os
import shutil

def rename_files(directory_path):
    octaves = [0, 1, 2, 3, 4, 5, 6, 7]
    notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    index = -1
    for o in octaves:
        if o == 0:
            octave_notes = ['A', 'B']
        else:
            octave_notes = notes
        for n in octave_notes:
            if os.path.exists(directory_path + 'mp3/' + n + 'b' + str(o) + '.mp3'):
                index += 1
                shutil.copyfile(directory_path + 'mp3/' + n + 'b' + str(o) + '.mp3', directory_path + 'index/' + str(index) + '.mp3')
            if os.path.exists(directory_path + 'mp3/' + n + str(o) + '.mp3'):
                index += 1
                shutil.copyfile(directory_path + 'mp3/' + n + str(o) + '.mp3', directory_path + 'index/' + str(index) + '.mp3')

# Replace 'your_directory_path' with the actual path of the directory
directory_path = 'C:/Users/Noah Freedman/Documents/information/projects/interval_trainer/grand_piano/'

# Call the function to rename files in the specified directory
rename_files(directory_path)
