# Document Generator

Generate document from a CSV file using a DOCX template

---

## TL;DR

```shell
source venv/bin/activate

python main.py

docker run -it --rm --volume $(pwd)/config.py:/home/app/config.py --volume $(pwd)/data:/home/app/data --volume $(pwd)/templates:/home/app/templates --volume $(pwd)/output:/home/app/output docx-generator
```

---

## Setup

### 1. Setup Virtual Environment

```shell
python -m venv venv

source venv/bin/activate
```

### 2. Install Packages

```shell
python -m pip install --upgrade pip

pip install --upgrade docxtpl pandas

pip install --upgrade pre-commit
pre-commit install
```

`OR`

```shell
pip install -r requirements.txt
```

### 3. Add Package in Requirement file and configure pre-commit

_if change in packages then update the requirements with below cmd_

```shell
pip freeze > requirements.txt
```

---

## Docker

### 1. Build Docker Image

```shell
docker build -t docx-generator .
```

### 2. Run Docker Image

```shell
docker run -it --rm --volume $(pwd)/config.py:/home/app/config.py --volume $(pwd)/data:/home/app/data --volume $(pwd)/templates:/home/app/templates --volume $(pwd)/output:/home/app/output docx-generator
```

---
