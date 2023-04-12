Income Expenses API

## An API that helps keep track of income and expenses

## Installation steps

1. Ensure you have python3 installed

2. Clone the repository
3. create a virtual environment using `python3 -m venv venv`
4. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

5. Install the dependencies using `pip install -r requirements.txt`

6. Migrate existing db tables by running `python manage.py migrate`

7. Create Super-user using `python manage.py createsuperuser`

8. Run the django development server using `python manage.py runserver`
