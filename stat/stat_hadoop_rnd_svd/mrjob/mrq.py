from mrjob.job import MRJob
from mrjob.protocol import PickleProtocol, RawValueProtocol
from mrjob.protocol import RawProtocol
import numpy as np, sys
import numpy.linalg as lin

'''
Q = A*inv(R)
'''
class MRQ(MRJob):
    INTERNAL_PROTOCOL = PickleProtocol
    INPUT_PROTOCOL = RawProtocol
    
    def configure_options(self):
        super(MRQ, self).configure_options()
        self.add_passthrough_option('--R')
                
    def __init__(self, *args, **kwargs):
        super(MRQ, self).__init__(*args, **kwargs)
        self.R_inv = lin.inv(np.loadtxt(self.options.R,delimiter=';'))
        
    def mapper(self, key, line):
        line = line.replace('"','')
        line_vals = map(np.float,line.split(';'))
        mult = np.dot(line_vals,self.R_inv)
        yield (int(key),";".join(map(lambda x: str(np.round(x,3)),mult) ))
        
if __name__ == '__main__':
    MRQ.run()
