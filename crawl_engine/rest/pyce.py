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

app = Flask(__name__)
api = Api(app, version='0.0.1', title='Offer Management System',
    description='Maneuver - Offer Management System  REST API',
)

oms = api.namespace('OMS', description='OMS operations')

todo = api.model('Todo', {
    'id': fields.Integer(readOnly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})


queryES = api.model('query details Model', {
    'fname': fields.String(required=False, default="output", description='Name of output file.'),
    'size': fields.Integer(required=True, default=500, description='Number of record'),
    'ordering': fields.String(required=True, default='desc', description='Ordering of records'),
    'queryString': fields.String(required=True, default="host:\"dice.cdh5.s4.internal\" AND serviceType:\"dfs\""
                                 , description='ElasticSearc Query'),
    'tstart': fields.Integer(required=True, default="now-1d", description='Start Date'),
    'tstop': fields.Integer(required=False, default="None", description='Stop Date'),
    'metrics': fields.List(fields.String(required=False, default=' ', description='Desired Metrics')),
    'index': fields.String(required=False, default='logstash-*', description='Name of ES Core index')
})

# Elasticsearch endpoint
esendpoint = '194.102.63.78'


@oms.route('/escore')
class ESCoreVersion(Resource):
    '''Shows a list of all todos, and lets you POST to add new tasks'''
    # @oms.doc('list_todos')
    # @oms.marshal_list_with(todo)
    def get(self):
        '''List all tasks'''
        return "something"

    # @ns.doc('create_todo')
    # @ns.expect(todo)
    # @ns.marshal_with(todo, code=201)
    # def post(self):
    #     '''Create a new task'''
    #     return "somethingelse"


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


@oms.route('escore/index/<index>')
class ESCoreIndex(Resource):
    def get(self, index):
        return "Index {}".format(index)

    def delete(self, index):
        return "Delete index {}".format(index)

    def post(self, index):
        return "Open index {}".format(index)


@oms.route('/escore/index/<index>/settings')
class ESCoreIndexSettings(Resource):
    def get(self, index):
        return "Index settings {}".format(index)


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
    @api.expect(queryES)
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
        return "Crawler Info"


@oms.route('/crawler/status')
class CrawlerStatus(Resource):
    def get(self):
        return "Crawler Status"


@oms.route('/crawler/schedule')
class CrawlerSchedule(Resource):
    def get(self):
        return "Schedule"

    def put(self):
        return "New schedule"


@oms.route('/crawler/seed')
class CrawlerSeed(Resource):
    def get(self):
        return "Current seed"

    def put(self):
        return "New seed"


@oms.route('/crawler/start')
class CrawlerStart(Resource):
    def post(self):
        return "Start Crawling"


@oms.route('/crawler/stop')
class CrawlerStop(Resource):
    def post(self):
        return "stop Crawler"


@oms.route('/ontology')
class Ontology(Resource):
    def get(self):
        '''Returns current working ontology'''
        return "Current ontology"


@oms.route('/ontology/list')
class OntologyList(Resource):
    def get(self):
        '''Returns list of available ontology versions'''
        return "Ontology List"


if __name__ == '__main__':
    app.run(debug=True)