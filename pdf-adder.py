#!/usr/bin/python3
import PyPDF2
import os, sys


def merge_pdfs(f_names, merged_file):
    merger = PyPDF2.PdfFileMerger()
    opened_files = [open(file, 'rb') for file in f_names]
    for file in opened_files:
        try:
            merger.append(file)
        except:
            print("Error merging {}".format(file))
            raise
    with open(merged_file, 'wb') as f:
        merger.write(f)
    [file.close() for file in opened_files]
    print("Merged output is in '{}'.".format(merged_file))


if __name__ == '__main__':
    f_names = []
    if len(sys.argv) == 2:
        merged_file = sys.argv[1]
    else:
        merged_file = 'merged_file.pdf'
    [f_names.append(filename) for filename in sorted(os.listdir('.')) if filename.endswith('.pdf')]
    merge_pdfs(f_names, merged_file)








