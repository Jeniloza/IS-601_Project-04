FROM python:3.9

EXPOSE 5005

WORKDIR /Flask_App_Factory

COPY requirements.txt /Flask_App_Factory
RUN pip install  -r requirements.txt --upgrade pip

COPY . /Flask_App_Factory

CMD python app.py