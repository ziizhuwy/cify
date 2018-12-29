#__*__coding:utf-8__*__
#########################################################
# (C)  zii .All rights Reserved#
#########################################################
import time
from common.log.log_util import LogUtil as log
logger = log.getLogger(__name__)
class Spider(object):

    def __init__(self):
        self.s_id = -1
        self._url = None
        self.starttime=time.time()
        pass

    def _run(self, host):
        raise Exception('unimplemented method')

    def run(self, system):
        self._run(system)
        endtime=time.time()
        logger.error('totally used time:%s', str(endtime-self.starttime))
        self.report()


    def filter(self, resp):
        raise Exception('unimplemented method')

    def report(self):
        raise Exception('unimplemented method')