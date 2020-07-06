import nbformat
import sys

if len(sys.argv) < 2:
	print("Error, please run as: python3 wordcount <test.ipynb>")
	sys.exit(1)

with open(sys.argv[1]) as f:
    nb = nbformat.read(f, as_version=4)
    total_words = 0

    for cell in nb['cells']:
        if cell['cell_type'] == 'markdown':
            total_words += len(cell['source'].split())
    print("Total words:", total_words)
