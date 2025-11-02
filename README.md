# fastapi-example

Basic fastapi example

# Setup

```
pip install -e .[dev]
```

# Init Database

```
python -c 'import fastapi_backend; fastapi_backend.init()'
```

# Run
```
uvicorn fastapi_backend:app --reload --host 192.168.2.22
```
