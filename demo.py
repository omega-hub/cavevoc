########################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 7/4/2013
#
# Demo application to show the use of the CAVEVOC speech recognition module
# Look for comments below that say ADD THIS TO USE CAVEVOC
# to find out how to use it in your own programs.
#
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *

import random

########################################################################
# ADD THIS TO USE CAVEVOC
# The init function tells CAVEVOC to call the function MakeText whenever
# speech is translated.
from cavevoc import cavevoc
cavevoc.init("MakeText")

########################################################################
# Make a scene.

g_scene = getSceneManager()

# Create a light
g_light = Light.create()
g_light.setColor(Color("#FFFFFF"))
g_light.setAmbient(Color("#303030"))
g_light.setPosition(Vector3(-5,5,5))
g_light.setEnabled(True)



########################################################################
# Callback function called by cavevoc when text is received from the recognizer.
# This particular callback takes the confidence level and text and creates a 3DText object
# and places it in some random location in front of the CAVE.

SEED=1
random.seed(SEED)
def MakeText(confid, textstr):
	text = Text3D.create('fonts/arial.ttf',0.05,str(confid)+"\n"+textstr)
	
	# Note: the random number had to be seeded ahead of time because MakeText will get
	# called by each of the CAVE2 nodes independently and unless they have the same starting seed
	# the random positions generated will be different per node.

	randX = random.random()
	randY = random.random()
	randZ = random.random()
	
	text.setPosition(Vector3(-1+randX*2,1+randY,-2.5-randZ))
	text.setFontResolution(120)
	text.setColor(Color('white'))
	print "CONFIDENCE:"+ str(confid) + " MESG:" +  textstr


# You're going to need to have an onUpdate function in which you add the cavevoc.update call.
def onUpdate(frame, time, dt):

	########################################################################
	# ADD THIS TO USE CAVEVOC
	cavevoc.update()


# Tell Omegalib about the onUpdate function
setUpdateFunction(onUpdate)
