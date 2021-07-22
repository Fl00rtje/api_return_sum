# API 

Welcome!
This API returns the sum of two numbers. This project is written in Python and the Django REST framework.

### How to start with the project
1. Create a new directory
2. Create a virtual environment for the project
3. Clone the project to your computer: git clone https://github.com/Fl00rtje/api_return_sum.git
4. Install the requirements: pip install -r requirements.txt
5. Make the migrations: python manage.py makemigrations
6. Migrate: python manage.py migrate
7. Run the server: python manage.py runserver

### Data format
The data format is JSON. This holds for the input as well as for the output.

### Endpoint
You can either navigate to the endpoint in your browser and submit the data there or send a request from your terminal.
The browser version will provide you with some extra information. Check it out! :D

The endpoint is: http://127.0.0.1:8000/sum/

### Input
- Please provide as **key** "input".
- The **value** should be of the form "100 + 4".

For example: {"input": "100 + 4"}

### Output
- The first number is returned as the value of "num_1".
- The second number is returned as the value of "num_2".
- The sum of the first and second number is returned as "total".

For example:
{
    "num_1": 100,
    "num_2": 4,
    "total": 104
}


