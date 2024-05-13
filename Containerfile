FROM python:3.10-slim

EXPOSE 8501

RUN pip install --upgrade pip
RUN pip install streamlit

WORKDIR /app
ENV MAIN_APP_FILE="0_🏡_Main page.py"
COPY ./${MAIN_APP_FILE} .
COPY pages /app/pages
COPY utils /app/utils
ADD start_app.sh /tmp
CMD bash /tmp/start_app.sh
