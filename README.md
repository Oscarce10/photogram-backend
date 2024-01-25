# Fastapi base template for Python API projects

Base template project to expand your ideas without need to set up the project from scratch.

## Installation

### Pip

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage

### Pip

```bash
uvicorn config:app --host=127.0.0.1 --port=3000 --reload --log-level=info
```


### Docker
    
```bash
$ docker build -t fastapitemplate .
$ docker run -p 3000:3000 --network host fastapitemplate

```