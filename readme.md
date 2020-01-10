** Activate Virtual Environment **

'''
source blockchain-env/Scripts/activate
'''

** Install all packages **

'''
pip install -r requirements.txt
'''

** Run the tests **
Make sure to activate virtual environment.

'''
python -m pytest backend/tests
'''