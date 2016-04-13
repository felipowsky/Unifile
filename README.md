# Merge All Files

[![Build Status](https://travis-ci.org/felipowsky/MergeAllFiles.svg?branch=master)](https://travis-ci.org/felipowsky/MergeAllFiles)

## Description
This python script will merge the content from all the files in a directory and its subdirectores into one file.

Edit `extensions` variable to configure which type of files you want to merge.

Example:
```python
extensions = ['.swift', '.h', '.m', '.cpp', '.c', '.py', '.java']
```

## Usage

To merge files from current directory:
```bash
./merge_all_files.py
```

To merge files from a specific directory:
```bash
./merge_all_files.py <directory>
```
