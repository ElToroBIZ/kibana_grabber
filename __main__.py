import os
import re
import json
import argparse

from .kibana_scroll import KibanaScroll


parser = argparse.ArgumentParser()
parser.add_argument("--host", required=True, help="Kibana hostname, including protocol e.g. http/https")
parser.add_argument("--port", help="Kibana port", default='5601')
parser.add_argument("--index", required=True, help="Kibana index name to grab")


if __name__ == '__main__':
    args = parser.parse_args()
    kibana_addr = '{host}:{port}'.format(host=args.host, port=args.port)
    print('Starting grabbing ElasticSearch data using Kibana')
    ks = KibanaScroll(kibana_addr, args.index)
    dir_name = re.sub(r'^https?://', '', args.host)
    work_dir = './kibana_{host}_{port}_grab'.format(host=dir_name, port=args.port)
    if not os.path.exists(work_dir):
        os.mkdir(work_dir)
    with open(work_dir + '/%s' % args.index, 'w') as out_file:
        for es_data in ks:
            print('Scrolling next page...')
            for es_doc in es_data:
                out_file.write(json.dumps(es_doc) + '\n')
