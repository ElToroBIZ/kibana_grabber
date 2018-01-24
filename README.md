# kibana_grabber
Grab ElasticSearch data using insecure Kibana instances into file

## Description
Kibana restricts amount of data whitch can be retrieved using general ElasticSearch queries(10K per query).
This sample demonstrates usage of scrolling mechanism that is not restricted in kibana and can be used to pull all data from ElasticSearch index inside of Kibana.

## Usage
```python3 -m kibana_grabber --host=http://hostname --index=accounts```

## Example sources
Tested with Kibana 6.x.x instances. 

Useful with servers found in https://zoomeye.org with dork  ```+port:"5601" +service:"http" +app:"Elasticsearch Kibana"```
