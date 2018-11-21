from flask import Flask, jsonify
from flask import request
from flask import redirect
from flask import make_response
from flask import abort
from flask import url_for
from flask import render_template
from flask import Response
from flask import send_file
from flask import send_from_directory
from flask import copy_current_request_context
from flask_restplus import Api, Resource, fields
from escore.core import ESCore
from postprocessing.offer_formatter import offer_format
import os

app = Flask(__name__)
api = Api(app, version='0.0.1', title='Offer Management System',
    description='Maneuver - Offer Management System  REST API',
)

oms = api.namespace('OMS', description='OMS operations')

cpu_model = api.model('OMS CPU', {
    "type": fields.List(fields.String(required=False, default='CPU', description="List of compute types")),
    "cpu": fields.Integer(required=False, default=1, description="Numper of vCPU cores"),
    "gpu": fields.Integer(required=False, default=0, description="Number of GPUs")
})

storage_model = api.model('OMS Storage', {
    "type": fields.List(fields.String(required=False, default='HDD', description="List of storage types")),
    "hdd": fields.Integer(required=False, default=50, description="HDD storage"),
    "ssd": fields.Integer(required=False, default=0, description="SSD Storage")
})

network_model = api.model('OMS Network', {
    "connections": fields.Integer(required=False, default=20, description="Number of expected connections"),
    "dataIn": fields.Integer(required=False, default=20, description="Estimated quantity of incoming data."),
    "dataOut": fields.Integer(required=False, default=20, description="Estimated quantity of outgoing data.")
})

keywords_model = api.model('OMS Keywords', {
    "keywords": fields.List(fields.String(required=False, default='Keyword1'))
})

model_ip = api.model('OMS IP', {
    "publicIPs": fields.Integer(required=False, default=3, description="Estimated number of public IPs"),
    "IPType": fields.String(required=False, default="IP4", description="IP version")
})
oms_req_model = api.model('OMS Req Model', {
    "memory": fields.Integer(required=False, default=512, desciption="Estimated system memory"),
    "cpu": fields.Nested(cpu_model),
    "storage": fields.Nested(storage_model),
    "network": fields.Nested(network_model),
    "keywords": fields.Nested(keywords_model),
    "operatingSystem": fields.List(fields.String(required=False, default="Linux", description="Operating system"))
})

oms_query_model = api.model("OMS Query Model", {
    "tag": fields.Nested(oms_req_model),
    "IP": fields.Nested(model_ip)
})

# Elasticsearch endpoint
esendpoint = '194.102.63.78'


# Folder locations
ontology_dir = "{}ontology_engine/".format(os.path.join(os.path.dirname(os.path.abspath(__file__)))[:-4])


@oms.route('/escore')
class ESCoreVersion(Resource):
    def get(self):
        '''List General Information related to ESCore'''
        return "ToDo"


@oms.route('/escore/info')
class ESCoreInfo(Resource):
    def get(self):
        '''Elasticsearch information'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.info()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/escore/index/<index>')
@api.doc(params={'index': "Elasticsearch index"})
class ESCoreIndex(Resource):
    def get(self, index):
        '''ES index information'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Index {}".format(index)

    def delete(self, index):
        '''Delete ES index'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Delete index {}".format(index)

    def post(self, index):
        '''Open ES Index'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Open index {}".format(index)


@oms.route('/escore/index/<index>/settings')
@api.doc(params={'index': "Elasticsearch index"})
class ESCoreIndexSettings(Resource):
    def get(self, index):
        '''Get ES Index settings'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Index settings {}".format(index)


@oms.route('/escore/cluster/health')
class ESCoreClusterHealt(Resource):
    def get(self):
        '''Elasticsearch cluster health'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.clusterHealth()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/escore/cluster/settings')
class ESCoreClusterSettings(Resource):
    def get(self):
        '''Elasticsearch cluster settings'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.clusterSettings()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/escore/cluster/state')
class ESCoreClusterState(Resource):
    def get(self):
        '''Elasticsearch cluster state'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.clusterState()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/escore/node/info')
class ESCoreNodeInfo(Resource):
    def get(self):
        '''Elasticsearch node info'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.nodeInfo()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/escore/node/state')
class ESCoreNodeState(Resource):
    def get(self):
        '''Elasticsearch node state'''
        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.nodeState()
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        response = jsonify(resp)
        response.status_code = 200
        return response


@oms.route('/query/<type>')
@api.doc(params={'type': """Output type, can be "full" or "format"."""})
class Query(Resource):
    @api.expect(oms_query_model)
    def post(self, type):
        '''OMS query'''
        type_list = ['full', 'format']
        if type not in type_list:
            response = jsonify({"error": "unsuported type", "types": ["full", "format"]})
            response.status_code = 417
            return response

        if not request.is_json:
            response = jsonify({"error": "request is not of type JSON"})
            response.status_code = 417
            return response
        if request.json is None:
            response = jsonify({'error': 'empty payload'})
            response.status_code = 417
            return response

        esconnection = ESCore(esendpoint)
        try:
            resp = esconnection.recomQuery(request.json)
        except Exception as inst:
            response = jsonify({"error": "unable to connect to OMS ESCore"})
            response.status_code = 500
            return response
        if type != 'format':
            response = jsonify(resp)
        else:
            response = jsonify(offer_format(resp))
        response.status_code = 200
        return response


@oms.route('/crawler')
class CrawlerInfo(Resource):
    def get(self):
        '''Get general Crawler information'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Crawler Info"


@oms.route('/crawler/status')
class CrawlerStatus(Resource):
    def get(self):
        '''Get Crawler status'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Crawler Status"


@oms.route('/crawler/schedule')
class CrawlerSchedule(Resource):
    def get(self):
        '''Get Crawler schedule'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Schedule"

    def put(self):
        '''Change Crawler schedule'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "New schedule"


@oms.route('/crawler/seed')
class CrawlerSeed(Resource):
    def get(self):
        '''Get Crawler seed'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Current seed"

    def put(self):
        '''Modify Crawler seed'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "New seed"


@oms.route('/crawler/start')
class CrawlerStart(Resource):
    def post(self):
        '''Start Crawler'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Start Crawling"


@oms.route('/crawler/stop')
class CrawlerStop(Resource):
    def post(self):
        '''Stop Crawler'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "stop Crawler"


@oms.route('/ontology')
class Ontology(Resource):
    def get(self):
        '''Returns current working ontology'''
        ontology = os.path.join(ontology_dir, "Generated_7(sample).owl")
        # return ontology_dir
        with open(ontology) as f:
            onto = f.read()
        return Response(onto, mimetype='application/rdf+xml')
        # return "Current ontology"


@oms.route('/ontology/list')
class OntologyList(Resource):
    def get(self):
        '''Returns list of available ontology versions'''
        response = jsonify({"warrning": "not allowed"})
        response.status_code = 403
        return response
        # return "Ontology List"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)