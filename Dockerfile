FROM python:3.8

# set a directory for the app
WORKDIR /usr

# install pip
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# copy all the files to the container
RUN git clone https://github.com/Fl00rtje/api_return_sum.git

# set a directory for the app
WORKDIR /usr/api_return_sum

# install dependencies
RUN pip install --no-cache-dir -r /usr/api_return_sum/requirements.txt
RUN pip install gunicorn

# set a directory for the app
WORKDIR /usr/api_return_sum/api_assignment

# run the migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# define the port number the container should expose
EXPOSE 8000

# run the command
CMD gunicorn api_assignment.wsgi:application --bind 0.0.0.0:8000
