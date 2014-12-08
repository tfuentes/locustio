def CheckContent(response,Sstring):
        if response.content.find(Sstring) != -1:
                response.success()
                print "success para string " + Sstring
        else:
                response.failure("String " + Sstring + " not found")
                print "fail"
