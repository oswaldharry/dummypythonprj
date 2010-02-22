def buildConnectionString(params):
    """builds a conn str from a dict of params 


    Returns a string """
    return ";".join(["%s=%s"% (k,v) for k,v in params.items() ])

if __name__=="__main__":
    print 'main'
    myParams={"server":"mypilgrim",
        "database":"master",
        "uid":"sa",
        "pwd":"secret"

    }
    print buildConnectionString(myParams)
    
