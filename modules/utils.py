import os
import re


def get_file_names(folderpath,out="output.txt"):
    filename_list = os.listdir(folderpath)
    with open(out, "w") as o:
        for el in filename_list:
            o.write(el + "\n")



def get_all_file_names(folderpath,out="output.txt"):
    for root, dirs, files in os.walk(folderpath):
        for file in files:
            with open(out, "a") as o:
                    o.write(os.path.join(root,file) + "\n")
                   
           


def print_line_one(file_names):
                for files in file_names:
                    with open(files, "r") as f:
                        print(f.readline())
      

def print_emails(file_names):
                for files in file_names:
                    with open(files, "r") as f:
                        for line in f:
                            if re.search(r'[\w\.-]+@[\w\.-]+', line):
                                print(line)



def write_headlines(md_files, out="output.txt"):
    new_list = []
    for files in md_files:
        with open(files, "r") as f:
            for line in f:
                if re.search("^#", line):
                    new_list.append(line)
                    with open(out, "w") as o:
                        for el in new_list:
                            o.write(el)