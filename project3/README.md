# Project 3: Splitting a giant excel file
## What this project does:
For work, we were given a 272MB Excel file.  It's about 350,000 rows and the columns go out to DQ (A-Z, AA-AZ, BA-BZ, CA-CZ, DA-DQ).
When I tried to open it, it took over 24 hours (26 hours I believe) to do so.
<br \>
Utilizing Python, we will split the file into more managable files.  With my original file, it took longer than an hour (up to around 2 hours total before I stopped it) to split it all up at 100,000 splits.
Unfortunately, I am unable to provide the actual original Excel file, however, included is a script to create a similar (but smaller) sample.
<br \>

### Usage instructions
1. install pandas, numpy, openpyxl, and faker  
<br \>
**NOTE** Faker is only required if you want to make your own fake excel data files.
<br \>
Linux:
```bash
virtualenv ~/venv/giantfile
source ~/venv/bin/activate
pip3 install pandas
pip3 install numpy
pip3 install openpyxl
pip3 install faker
```
<br \>
Windows:
```powershell
virtualenv C:\venv\giantfile
C:\venv\giantfile\Scripts\activate.ps1
pip install pandas
pip install numpy
pip install openpyxl
pip install faker
```
<br \>
Alternatively for the pip install lines, you can just do:
Linux:
```bash
pip3 install -r requirements.txt
```
<br \>
Windows:
```powershell
pip install -r requirements.txt
```
<br \>
2. (Optional) Run the sampler script to create dummy files.  Suggestion would be 50,000 for amount of rows.  Resulting files should be about 2MB each.  Filenames are this-file-is-fake-data.csv and this-file-is-fake-data.xlsx
<br \>
Windows:
```powershell
python sampler.py
```
<br \>
Linux:
```bash
python3 sampler.py
```
<br \>
<br \>
3. Run <filename.py> and provide the information as needed.  Suggestion for the rowsize would be 10,000 for rows per file.
<br \>
Windows:
```powershell
python <filename>.py
```
<br \>
Linux:
```bash
python3 <filename>.py
```
Resulting files will be named split_##.xlsx or split_##.csv
<br \>
<br \>

## Known issues
1. At least with the original Excel file, I get a warning:
```
C:\venv\giantfile\lib\site-packages\openpyxl\styles\stylesheet.py:221: UserWarning: Workbook contains no default style, apply openpyxl's default
  warn("Workbook contains no default style, apply openpyxl's default")
```
However, this is not a showstopper.  It is just a warning.  Also worth noting that I did not get the same warning with the fake data.
<br \>
2. Not really an issue but a limitation of sorts.  It will not work with xls files.  XLS files are files created by Office 2003 and earlier.  Microsoft changed their file formats beginning in Office 2007 to include an additional "x" (docx, xlsx, pptx, etc.)