# Project 2 (continuation of Lab 7)
## What this project does:
The script goes out to a website and downloads it as an HTML file.  For now, it just gets the html file for www.uc.edu .
After it gets the HTML file, it removes all the empty line breaks.
### Usage instructions
1. Install requests
Linux:
```bash
virtualenv ~/venv/requests
source ~/venv/bin/activate
pip install requests
```
Windows:
```powershell
virtualenv C:\venv\requests
C:\venv\requests\Scripts\activate.ps1
pip install requests
```

2. From the folder that contains project2.py, run the program using Python
```python project2.py```

3. It will save the files off as uc_homepage.html and uc_homepage_cleaned.html

---
When done, deactivate the virtual environment
```
deactivate
```