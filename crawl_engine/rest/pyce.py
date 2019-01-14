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
from ontology_engine.ontology_engine import OntologyEngine
from providers.provider_crawl import ProviderCrawl
from postprocessing.offer_formatter import offer_format
import multiprocessing
from crontab import CronTab
import time
import os
import json
from rest.async_crawl import async_crawl
from utils.utils import checkPID
import signal

app = Flask(__name__)
api = Api(app, version='0.0.1', title='Offer Management System',
    description='Maneuver - Offer Management System  REST API',
)

trusted_proxies = ('127.0.0.1')
cProcessList = []
global cProcessList

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

scheduler_model = api.model('Crawl scheduler', {
    "min": fields.Integer(required=False, default=0, description="Minutes"),
    "hour": fields.Integer(required=False, default=1, description="Hours"),
    "day": fields.Integer(required=False, default=1, description="Days")
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
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            escore = ESCore(esendpoint)
            escore.createIndex(index)
            resp = jsonify({"message": "created index {}".format(index)})
            resp.status_code = 201
            return resp
        # return "Index {}".format(index)

    def delete(self, index):
        '''Delete ES index'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            escore = ESCore(esendpoint)
            escore.deleteIndex(index)
            resp = jsonify({"message": "deleted index {}".format(index)})
            resp.status_code = 200
            return resp
        # return "Delete index {}".format(index)

    def post(self, index):
        '''Open ES Index'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            escore = ESCore(esendpoint)
            escore.openIndex(index)
            resp = jsonify({"message": "opened index {}".format(index)})
            resp.status_code = 200
            return resp
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
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            response = jsonify({"warrning": "not allowed"})
            response.status_code = 403
            return response
            # return "Crawler Info"


@oms.route('/crawler/status')
class CrawlerStatus(Resource):
    def get(self):
        '''Get Crawler status'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            alive = []
            for proc in cProcessList:
                procDetail = {}
                if proc['process'].is_alive():
                    procDetail['Start'] = proc['start']
                    procDetail['WorkerID'] = proc['pid']
                    alive.append(procDetail)
            response = jsonify(alive)
            response.status_code = 200
            return response


@oms.route('/crawler/schedule')
class CrawlerSchedule(Resource):
    def get(self):
        '''Get Crawler schedule'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        if not os.path.isfile('../../data/scheduel.json'):
            resp = jsonify({'message': 'no scheduel set'})
            resp.status_code = 404
            return resp
        sch = json.load(open('../../data/scheduel.json'))
        response = jsonify(sch)
        response.status_code = 200
        return response

    @api.expect(scheduler_model)
    def put(self):
        '''Change Crawler schedule'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        file_cron = CronTab(tabfile='../../data/oms.tab')
        job = file_cron.new(command='python async_crawl.py')
        if request.json['min']:
            job.min.every(request.json['min'])
        elif request.json['hour']:
            job.hour.every(request.json['hour'])
        elif request.json['day']:
            job.day.every(request.json['day'])
        with open('../../data/scheduel.json', 'w') as fp:
            json.dump(request.json, fp)
        response = jsonify({"scheduel": request.json})
        response.status_code = 201
        return response
        # return "New schedule"


@oms.route('/crawler/seed')
class CrawlerSeed(Resource):
    def get(self):
        '''Get Crawler seed'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            if not os.path.isfile("../../data/seed.json"):
                resp = jsonify({"message": "seed not set"})
                resp.status_code = 404
                return resp
            data = json.load(open('../../data/crawled_aws.json'))
            return Response(data, mimetype='application/json')

    def put(self):
        '''Modify Crawler seed'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            with open('../../data/seed.json', 'w') as fp:
                json.dump(request.json, fp)
            resp = jsonify({"message": "saved new seed",
                            "seed": request.json})
            resp.status_code = 201
            return resp


@oms.route('/crawler/start')
class CrawlerStart(Resource):
    def post(self):
        '''Start Crawler'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            if not os.path.isfile("../../data/seed.json"):
                resp = jsonify({"message": "seed not provided"})
                resp.status_code = 404
                return resp
            seed = json.load(open('../../data/seed.json'))
            crawl = ProviderCrawl(seed=seed, esendpoint=esendpoint)
            carwled = crawl.crawl()
            if not carwled:
                resp = jsonify({"error": "could finish crawling "})
                resp.status_code = 500
                return resp

            try:
                ontology = OntologyEngine()
                ontology.load_ontology()
                data = json.load(open('../../data/crawled_aws.json'))
                ontology.sync(data, 'amazon')

                data2 = json.load(open('../../data/crawled_goo.json'))
                ontology.sync(data2, 'google')
            except Exception as inst:
                resp = jsonify({"message": "failed to populate ontology",
                                "type": type(inst),
                                "args": inst.args})
                resp.status_code = 500
                return resp
            response = jsonify({"message": "success"})
            response.status_code = 200
            return response
        # return "Start Crawling"


@oms.route('/crawler/start/async')
class CrawlerStartAsync(Resource):
    def post(self):
        '''Start Crawler'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            for proc in cProcessList:
                try:
                    if not proc['process'].is_alive():
                        cProcessList.remove(proc)
                        print('Process with PID %s inactive, removed from process list!', proc['pid'])
                except Exception as inst:
                    print('Checking process failed with %s and %s', type(inst), str(inst.args))
            aworkers = 1
            if len(cProcessList) > aworkers:
                print('Maximum number (%s) of query workers exeeded!', str(aworkers))
                message = 'Maximum number of query workers %s' % str(aworkers)
                response = jsonify({'Status': 'To many query workers', 'Message': message})
                response.status_code = 429
                return response
            backProc = multiprocessing.Process(target=async_crawl, args=(esendpoint,))
            backProc.daemon = True
            backProc.start()
            start_time = time.time()
            # fuuid = fname.split('.')[0]
            # tuuid = fname.split('.')[1]
            procdist = {'process': backProc, 'pid': backProc.pid, 'start': start_time}
            if not checkPID(backProc.pid):
                response = jsonify({'Status': 'Worker Fail', 'Message': 'Failed to start crawl worker'})
                response.status_code = 500
                return response
            cProcessList.append(procdist)
            response = jsonify({'WorkerID': backProc.pid, 'Start': start_time})
            response.status_code = 201
            return response


@oms.route('/crawler/stop')
class CrawlerStop(Resource):
    def post(self):
        '''Stop Crawler'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            for proc in cProcessList:
                try:
                    try:
                        if not proc['process'].is_alive():
                            cProcessList.remove(proc)
                            print('Process with PID %s inactive, removed from process list!', proc['pid'])
                    except Exception as inst:
                        print('Checking process failed with %s and %s', type(inst), str(inst.args))
                    os.kill(proc['pid'], signal.SIGTERM)
                except Exception as inst:
                    resp = jsonify({"message": "cloudnt stop crawler",
                                    "type": type(inst),
                                    "args": inst.args})
                    resp.status_code = 500
                    return resp
        resp = jsonify({'processes': cProcessList})
        resp.status_code = 200
        return resp


@oms.route('/ontology')
class Ontology(Resource):
    def get(self):
        '''Returns current working ontology'''
        onto_name = "Generated_7(sample).owl"
        if os.path.isfile("../../data/{}".format(onto_name)):
            ontology = os.path.join(ontology_dir, "Generated_7(sample).owl")
            # return ontology_dir
            with open(ontology) as f:
                onto = f.read()
            return Response(onto, mimetype='application/rdf+xml')
        else:
            resp = jsonify({"message": "ontology not generated"})
            resp.status_code = 404
            return resp
        # return "Current ontology"


@oms.route('/ontology/list')
class OntologyList(Resource):
    def get(self):
        '''Returns list of available ontology versions'''
        if request.remote_addr not in trusted_proxies:
            response = jsonify({"warrning": "not allowed",
                                "remote": request.remote_addr})
            response.status_code = 403
            return response
        else:
            response = jsonify({"warrning": "not allowed"})
            response.status_code = 403
            return response
        # return "Ontology List"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)