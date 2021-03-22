# Lab 8
## What this project does:
### ws-newegg.py
It goes out and gets the product title, price, and stock level.
It is hardcoded to a specific item on newegg's site that should be out of stock most of the time (because graphics cards are always out of stock)—Asus ROG Strix GeForce RTX 3090.
#### Usage instructions
1. Install requests and beautifulsoup
Linux:
```bash
virtualenv ~/venv/ws-newegg
source ~/venv/bin/activate
pip install requests bs4
```
Windows:
```powershell
virtualenv C:\venv\ws-newegg
C:\venv\requests\Scripts\activate.ps1
pip install requests bs4
```
2. From the folder that contains ws-newegg.py, run the program using Python  
    Windows: ```python ws-newegg.py```  
    Linux: ```python3 ws-newegg.py```
3. It will print the output to the console.

### ws-microcenter.py
This one prompts for user input and returns the product name, price, and stock level.
It uses regex to parse the url to get the information.
#### Known issues
It does not pull product name information on:
 - Desktops (e.g. https://www.microcenter.com/product/631993/powerspec-g508-gaming-computer )
 - Laptops (e.g. https://www.microcenter.com/product/623186/hp-15-ef1072nr-156-laptop-computer---silver )
 - Phones (e.g. https://www.microcenter.com/product/618178/samsung-galaxy-a51-unlocked-4g-lte---prism-crush-black-smartphone )  
 Presumably, it is because the product name is on top and the specs are in the subheader under the product name.

It also does not pulling pricing information on items with multiple prices due to volume discounts  
e.g. https://www.microcenter.com/product/484619/eset-internet-security---1-device,-3-year-(oem)

#### Usage instructions
1. Install requests and beautifulsoup
Linux:
```bash
virtualenv ~/venv/ws-newegg
source ~/venv/bin/activate
pip install requests bs4
```
Windows:
```powershell
virtualenv C:\venv\ws-newegg
C:\venv\requests\Scripts\activate.ps1
pip install requests bs4
```
2. From the folder that contains ws-microcenter.py, run the program using Python  
    Windows: ```python ws-microcenter.py```  
    Linux: ```python3 ws-microcenter.py```
3. Follow the instruction on screen and provide a microcenter webpage.
Some example ones are:  
https://www.microcenter.com/product/634208/amd-ryzen-threadripper-pro-3995wx-castle-peak-27ghz-64-core-swrx8-boxed-processor  
https://www.microcenter.com/product/630684/asus-geforce-rtx-3070-tuf-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card  
https://www.microcenter.com/product/602978/micro-center-full-size-arcade-cabinet-32---unassembled
4. It will print the output to the console