# swyft-api

Python based API created using FastAPI

- Run the code by navigating to src and running `uvicorn src.main:app --reload` in terminal. The --reload option enables automatic reloading of the server when changes are made to the code

- Once your FastAPI app is running, you can access it in your browser or through tools like curl or httpie. For example: open your browser and go to: http://127.0.0.1:8000

## Check the Interactive API Documentation

- Option 1 Swagger UI : Go to http://127.0.0.1:8000/docs

- Option 2 ReDoc : Go to http://127.0.0.1:8000/docs

## Testing

- Install **httpx** ```pip install httpx```
- Install **pytest** ```pip install pytest```
- Run ```pytest```