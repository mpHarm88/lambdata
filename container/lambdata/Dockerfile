FROM debian
ENV PYTHONUNBUFFERED=1
RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl vim -y && \
pip3 install pandas numpy scikit-learn xgboost category_encoders && \
pip3 install -i https://test.pypi.org/simple/ lambdata-mpharm88 && \
python3 -c "import lambdata_mpharm88;print('success')"

