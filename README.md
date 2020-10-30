# AWS Elastic Beanstalk Deployment
Failed with critical error:
```
Unsupported upgrade request.
```

### FastAPI Deployment
- [Hello World Test]()
- [Iris Example Predictions - SVM Classification]()


### Project Structure
- Project Directory
    - `/application` - Python package
        - `__init__.py` - `from application.main import application`
        - `main.py` - primary application routes and FastAPI app named `application`
        - `model.joblib` - joblib or pickled model
    - `.gitignore`
    - `builder.py` - ML model builder script (external)
    - `loader.py` - ML model loader script (external)
    - `README.md`
    - `Pipfile` - deployment dependencies


### AWS NOTES:
    - AWS wants to run application:application by default.
    - Let AWS choose the host and port numbers.
    - Let AWS make it's own Dockerfile and Procfile.
    - We provide a Python package or module and a Pipfile file zipped together into a versioned project archive.


### The deployment zip archive should include only the following
- Your Python application package or module: `/application` or `application.py`
- Package dependencies: `Pipfile`


### Iris Example Project Dependencies
- FastAPI
- pydantic
- uvicorn
- joblib
- pandas
- scikit-learn


### EB Environment Variables
In the Elastic Beanstalk Console go to your environment -> Configuration. Then
Software -> Edit. At the bottom of the page you can add a [key: value] pair for 
each of the environment variables required for the app.
