```
usage: run.py [-h] [--pages [PAGES [PAGES ...]]] [--file FILE]
              [--rotate {clockwise,anticlockwise}] [--angle {90,180}]

Simple cli tool using PyPdf2 to handle pdfs

optional arguments:
  -h, --help            show this help message and exit
  --pages [PAGES [PAGES ...]]
                        pages to rotate. all pages will be rotated if left
                        blank
  --file FILE           filename. must be run in same directory.
  --rotate {clockwise,anticlockwise}
                        direction to rotate
  --angle {90,180}      angle to rotate

```

## Requirements
* Python 3.6+
* PyPdf2

# Usage
![Usage](/usage.png "Usage")