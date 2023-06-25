FROM python:3.10
WORKDIR /app
COPY ["requirements.txt","app.py","model.pkl","./"] /app
RUN pip install -r requirements.txt
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]