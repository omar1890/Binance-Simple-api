# Binance-Simple-api
- This is a simple flask application with 2 endpoints 
  - 1 : get the current price for a specific symbol from binance site 
  - 2 : get a historical prices for a specific symbol for a one day

- There is a notebook called Binance.ipynb which contains my tries with python-binance package and a successfull try with web socket and get price updated 

# How to run it ?
1) git clone github repo 
2) you must have a python in your machine and vs code or any code editor 
3) you should create python environment in the repo after download it
4) pip install -r requirements.txt (which contains required packages)
5) python app.py (in the same folder) 
6) access http://127.0.0.1:5000 from your browser 

# Screen from main page
![image](https://user-images.githubusercontent.com/19292752/173202884-15854291-1478-4bcd-b3f3-70cc95ca1780.png)

# Screen from historical page
![image](https://user-images.githubusercontent.com/19292752/173202847-44e64774-3fdb-4566-a985-b434416ad6dc.png)


# what is missing ?
I have already test web socket part but alone without integration with flask api 
