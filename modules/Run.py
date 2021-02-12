#
import argparse
from Week2 import read_csv, write_lines_to_file
from utils import get_file_names, get_all_file_names, print_line_one, print_emails, write_headlines

parser = argparse.ArgumentParser(description='A program that write and read from a csv file')
parser.add_argument('-f', dest="file", required=True, help='csv file')
parser.add_argument("-o", dest="outfile", default=None, help='The name of the file to store the url in')


file_names = ['/home/jovyan/python_handin_template/modules/textfiles/text1.txt',
             '/home/jovyan/python_handin_template/modules/textfiles/text2.txt',
             '/home/jovyan/python_handin_template/modules/textfiles/text3.txt']


args = parser.parse_args()
file = args.file
outfile = args.outfile

output_list = read_csv(file)
#string_tuples = [('A', 'B', 'C'), 
#             ('Tutorialspoint', 'is a', 'popular',
#                'site', 'for tech learnings')]

if outfile != None:
    write_lines_to_file(outfile, output_list)
else:
    print(output_list)
