import requests


class KibanaScroll:
    """
        Scroll over ElasticSearch data using scrolling mechanism using Kibana Proxy
    """
    INIT_URL = '{kibana_host}/api/console/proxy?path={kibana_index}/_search?scroll=1m&method=POST'

    def __init__(self, kibana_host, kibana_index, kibana_version='6.0.0', batch_size=10000):
        self._kibana_host = kibana_host
        self._kibana_index = kibana_index
        self._kibana_version = kibana_version
        self._headers = {'kbn-version': kibana_version}
        if batch_size > 10000:
            raise ValueError('Batch limit in scroll cannot be greater than 10K')
        else:
            self._batch_size = batch_size
        self._scroll_id = None

    def __iter__(self):
        return self

    def __next__(self):
        if not self._scroll_id:
            es_data = self.__init_scroll()
        else:
            es_data = self.__regular_scroll()
        if not es_data:
            raise StopIteration
        else:
            return es_data

    def __init_scroll(self):
        payload = {
            'size': self._batch_size,
            'query':  {'match_all': {}}
        }
        resp = requests.post(KibanaScroll.INIT_URL.format(kibana_host=self._kibana_host,
                                                          kibana_index=self._kibana_index),
                             json=payload,
                             headers=self._headers)
        json_body = resp.json()
        self._scroll_id = json_body['_scroll_id']
        return json_body['hits']['hits']

    def __regular_scroll(self):
        payload = {
            "scroll_id": self._scroll_id,
            "scroll": "1m"
        }
        resp = requests.post('{kibana_host}/api/console/proxy?path=_search/scroll&method=POST'.format(kibana_host=self._kibana_host),
                             json=payload,
                             headers=self._headers)
        json_body = resp.json()
        return json_body['hits']['hits']
