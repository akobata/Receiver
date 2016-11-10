FROM alpine:3.1

# Update
RUN apk add

# Install app dependencies
RUN pip install stomp.py

# Bundle app source
COPY Receiver.py /src/Receiver.py

EXPOSE 61613
CMD ["python","/src/Receiver.py"]
