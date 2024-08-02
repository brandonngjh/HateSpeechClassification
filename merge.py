import nbformat
from nbformat import NotebookNode

# Function to merge multiple notebooks
def merge_notebooks(filenames):
    merged = None
    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)
    return merged

# List of notebook filenames to merge
notebook_filenames = [
    './Task 1 Logistics Regression.ipynb',
    './Task 2 Dimension Reduction.ipynb',
    './merge.ipynb'
]

# Merge the notebooks
merged_notebook = merge_notebooks(notebook_filenames)

# Save the merged notebook
with open('merge1.ipynb', 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)
