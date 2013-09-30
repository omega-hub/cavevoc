#####################################################################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 7/25/2013
#
# Demo application to show the use of the CAVEVOC speech recognition module
# Look for comments below that say ADD THIS TO USE CAVEVOC
# to find out how to use it in your own programs.
#
# This particular demo also shows how to use the PyParsing library to more cleanly parse the incoming speech commands.
#
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *
from pyparsing import *

import random

#####################################################################################################################
# ADD THIS TO USE CAVEVOC
# The init function tells CAVEVOC to call the function ParseVoiceCommand whenever
# speech is translated.
from cavevoc import cavevoc
cavevoc.init("ParseVoiceCommand")

g_recogTextNode = None

def ShowRecogText(confid,textstr):
	global g_recogTextNode
	text = Text3D.create('neuropol.ttf',0.05,str(confid)+"\n"+textstr)
	min=text.getBoundMinimum()
	max=text.getBoundMaximum()
	size = max-min
		
	text.setPosition(getDefaultCamera().getHeadOffset() + Vector3(-size.x/2.0,-0.5+size.y/2,-2))
	text.setFontResolution(120)
	text.setColor(Color('white'))
	if (g_recogTextNode != None):
		getDefaultCamera().removeChildByRef(g_recogTextNode)
	getDefaultCamera().addChild(text)
	g_recogTextNode = text
	
#####################################################################################################################
# Make a scene.

g_scene = getSceneManager()

# Create a light
g_light = Light.create()
g_light.setColor(Color("#FFFFFF"))
g_light.setAmbient(Color("#303030"))
g_light.setPosition(Vector3(-5,5,5))
g_light.setEnabled(True)

# headlight
g_headlight = Light.create()
g_headlight.setColor(Color("white"))
g_headlight.setEnabled(True)
getDefaultCamera().addChild(g_headlight)

g_mainScene = SceneNode.create("MainScene")

ShowRecogText(0,"Welcome to IDEATION")

def f2m(feet):
	return feet*0.305
	
def PutInFrontOfMe(camera, object):
	object.setPosition(camera.localToWorldPosition(camera.getHeadOffset() + Vector3(0,0,-1)))

def MakeCube(x,y,z):
	print "MAKING CUBE"
	global g_mainScene
	
	cube = BoxShape.create(x,y,z)

	cube.setEffect('colored')
	cube.getMaterial().setColor(Color(0.3,0.3,0.3,1),Color(0,0,0,1))
	cube.setSelectable(True)
	PutInFrontOfMe(getDefaultCamera(), cube)
	g_mainScene.addChild(cube)
	return cube

def MakeSphere(size):
	global g_mainScene
	sphere = SphereShape.create(size/2,8)
	sphere.setEffect('colored')
	sphere.getMaterial().setColor(Color(0.3,0.3,0.3,1),Color(0,0,0,1))
	sphere.setSelectable(True)
	PutInFrontOfMe(getDefaultCamera(), sphere)
	g_mainScene.addChild(sphere)
	return sphere

g_ptrSphere = MakeSphere(0.05)
g_ptrSphere.setSelectable(False)

g_lastCommand = ""
g_lastObject = None
g_textstr = ""


#####################################################################################################################
# Callback functions that are called when text is successfully parsed by PyParsing. These calls are what actually
# translate the correctly parsed phrases into program action- like creating a cube, painting it red, etc.
def BuildAction(tokens):
	global g_lastCommand
	global g_lastObject
	print ("BUILD ACTION: ", tokens)
	if (tokens[1] == "CUBE"):
		g_lastObject= MakeCube(f2m(1), f2m(1), f2m(1))
	
	if (tokens[1] == "SPHERE"):
		g_lastObject = MakeSphere(f2m(1))
	g_lastCommand = g_textstr

def SetColorAction(tokens):
	global g_lastCommand
	global g_lastObject
	print ("SET COLOR ACTION: ", tokens)
	if (g_lastObject != None):
		g_lastObject.getMaterial().setColor(Color(tokens[1]),Color(0.2,0.2,0.2,1))
		g_lastCommand = g_textstr
		
def SetNameAction(tokens):
	global g_lastCommand
	global g_lastObject
	print ("SET NAME ACTION: ", tokens)
	if (g_lastObject != None):
			g_lastObject.setName(tokens[1])
			

def PositionAction(tokens):
	global g_lastCommand
	global g_lastObject
	print ("SET POSITION ACTION: ", tokens)
	g_lastObject = g_mainScene.getChildByName(tokens[1])
	if g_lastObject != None:
		g_lastCommand = g_textstr
		PutInFrontOfMe(getDefaultCamera(),g_lastObject)

g_againFlag = False
def RepeatAction(tokens):
	global g_lastCommand
	global g_lastObject
	global g_againFlag
	ParseVoiceCommand(1,g_lastCommand)

#####################################################################################################################
# The Grammar

# individualObjectGram ::= BOX | CUBE | SPHERE | BALL       <-- BOX is replaced with CUBE; BALL is replaced with SPHERE on parsing
individualObjectsGram = (Literal("BOX").setParseAction(replaceWith("CUBE")) | Literal("CUBE") | Literal("SPHERE") | Literal("BALL").setParseAction(replaceWith("SPHERE")))

# buildObjectGram ::= MAKE | BUILD | CREATE + A + individualObjectGram	<-- MAKE and CREATE are converted to BUILD. Suppress() is used to suppress token generation for "A"
buildObjectGram = (Literal("MAKE").setParseAction(replaceWith("BUILD")) | Literal("BUILD") | Literal("CREATE").setParseAction(replaceWith("BUILD")))  +  Suppress(Literal("A")) + individualObjectsGram

# colorGram ::= RED | GREEN | BLUE | YELLOW | BLACK | ORANGE | WHITE | NAVY | MAGENTA etc.....
colorGram = Literal("RED") | Literal("GREEN") | Literal("BLUE") | Literal("ORANGE") | Literal("BLACK") | Literal("WHITE") | Literal("NAVY") | Literal("CYAN") | Literal("MAGENTA") | Literal("YELLOW") | Literal("PINK") | Literal("PURPLE")

# setColorGram ::= MAKE | COLOR | PAINT  + IT | THIS + colorGram  <-- MAKE and PAINT are converted to COLOR. E.g. COLOR IT RED

setColorGram = (Literal("MAKE").setParseAction(replaceWith("COLOR")) | Literal("PAINT").setParseAction(replaceWith("COLOR")) | Literal("COLOR"))  + Optional(Suppress(Literal("IT") | Literal("THIS") | Literal("IS"))) + colorGram

# aNameGram is just a Word consisting of alphabet characters
aNameGram = Word(alphas)

# setNameGram ::= NAME | CALL + IT | THIS + aNameGram  <-- NAME IT FRED is an example. The "IT" is ignored. 
setNameGram = (Literal("NAME") | Literal("CALL").setParseAction(replaceWith("NAME"))) + Optional(Suppress(Literal("IT") | Literal("THIS"))) + aNameGram

# positionObjectGram ::= POSITION | PLACE | PUT | BRING | MOVE | GET + Word
positionObjectGram = (Literal("POSITION") | Literal("PLACE").setParseAction(replaceWith("POSITION")) | Literal("PUT").setParseAction(replaceWith("POSITION")) | Literal("BRING").setParseAction(replaceWith("POSITION")) | Literal("MOVE").setParseAction(replaceWith("POSITION")) | Literal("GET").setParseAction(replaceWith("POSITION"))) + aNameGram + Suppress(ZeroOrMore(Word(alphas)))

repeatGram = Literal("AGAIN") | Literal("REPEAT")

# This is essentially one command. The setParseAction tells PyParsing to call the respective functions when the text is successfully parsed.
individualCommandsGram = buildObjectGram.setParseAction(BuildAction) | setColorGram.setParseAction(SetColorAction) | setNameGram.setParseAction(SetNameAction) | positionObjectGram.setParseAction(PositionAction) | repeatGram.setParseAction(RepeatAction)

# This implements the "AND" operator. So you can chain commands together like: MAKE A BOX AND COLOR IT RED AND MOVE IT HERE
# CommandGram is essentially the ROOT NODE of the grammar.
commandGram  = Forward()
commandGram << individualCommandsGram + Optional(Literal("AND") + commandGram)

#####################################################################################################################
# This function is called by CAVEVOC when it receives incoming text from the CAVEVOC client.
# This function takes the text string and gives it to the PyParsing grammar to parse.
def ParseVoiceCommand(confid, textstr):
	global g_lastCommand
	global g_lastObject
	global g_againFlag
	global g_textstr
	
	g_textstr=textstr
	
	print "CONFIDENCE:"+ str(confid) + " MESG:" +  textstr
	ShowRecogText(confid,textstr)
	
	try:
		commandGram.parseString(textstr.upper())
	except ParseException:
		ShowRecogText (0,"I DON'T UNDERSTAND " + textstr)
	print



#####################################################################################################################
# This code computes the closest intersecting object to the fired ray.		
g_minDistance = 999999
g_closestObject = None
g_previousObject = None
def RayIntersectionCallback(node, distance):
	global g_minDistance
	global g_closestObject 
	# save away the closest object you have intersected with
	if (node != None):
		if (distance < g_minDistance):
			g_minDistance = distance
			g_closestObject = node
			
#####################################################################################################################
# You're going to need to have an onUpdate function in which you add the cavevoc.update call.
def onUpdate(frame, time, dt):

	global g_closestObject
	global g_minDistance
	global g_lastObject
	global g_previousObject
	
	########################################################################
	# ADD THIS TO USE CAVEVOC
	cavevoc.update()
	
	########################################################################
	# The following code creates a head pointer as an intersection ray.
	# So when you talk about objects like: PAINT IT GREEN, the IT refers to the object
	# that your head ray is pointing at.
	# The current selected object gets its bounding box turned on to show that it is selected.
	
	camera = getDefaultCamera()
	camPosition = camera.getPosition()
	headOffset = camera.getHeadOffset()
	headPositionWorld = camera.localToWorldPosition(headOffset)

	g_minDistance = 999999
	theray = camera.getOrientation() * camera.getHeadOrientation() * Vector3(0,0,-1)

	g_closestObject = None
	querySceneRay(headPositionWorld,  theray, RayIntersectionCallback)
	global g_ptrSphere
	g_ptrSphere.setPosition(headPositionWorld+theray)

	
	if g_closestObject != None:
		if g_previousObject != None:
			g_previousObject.setBoundingBoxVisible(False)
			
		g_lastObject = g_closestObject
		g_lastObject.setBoundingBoxVisible(True)
		g_previousObject = g_lastObject

setUpdateFunction(onUpdate)