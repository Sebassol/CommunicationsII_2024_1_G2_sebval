import numpy as np
from gnuradio import gr
import math

class blk(gr.sync_block):  
    """This block is a CE VCO or baseband VCO and works as following: ….."""

    def __init__(self,):  
        gr.sync_block.__init__(
            self,
            name='VCO_CMLP',   
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )
        
    def work(self, input_items, output_items):
        Q=input_items[0]
        A=input_items[1]
        y=output_items[0]
        N=len(A)
        y[:]=A*np.exp(1j*Q)
        return len(y)
