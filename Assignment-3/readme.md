# Assignment-3
## Made by Tjalfe Møller & David Carl

<aside class="warning">
DISCLAIMER We made our SOAP server with Intellij and Java 1.8 so we sadly cant help if you are not running these applications.

Our SOAP server is written in Java 1.8 and our API server & client is written in Python 3.7.0
</aside>

### How to run SOAP server

Import as maven to your prefered IDE.
Make sure you are using Java 8. As some of the features has been removed from the later versions.

Make sure the port is avaible otherwise you will have to change it yourself in both the client and server.


### How to run the API server
Depending on how you installed python on your machine its

```
python3 apiServer.py

python apiServer.py
```

If its something else, I am very sorry you are alone in this.

Make sure the port is avaible otherwise you will have to change it yourself in both the client and server.

### How to to run the Client
Depending on how you installed python on your machine its

```
python3 client.py

python client.py
```

From here you are presented with a CLI based interface and you can use the following commands:
```
soap
api
exit
```

The names should be self explaining and further guidance will be provided once you run either commands.

### Install Python3 depencies
Run the following command depending on your pip installation
```
pip install -r requirements.txt 

pip3 install -r requirements.txt 
```