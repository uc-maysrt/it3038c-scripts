# My Github repo for IT3038C

### LAB 7
Linux:
```bash
virtualenv ~/venv
source ~/venv/bin/activate
pip install requests
```

Windows:
```powershell
virtualenv C:\venv\requests
C:\venv\requests\Scripts\activate.ps1
pip install requests
```

Now, in Python, run the following code
```python
import requests
target = requests.get('')
```

The syntax above will load the target url.
After the target url is loaded, we can run a few commands that we can run against the URL.

```python
target.status_code
```
status_code will reply with the HTTP response code (200, 404, etc.)

```python
target.encoding
```
encoding will return the encoding type (UTF-8, UTF-16, etc.)

```python
target.headers
```
headers will return the headers of the website

When done, deactivate the virtual environment
```
deactivate
```