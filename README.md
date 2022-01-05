### 0. Intro
Web app for Shopify Backend Developer Inter Challenge - Summer 2022.

Implemented basic CRUD and data export.
### 1. env setup
- Recommend install python 3.9.7 with conda.
```bash
conda create -n test python=3.9.7
conda activate test

pip install -r requirements.txt
```

### 2. run
```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```
