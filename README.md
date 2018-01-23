# kibana_grabber
Grab data from insecure Kibana instance into file

Usage: python3 -m kibana_grabber --host=http://hostname --index=accounts

Tested with Kibana 6.x.x

Useful with servers found in zoomeye.org with dork  +port:"5601" +service:"http" +app:"Elasticsearch Kibana"
