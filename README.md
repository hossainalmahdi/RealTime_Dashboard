# RealTime_Dashboard

### Step 1. Create the project structure
```
$ curl -sSL https://install.python-poetry.org | python3 -
```
### step 2. Install Poetry
```
$ poetry install
```

### Step 3. Build the UI with Streamlit
```
$ poetry add streamlit
```

### Step 4. Run the app 
```
$ poetry run streamlit run main.py --server.runOnSave true
```