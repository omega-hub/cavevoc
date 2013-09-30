## @package cavevoc
# CAVE Python speech recognition module.
# This Python script receives incoming speech commands from a separate CAVEVOC client running on a separate
# computer.
# The CAVEVOC client is written in Processing and is based on the STT library found here: http://stt.getflourish.com/
# CAVEVOC client takes audio in and sends it to Google for processing. Google returns with the text and confidence level.
# CAVEVOC then sends the text to the CAVEVOC Python Module.
#
# This module contains only static members and member functions so you do not need to create any objects of this class to use it.
# To import the module into your own program:
#
# from cavevoc import cavevoc
#
# To initialize call:
#	cavevoc.init("CallbackFunctionName", receivePort)
#	CallbackFunctionName is the name of your callback function.
#	receivePort is the network port that cavevoc should listen on. This is an optional paratmeter.
#	The default port is 5005.
#
#	CallbackFunctionName should consist of only 2 input parameters of type String and float
#	to receive the incoming translated string from the speech recognition system and its confidence level.
#	Confidence ranges from 0 to 1
#	e.g. CallbackFunctionName(confidence,incomingString):
#
# Lastly use CAVEVOC in your onUpdate function as follows:
#	cavevoc.update()
#
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Original Version 7/20/2013

from math import *
from euclid import *
from omega import *
from cyclops import *
import socket
import errno

## cavevoc class
# Insert comment here about Cavevoc class
class cavevoc:
	__DEFAULT_LISTENING_PORT = 5005
	__sock = None
	__incomingPort = __DEFAULT_LISTENING_PORT
	__funcName = None
	
	@staticmethod
	## Initialize cavevoc
	# @param funcName - name of your callback function (as a String). Callback function should receive 2 parameters, a float for the confidence level, and the incoming recognized text string.
	# @param receivePort - optional parameter to specify the network port (as an integer) to listen on for incoming messages. Default is port 5005.
	def init(funcName,receivePort = __DEFAULT_LISTENING_PORT):
		cavevoc.__funcName = funcName
		cavevoc.__incomingPort = receivePort
		print "CAVEVOC: "+ str(cavevoc.__funcName) + " LISTEN PORT:"+ str(cavevoc.__incomingPort)
		
		# You should only create a udp socket in the master node
		if (isMaster()):
			cavevoc.__sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
			cavevoc.__sock.bind(("", cavevoc.__incomingPort))
			cavevoc.__sock.setblocking(0)
			#sockinfo = socket.gethostbyname(socket.getfqdn())
			#print "HOST INFO " + sockinfo
			#print "HOST " + sock.getsockname()[0]
			
	@staticmethod
	## Update cavevoc. At each call it polls the network for incoming messages from the CAVEVOC client.
	def update():
	
		# Read data from UDP socket only on the master node
		if (isMaster()):
			try:
				data, addr = cavevoc.__sock.recvfrom(1024) # buffer size is 1024 bytes

			except socket.error, e:
				err = e.args[0]
				#if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
					#print 'No data available'
				#else:
					# a "real" error occurred
				#	print e
				#	sys.exit(1)
			else:
				# got a message, do something :)
				# Since UDP messages are only received by the master node you have to then broadcast this to
				# the other nodes.
				# Below the code creates a Python command as a string.
				# The string is broadcasted to all the slave nodes where the code command is executed.
				confid, mid, rest = data.partition(" ")
				command = cavevoc.__funcName+'('+confid+',"'+rest+'")'
				print "CAVEVOC COMMAND: " + command + "\n"
				broadcastCommand(command)