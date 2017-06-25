
* Fork and clone this repository
* Create a virtualenv using `virtualenv venv; source venv/bin/activate`
* Install all the requirements using `pip install -r requirements.txt`
* Run the tests on your own computer with `pytest` the output should look like this:

```
========= test session starts ==========
platform darwin -- Python 3.5.2, pytest-3.0.7, py-1.4.33, pluggy-0.4.0
rootdir: /Users/gabor/work/co-learning-python-with-test, inifile:
collected 1 items

tests/test_lev.py .

======= 1 passed in 0.29 seconds =======
```

* For this you'll need to install `pytest` and then run `pytest` or `py.test` on older versions.
* Then set up Travis-CI for this project. Create the `.travis.yml` file, configure the Travis-CI service.
* Once Travis works in your own GitHub/Travis-CI accounts, send a pull-request.
* We will comment on the PR, but won't merge it.

  295  sudo apt install python3-venv
  296  pyvenv venv
  297  source venv/bin/activate
  298  pip install -r requirements.txt 
  299  pytest 
