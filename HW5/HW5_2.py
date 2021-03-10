import os

# os.system('cls')
    
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

# original_name = input("enter your name for original file:\n")
original_name = 'pic1.png'
original_file = os.path.join(THIS_FOLDER, original_name)

# copy_name     = input("enter your name for copy file:\n")
copy_name     = 'pic1_copy.png'
copy_file     = os.path.join(THIS_FOLDER, copy_name)

with open(original_file, 'rb') as reader, open(copy_file, 'bw') as writer:
    writer.write(reader.read())








