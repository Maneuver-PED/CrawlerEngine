from ontology_engine.ontology_engine import OntologyEngine
from providers.provider_crawl import ProviderCrawl
import json
import sys


def async_crawl(esendpoint):
    seed = json.load(open('../../data/seed.json'))
    crawl = ProviderCrawl(seed=seed, esendpoint=esendpoint)
    carwled = crawl.crawl()
    if not carwled:
        sys.exit(1)

    try:
        ontology = OntologyEngine()
        ontology.load_ontology()
        data = json.load(open('../../data/crawled_aws.json'))
        ontology.sync(data, 'amazon')

        data2 = json.load(open('../../data/crawled_goo.json'))
        ontology.sync(data2, 'google')
    except Exception as inst:
        sys.exit(1)
    sys.exit(0)