# Unifile

## Description
This python script unifies the content of multiple files into a single file.
Edit `extensions` variable in `unifile.py` to configure which files you want to merge.

Example:
```python
extensions = ['.swift', '.h', '.m', '.cpp', '.c', '.py', '.java']
```

## Usage

To unify the content of files of the current directory:
```bash
./unifile.py
```

To unify the content of files of a specific directory:
```bash
./unifile.py <directory>
```
