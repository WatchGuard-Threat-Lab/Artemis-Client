Artemis-Client
==============
Artemis is a python-based honeypot system built using several open source tools. Artemis-Client
uses the Thug honeyclient to scrape websites for potential malware.

Artemis has been released uner the GNU GPLv3, as published by the FSF.

Installing
==========
```
apt-get install python-socks build-essential python-dev python-setuptools libboost-python-dev libboost-all-dev libemu-dev subversion curl python-pip libxml2-dev libxslt-dev graphviz libgraphviz-dev git libtool graphviz-dev automake libssl-dev libfuzzy-dev libffi-dev graphviz python-pygraphviz libjpeg8-dev autoconf

pip install thug==0.9.4

git clone https://github.com/buffer/pyv8.git
cd pyv8
python setup.py build
python setup.py install
cd ..
rm -rf pyv8

cd /opt
git clone https://github.com/WatchGuard-Threat-Lab/Artemis-Client.git
cd Artemis-Client
python setup.py build
python setup.py install


Set up thug logging
cp /usr/local/lib/python2.7/dist-packages/etc/thug/logging.conf.default /usr/local/lib/python2.7/dist-packages/etc/thug/logging.conf


Edit logging.conf to configure hpfeeds

Edit /opt/artemis-client/config.cfg to configure hpfeeds
```

Usage
=====

python /opt/Artemis-Client/artemis.py start
