RUN mkdir /data
WORKDIR /data
ADD ..
RUN pip3 install flask
ENV PORT 5000
EXPOSE 5000
CMD ["python3","app1_1_simple_prog_to_access_diff_webpages_using_url.py"]
