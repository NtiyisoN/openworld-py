'''
Created on Dec 12, 2012

@author: zserre
'''
import openworld

def test():
    owc = openworld.OWClient()

    dtList = owc.getDataTypes()  
    for dt in dtList:
        print '-----------------'
        print 'creator: ' + dt.creator
        print 'isPublic: ' + dt.isPublic
        print 'dataName: ' + dt.dataName
        print 'key: ' + dt.key
        print 'privateApplicationList: ' + dt.privateApplicationList
        print 'externalServer: ' + dt.externalServer
            
    return

if __name__=="__main__":
    test()
