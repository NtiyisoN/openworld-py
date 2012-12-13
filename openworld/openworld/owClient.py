'''
Created on Dec 12, 2012

@author: zserre
'''
import httplib
import urllib
import urllib2
import json

class OWDataType:
    
    def __init__(self, d):
        self.creator = d['creator']
        self.isPublic = d['isPublic']
        self.dataName = d['dataName']
        self.key = d['key']
        self.privateApplicationList = d['privateApplicationList']
        self.externalServer = d['externalServer']
              
        
class OWClient:
    '''
    Client for connecting to a OpenWorld Server
    '''
    
    # mDataTypeKey,mCreatorKey,mTitle,mSubtitle

    def __init__(self):
        self.url = 'http://openworldserver.appspot.com'
        self.port = 80
        
    def serverRequest(self, page, data={}, body=""):
        #print json.dumps(dpDict)
        
        params = urllib.urlencode(data)
        if data != {}: params = '?' + params
        req = urllib2.Request(self.url + "/" + page + params, body , {'Content-Type': 'application/x-www-form-urlencoded'})
           
        try:
            fd = urllib2.urlopen(req)
            response = fd.read()          
            fd.close()
            return response
        except Exception, e:
            print e
        
        return ""
    
    def getDataTypes(self):
        '''
            API: getDataTypes - Returns a list of OWDataType objects
        '''
        
        json_resp = json.loads(self.serverRequest('getDataTypes'))
        rlist = []
        for o in json_resp:
            rlist.append(OWDataType(o))
        return rlist
       
        