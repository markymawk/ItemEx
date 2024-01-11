__author__ = "Kapedani, mawwwk"
version = "1.0"
# ItemEx lib
# Conversion function and data library for updating ItemGen nodes

from BrawlCrate.API import *	# BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlCrate.UI import MainForm
from BrawlLib import * # Imaging

# ItmFreqEntryNode list, as:
# (Item ID, SubItem ID, Minimum, Maximum, Frequency)
ITEM_LIST = [
	(0x00, 5000, 1, 1, 24.0),	# Assist Trophy
	(0x03, 6, 1, 1, 27.0),		# Barrel
	(0x03, 12, 1, 1, 4.0),		# Barrel
	(0x03, 18, 1, 1, 4.0),		# Barrel
	(0x07, 6, 1, 1, 40.0),		# Crate
	(0x07, 12, 1, 1, 5.0),		# Crate
	(0x07, 18, 1, 1, 5.0),		# Crate
	(0x09, 6, 1, 1, 135.0),		# Capsule
	(0x09, 18, 1, 1, 15.0),		# Capsule
	(0x0A, 6, 1, 1, 8.0),		# Rolling Crate
	(0x0A, 12, 1, 1, 1.0),		# Rolling Crate
	(0x0A, 18, 1, 1, 1.0),		# Rolling Crate
	(0x22, 6, 1, 1, 25.0),		# Party Ball
	(0x22, 12, 1, 1, 3.0),		# Party Ball
	(0x22, 18, 1, 1, 3.0),		# Party Ball
	(0x2a, 5000, 1, 1, 50.0),	# Pokeball
	(0x31, 5000, 1, 1, 7.0),	# Sandbag
	(0x20, 5000, 1, 1, 3.0),	# Heart Container
	(0x24, 5000, 1, 1, 7.0),	# Maxim Tomato
	(0x40, 5000, 1, 1, 24.0),	# Food
	(0x10, 5000, 1, 1, 6.0),	# Superspicy Curry
	(0x27, 5000, 1, 1, 6.0),	# Metal Box
	(0x25, 5000, 1, 1, 5.0),	# Poison Mushroom
	(0x26, 5000, 1, 1, 9.0),	# Super Mushroom
	(0x35, 5000, 1, 1, 8.0),	# Timer
	(0x3f, 5000, 1, 1, 7.0),	# Star
	(0x42, 5000, 1, 1, 6.0),	# Lightning
	(0x45, 5000, 1, 1, 15.0),	# Warpstar
	(0x0d, 5000, 1, 1, 12.0),	# Cracker Launcher
	(0x18, 5000, 1, 1, 12.0),	# Fire Flower
	(0x2c, 5000, 1, 1, 14.0),	# Ray Gun
	(0x3d, 5000, 1, 1, 17.0),	# Super Scope
	(0x04, 5000, 1, 1, 15.0),	# Beam Sword
	(0x1b, 5000, 1, 1, 2.0),	# Golden Hammer
	(0x1d, 5000, 1, 1, 9.0),	# Hammer
	(0x1f, 5000, 1, 1, 15.0),	# Fan
	(0x21, 5000, 1, 1, 5.0),	# Homerun Bat
	(0x2e, 5000, 1, 1, 9.0),	# Lip's Stick
	(0x3a, 5000, 1, 1, 8.0),	# Star Rod
	(0x02, 5000, 1, 1, 14.0),	# Banana Peel
	(0x06, 5000, 1, 1, 20.0),	# Bob-Omb
	(0x08, 0, 1, 1, 5.0),		# Bumper
	(0x08, 8200, 1, 1, 5.0),	# Bumper
	(0x0c, 5000, 1, 1, 11.0),	# Gooey Bomb
	(0x12, 5000, 1, 1, 10.0),	# Deku Nut
	(0x13, 5000, 1, 1, 7.0),	# Mr. Saturn
	(0x1a, 5000, 1, 1, 12.0),	# Freezie
	(0x1c, 5000, 1, 1, 9.0),	# Green Shell
	(0x28, 5000, 1, 1, 8.0),	# Hothead
	(0x29, 5000, 1, 1, 14.0),	# Pitfall
	(0x34, 5000, 1, 1, 13.0),	# Motion-Sensor Bomb
	(0x36, 5000, 1, 1, 13.0),	# Smart Bomb
	(0x38, 5000, 1, 1, 13.0),	# Smoke Screen
	(0x39, 5000, 1, 1, 9.0),	# Spring
	(0x41, 5000, 1, 1, 18.0),	# Team Healer
	(0x01, 5000, 1, 1, 8.0),	# Franklin Badge
	(0x32, 0, 1, 1, 6.0),		# Screw Attack
	(0x32, 8234, 1, 1, 6.0),	# Screw Attack
	(0x44, 5000, 1, 1, 10.0),	# Bunny Hood
	(0x3c, 5000, 1, 1, 10.0),	# Soccer Ball
	(0x43, 5000, 1, 1, 8.0),	# Unira
	(0x14, 5000, 1, 1, 5.0),	# Dragoon Part
	(0x2b, 5000, 1, 1, 10.0),	# Blast Box
	(0x37, 5000, 1, 1, 150.0)	# Smash Ball
]

# Helper functions
def isCommonItem(itemId):
	return itemId < 0x46 or itemId == 0x4f or (itemId >= 0x53 and itemId < 0x62)

def isContainer(itemId):
	return itemId == 0x03 or itemId == 0x07 or itemId == 0x0A or itemId == 0x22 or itemId == 0x09

def getContainerVariation(freqNodes):
	for freqNode in freqNodes:
		if isContainer(freqNode.ItemID):
			if freqNode.SubID >= 6 and freqNode.SubID < 24:
				return freqNode.SubID % 3
			elif freqNode.SubID < 6:
				return freqNode.SubID
	return 0

# Main ItemGen update function 
def updateItmTableGroupNode(groupNode):
	if groupNode.Id == 10000:
		itmFreqEntryNodes = []
		
		# Generate list of ItemFreqEntry nodes for common (vBrawl) items
		for freqNode in groupNode.Children:
			if isCommonItem(freqNode.ItemID):
				itmFreqEntryNodes.append(freqNode)
		
		# Remove all common ItemFreqEntry nodes
		for freqNode in itmFreqEntryNodes:
			freqNode.Remove()
		
		# Create new item freq entry nodes
		for itemFreq in ITEM_LIST:
			freqNode = ItmFreqEntryNode()
			freqNode.ItemID = itemFreq[0]
			freqNode.SubID = itemFreq[1]
			freqNode.Minimum = itemFreq[2]
			freqNode.Maximum = itemFreq[3]
			freqNode.Frequency = itemFreq[4]
			groupNode.AddChild(freqNode)
			
			# Add container variation data
			if isContainer(itemFreq[0]):
				freqNode.SubID += getContainerVariation(groupNode.Children)
