'''
Created on 12. sept 2017

@author: Peeter Meos
'''

import collections

from ibapi.client import EClient
from ibapi import wrapper


class Client(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)
        # ! [socket_declare]

        # how many times a method is called to see test coverage
        self.clntMeth2callCount = collections.defaultdict(int)
        self.clntMeth2reqIdIdx = collections.defaultdict(lambda: -1)
        self.reqId2nReq = collections.defaultdict(int)
        self.setupDetectReqId()
        
# ! [ewrapperimpl]
class Wrapper(wrapper.EWrapper):
    # ! [ewrapperimpl]
    def __init__(self):
        wrapper.EWrapper.__init__(self)

        self.wrapMeth2callCount = collections.defaultdict(int)
        self.wrapMeth2reqIdIdx = collections.defaultdict(lambda: -1)
        self.reqId2nAns = collections.defaultdict(int)
        self.setupDetectWrapperReqId()

class Trader(Wrapper, Client):
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self, wrapper=self)
        # ! [socket_init]
        self.nKeybInt = 0
        self.started = False
        self.nextValidOrderId = None
        self.permId2ord = {}
        self.reqId2nErr = collections.defaultdict(int)
        self.globalCancelOnly = False
        self.simplePlaceOid = None   
        
    def dumpTestCoverageSituation(self):
        for clntMeth in sorted(self.clntMeth2callCount.keys()):
            pass
            # logging.debug("ClntMeth: %-30s %6d" % (clntMeth,
            # self.clntMeth2callCount[clntMeth]))

        for wrapMeth in sorted(self.wrapMeth2callCount.keys()):
            pass
            # logging.debug("WrapMeth: %-30s %6d" % (wrapMeth,
            # self.wrapMeth2callCount[wrapMeth]))

    def dumpReqAnsErrSituation(self):
    # logging.debug("%s\t%s\t%s\t%s" % ("ReqId", "#Req", "#Ans", "#Err"))
        for reqId in sorted(self.reqId2nReq.keys()):
            nReq = self.reqId2nReq.get(reqId, 0)
            nAns = self.reqId2nAns.get(reqId, 0)
            nErr = self.reqId2nErr.get(reqId, 0)
            # logging.debug("%d\t%d\t%s\t%d" % (reqId, nReq, nAns, nErr)) 
            
            
    @iswrapper
    # ! [connectack]
    def connectAck(self):
        if self.async:
            self.startApi()

    # ! [connectack]

    @iswrapper
    # ! [nextvalidid]
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        # logging.debug("setting nextValidOrderId: %d", orderId)
        self.nextValidOrderId = orderId
        # ! [nextvalidid]

        # we can start now
        self.start()
        
    def start(self):
        if self.started:
            return

        self.started = True

        if self.globalCancelOnly:
            print("Executing GlobalCancel only")
            self.reqGlobalCancel()
        else:
            print("Executing requests")
            self.reqGlobalCancel()
            self.marketDataType_req()
            self.accountOperations_req()
            self.tickDataOperations_req()
            self.marketDepthOperations_req()
            self.realTimeBars_req()
            self.historicalDataRequests_req()
            self.optionsOperations_req()
            self.marketScanners_req()
            self.reutersFundamentals_req()
            self.bulletins_req()
            self.contractOperations_req()
            self.contractNewsFeed_req()
            self.miscelaneous_req()
            self.linkingOperations()
            self.financialAdvisorOperations()
            self.orderOperations_req()
            print("Executing requests ... finished")