#!/usr/bin/env python
#-*- coding: utf-8 -*-
#!/usr/bin/python
#Thanks to Russell Borogove

import pyaudio
import struct
import math
from collections import OrderedDict
from datetime import datetime

global start_time
start_time = datetime.now()
global end_time
end_time = datetime.now()
global s1
s1=0
global s2
s2=0
global s
s= s1,s2


INITIAL_TAP_THRESHOLD = 0.010
FORMAT = pyaudio.paInt16 
SHORT_NORMALIZE = (1.0/32768.0)
CHANNELS = 2
RATE = 44100  
INPUT_BLOCK_TIME = 0.05
INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)
# if we get this many noisy blocks in a row, increase the threshold
OVERSENSITIVE = 5.0/INPUT_BLOCK_TIME                    
# if we get this many quiet blocks in a row, decrease the threshold
UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME 
# if the noise was longer than this many blocks, it's not a 'tap'
MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME

kelime=OrderedDict({})
kelime.clear()
sira={}
sira.clear()
liste=[]
global c
c=0
def get_rms( block ):
    # RMS amplitude is defined as the square root of the 
    # mean over time of the square of the amplitude.
    # so we need to convert this string of bytes into 
    # a string of 16-bit samples...

    # we will get one short out for each 
    # two chars in the string.
    global count
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    # iterate over the block.
    sum_squares = 0.0
    for sample in shorts:
        # sample is a signed short in +/- 32768. 
        # normalize it to 1.0
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )

class TapTester(object):
    def __init__(self):
        self.pa = pyaudio.PyAudio()
        self.stream = self.open_mic_stream()
        self.tap_threshold = INITIAL_TAP_THRESHOLD
        self.noisycount = MAX_TAP_BLOCKS+1 
        self.quietcount = 0 
        self.errorcount = 0
    def stop(self):
        self.stream.close()

    def find_input_device(self):
        device_index = None            
        for i in range( self.pa.get_device_count() ):     
            devinfo = self.pa.get_device_info_by_index(i)   
            print( "Device %d: %s"%(i,devinfo["name"]) )

            for keyword in ["mic","input"]:
                if keyword in devinfo["name"].lower():
                    print( "Found an input: device %d - %s"%(i,devinfo["name"]) )
                    device_index = i
                    return device_index

        if device_index == None:
            print( "No preferred input found; using default input device." )

        return device_index

    def open_mic_stream( self ):
        device_index = self.find_input_device()

        stream = self.pa.open(   format = FORMAT,
                                 channels = CHANNELS,
                                 rate = RATE,
                                 input = True,
                                 input_device_index = device_index,
                                 frames_per_buffer = INPUT_FRAMES_PER_BLOCK)

        return stream

    def tapDetected(self):
	global end_time
	end_time = datetime.now()
        print "."	
	z=1
	if self.noisycount == z:
		global c		
		c=c+1
		global k
		k="a",c		
		kelime[k]=z
		z=1
		print kelime.keys()
	else:
		global c		
		c=c+1
		global k
		k="a",c		
		kelime[k]=z
		z=1
		print kelime.keys()

	#print(format(end_time - start_time))
	global start_time
	
	if (format(end_time - start_time)) > "0:00:04.000000":
		sira[k]=z
		p=len(sira)
		if len(sira)==1:
			global s1
			s1=len(kelime)-1	
			#print s1
			print "First order"
			kelime.clear()
			start_time = datetime.now()
		if len(sira)==2:
			global s2			
			s2=len(kelime)-1			
			global s			
			s=s1,s2						
			#print "bu ikinci sıra"			
			print "This is the letter: ",s
			sira.clear()
			kelime.clear()
			start_time = datetime.now()
#Buradan başlıyor alfabe
		if s==(1, 1):
			liste.append("a")
			print liste
			s=0
		if s==(1, 2):
			liste.append("b")
			print liste
			s=0
		if s==(1, 3):
			liste.append("c")
			print liste
			s=0
		if s==(1, 4):
			liste.append("ç")
			print liste
			s=0
		if s==(1, 5):
			liste.append("d")
			print liste
			s=0
		if s==(1, 6):
			liste.append("e")
			print liste
			s=0
		if s==(2, 1):
			liste.append("f")
			print liste
			s=0
		if s==(2, 2):
			liste.append("g")
			print liste
			s=0
		if s==(2, 3):
			liste.append("ğ")
			print liste
			s=0
		if s==(2, 4):
			liste.append("h")
			print liste
			s=0
		if s==(2, 5):
			liste.append("ı")
			print liste
			s=0
		if s==(2, 6):
			liste.append("i")
			print liste
			s=0
		if s==(3, 1):
			liste.append("j")
			print liste
			s=0
		if s==(3, 2):
			liste.append("k")
			print liste
			s=0
		if s==(3, 3):
			liste.append("l")
			print liste
			s=0
		if s==(3, 4):
			liste.append("m")
			print liste
			s=0
		if s==(3, 5):
			liste.append("n")
			print liste
			s=0
		if s==(3, 6):
			liste.append("o")
			print liste
			s=0
		if s==(4, 1):
			liste.append("ö")
			print liste
			s=0
		if s==(4, 2):
			liste.append("p")
			print liste
			s=0
		if s==(4, 3):
			liste.append("r")
			print liste
			s=0
		if s==(4, 4):
			liste.append("s")
			print liste
			s=0
		if s==(4, 5):
			liste.append("ş")
			print liste
			s=0
		if s==(4, 6):
			liste.append("t")
			print liste
			s=0
		if s==(5, 1):
			liste.append("u")
			print liste
			s=0
		if s==(5, 2):
			liste.append("ü")
			print liste
			s=0
		if s==(5, 3):
			liste.append("v")
			print liste
			s=0
		if s==(5, 4):
			liste.append("y")
			print liste
			s=0
		if s==(5, 5):
			liste.append("z")
			print liste
			s=0
		if s==(5, 6):
			liste.append(" ")
			print liste
			s=0
		kelime.clear()
		
			

    def listen(self):
        try:
            block = self.stream.read(INPUT_FRAMES_PER_BLOCK)
        except IOError, e:
            # dammit. 
            self.errorcount += 1
            print( "(%d) Error recording: %s"%(self.errorcount,e) )
            self.noisycount = 1
            return

        amplitude = get_rms( block )
        if amplitude > self.tap_threshold:
            # noisy block
            self.quietcount = 0
            self.noisycount += 1
            if self.noisycount > OVERSENSITIVE:
                # turn down the sensitivity
                self.tap_threshold *= 1.1
        else:            
            # quiet block.

            if 1 <= self.noisycount <= MAX_TAP_BLOCKS:
                self.tapDetected()
            self.noisycount = 0
            self.quietcount += 1
            if self.quietcount > UNDERSENSITIVE:
                # turn up the sensitivity
                self.tap_threshold *= 0.9

if __name__ == "__main__":
    tt = TapTester()

    for i in range(1000):
        tt.listen()
	
