FROM python:3.8.10
COPY . /deasfio_brasil_prev
WORKDIR /deasfio_brasil_prev
RUN pip install -r requirements.txt
WORKDIR /deasfio_brasil_prev/app
CMD python3 play.py