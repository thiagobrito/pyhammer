import os
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import execProg

class RunCsUnitTestStep(AbstractStep):
    """Cs UnitTest Step"""

    def __init__( self, csTestDllPath ):
        AbstractStep.__init__( self, "Cs UnitTest" )
        
        msTestPath = "C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE"
        if os.path.isdir(msTestPath) == 0:
            msTestPath = "C:\Program Files\Microsoft Visual Studio 10.0\Common7\IDE"   

        self.command = """%s\\MSTest.exe /testcontainer:%s""" % ( msTestPath, csTestDllPath )
        self.csTestDllPath = csTestDllPath

    def do( self ):
        self.reporter.message( "RUN CS UNITTEST: %s" % self.csTestDllPath )

        print(self.command)

        result = execProg( self.command, self.reporter, os.path.dirname(self.csTestDllPath) ) == 0
        return result


