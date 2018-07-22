#!/usr/bin/env python
#-*- coding: utf-8 -*-

import argparse
import os
import sys
import contextlib
from argparse import ArgumentParser
from typing import List
import PyPDF2



def execute(parser: ArgumentParser):
    if parser.file[-3:] != "pdf":
        print(f'{parser.file} must be a pdf!')
        sys.exit(1)
    
    if not args.rotate:
        print ('--rotate needs to be used. -h for more information.')
        sys.exit(1)
    
    if not args.angle:
        print ('--angle needs to be used. -h for more information')
        sys.exit(1)
    try:
        pages = [int(i) for i in parser.pages]
        rotate_pdf(parser,pages)
    except FileNotFoundError:
        print(f'{parser.file} could not be found in the same directory!')
        sys.exit(1)
    except ValueError:
        print('--pages must be integer!')
        sys.exit(1)

def rotate_pdf(parser: ArgumentParser,page_array: List):
    with open(parser.file, 'rb') as f:
        print(f'Opening {parser.file}')
        pdf_reader = PyPDF2.PdfFileReader(f)
        pdf_writer = PyPDF2.PdfFileWriter()
        
        all_pages = True if not parser.pages else False
        clockwise = True if parser.rotate == "clockwise" else False
        rotate_angle = float(parser.angle)
        for page_no in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_no)
            if all_pages or page_no+1 in page_array:
                if clockwise:
                    print(f'Rotating page {page_no+1} at {rotate_angle} degrees clockwise')
                    page.rotateClockwise(rotate_angle)
                else:
                    print(f'Rotating page {page_no+1} at {rotate_angle} degrees counter-clockwise')
                    page.rotateCounterClockwise(rotate_angle)
            pdf_writer.addPage(page)
        with open(f'{parser.file[:-4]}_rotated.pdf','wb') as outfile:
            pdf_writer.write(outfile)
            print(f'Written to {parser.file[:-4]}_rotated.pdf')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple cli tool using PyPdf2 to handle pdfs')
    parser.add_argument('--pages',nargs='*', help='pages to rotate. all pages will be rotated if left blank' )
    parser.add_argument('--file',help='filename. must be run in same directory.')
    parser.add_argument('--rotate',help='direction to rotate',choices=['clockwise','anticlockwise'])
    parser.add_argument('--angle',help='angle to rotate',choices=['90','180'])
    args = parser.parse_args()

    execute(args)