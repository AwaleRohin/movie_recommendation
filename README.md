### Simple movie recommendation engine created using cosine similarity

### Steps to run project
- First make sure you have `python` installed along with `pip` and `virtualenv`. Usually pip is installed along python and to install virtualenv: pip install virtualenv
- Also make sure you have installed redis: for ubuntu `sudo apt install redis-server` and for windows [check out this article](`https://redislabs.com/blog/redis-on-windows-10/`)
- Clone the repo
- Create virtualenv: `virtualenv venv` or `virtualenv -p python3 venv`
- Activate virtualenv: for linux(`source venv/bin/activate`) and for windows(`source venv/Scripts/activate`)
- Install all necessary libraries in venv: `pip install -r requirements.txt` (all necessary libraries for project are in requirements.txt file)
- Create `credentials.yaml` file with help from `credentials.yaml.example`
- Generate a `secret_key` to run the app. You can generate secret key from [here](https://djecrety.ir/)
- Create OMDb API key for `api_key` in credentials.yaml
- Finally run `python manage.py runserver` to run the project and also make sure your redis server is up `redis-server`
