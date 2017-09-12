'''
TWS API extension to fit Sigma needs

Created on 12. sept 2017

@author: Peeter Meos
@version: 0.1
'''

from ibapi import wrapper
from ibapi.client import EClient
from ibapi.client import TickerId
from ibapi.contract import Contract
from ibapi.utils import iswrapper
from sigma.utils.logger import Logger

class Client(EClient):
    def __init__(self, wrapper):
        EClient.__init__(self, wrapper)

        
class Wrapper(wrapper.EWrapper):
    pass
        
    
class Trader(Wrapper, Client):
    def __init__(self):
        Wrapper.__init__(self)
        Client.__init__(self, wrapper=self)
        self.nKeybInt = 0
        self.started = False
        self.nextValidOrderId = None
        self.logger = Logger()
            
    @iswrapper
    def connectAck(self):
        if self.async:
            self.startApi()

    @iswrapper
    def nextValidId(self, orderId: int):
        #super().nextValidId(orderId)

        print("setting nextValidOrderId: %d" % (orderId))
        self.nextValidOrderId = orderId
        self.start()
    
    def start(self):
        if self.started:
            return

        self.started = True
    
    @iswrapper
    def managedAccounts(self, accountsList: str):
        #super().managedAccounts(accountsList)
        print('Managed accounts: %s' % (accountsList))
        
    @iswrapper
    def updateAccountValue(self, key: str, val: str, currency: str, accountName: str):
        #super().updateAccountValue(key, val, currency, accountName)
        print("UpdateAccountValue. Key:", key, "Value:", val,
              "Currency:", currency, "AccountName:", accountName)
        
    @iswrapper    
    def updatePortfolio(self, contract: Contract, position: float,
                        marketPrice: float, marketValue: float,
                        averageCost: float, unrealizedPNL: float,
                        realizedPNL: float, accountName: str):
        #super().updatePortfolio(contract, position, marketPrice, marketValue,
        #                        averageCost, unrealizedPNL, realizedPNL, accountName)
        print("UpdatePortfolio.", contract.symbol, "", contract.secType, "@",
              contract.exchange, "Position:", position, "MarketPrice:", marketPrice,
              "MarketValue:", marketValue, "AverageCost:", averageCost,
              "UnrealizedPNL:", unrealizedPNL, "RealizedPNL:", realizedPNL,
              "AccountName:", accountName)
    
    @iswrapper
    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        #super().accountSummary(self, reqId, account, tag, value, currency)
        print("Acct Summary. ReqId:", reqId, "Acct:", account,
              "Tag: ", tag, "Value:", value, "Currency:", currency)
    
    @iswrapper
    def updateAccountTime(self, timeStamp: str):
        #super().updateAccountTime(timeStamp)
        print("UpdateAccountTime. Time:", timeStamp)
    
    @iswrapper    
    def currentTime(self, time: int):
        #super().currentTime(self, time)
        print("Current time is: ", time)
        
    @iswrapper
    def error(self, reqId: TickerId, errorCode:int, errorString:str):
        #super().error(reqId, errorCode, errorString)
        print(str)
        
    @iswrapper
    def winError(self, text: str, lastError: int):
        super().winError(text, lastError)
        