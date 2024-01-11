__author__ = "Kapedani, mawwwk"
__version__ = "0.9.1"

#from enum import Enum
from BrawlCrate.API import BrawlAPI
from System.IO import *
from BrawlLib.Internal import *
from BrawlCrate.UI import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.NodeWrappers import *
from BrawlCrate.API.BrawlAPI import AppPath
from BrawlLib.SSBB.ResourceNodes import *

# class Item(Enum):
# 	Common = -0x3
# 	AssistTrophy = 0x00
# 	Assist = 0x00
# 	FranklinBadge = 0x01
# 	Badge = 0x01
# 	BananaPeel = 0x02
# 	Banana = 0x02
# 	Barrel = 0x03
# 	BeamSword = 0x04
# 	Bill = 0x05
# 	BobOmb = 0x06
# 	Bombhei = 0x06
# 	Crate = 0x07
# 	Box = 0x07
# 	Bumper = 0x08
# 	Capsule = 0x09
# 	RollingCrate = 0x0A
# 	CarrierBox = 0x0A
# 	CD = 0x0B
# 	GooeyBomb = 0x0C
# 	Chewing = 0x0C
# 	CrackerLauncher = 0x0D
# 	Clacker = 0x0D
# 	CrackerLauncher_Shot = 0x0E
# 	Clacker_Shot = 0x0E
# 	Coin = 0x0F
# 	SuperspicyCurry = 0x10
# 	Curry = 0x10
# 	SuperspicyCurry_Shot = 0x11
# 	Curry_Shot = 0x11
# 	DekuNut = 0x12
# 	Deku = 0x12
# 	MrSaturn = 0x13
# 	Doseisan = 0x13
# 	Dragoon_Part = 0x14
# 	Dragoon = 0x14
# 	Dragoon_Set = 0x15
# 	Dragoon_Sight = 0x16
# 	Trophy = 0x17
# 	Figure = 0x17
# 	FireFlower = 0x18
# 	FireFlower_Shot = 0x19
# 	Freezie = 0x1A
# 	Freezer = 0x1A
# 	GoldenHammer = 0x1B
# 	GreenShell = 0x1C
# 	Hammer = 0x1D
# 	Hammer_Head = 0x1E
# 	Fan = 0x1F
# 	Harisen = 0x1F
# 	HeartContainer = 0x20
# 	Heart = 0x20
# 	HomeRunBat = 0x21
# 	PartyBall = 0x22
# 	Kusudama = 0x22
# 	Manaphy_Heart = 0x23
# 	MaximTomato = 0x24
# 	PoisonMushroom = 0x25
# 	MushD = 0x25
# 	SuperMushroom = 0x26
# 	Mushroom = 0x26
# 	MetalBox = 0x27
# 	Hothead = 0x28
# 	Pasaran = 0x28
# 	Pitfall = 0x29
# 	PokeBall = 0x2A
# 	BlastBox = 0x2B
# 	PowderBox = 0x2B
# 	RayGun = 0x2C
# 	RayGun_Shot = 0x2D
# 	LipStick = 0x2E
# 	RipStick = 0x2E
# 	LipStick_Flower = 0x2F
# 	RipStick_Flower = 0x2f
# 	LipStick_Shot = 0x30
# 	RipStick_Shot = 0x30
# 	Sandbag = 0x31
# 	ScrewAttack = 0x32
# 	Screw = 0x32
# 	Sticker = 0x33
# 	Seal = 0x33
# 	MotionSensorBomb = 0x34
# 	SensorBomb = 0x34
# 	Timer = 0x35
# 	Slow = 0x35
# 	SmartBomb = 0x36
# 	SmashBall = 0x37
# 	SmokeScreen = 0x38
# 	Spring = 0x39
# 	StarRod = 0x3A
# 	StarRod_Shot = 0x3B
# 	SoccerBall = 0x3C
# 	SuperScope = 0x3D
# 	SuperScope_Shot = 0x3E
# 	Star = 0x3F
# 	Starman = 0x3f
# 	Food = 0x40
# 	Tabemono = 0x40
# 	TeamHealer = 0x41
# 	TeamHealing = 0x41
# 	Lightning = 0x42
# 	Thunder = 0x42
# 	Unira = 0x43
# 	BunnyHood = 0x44
# 	UsagiHat = 0x44
# 	WarpStar = 0x45
# 	Warpstar = 0x45
# 	Subspace_Trophy = 0x46
# 	Adventure_Figure = 0x46
# 	Subspace_Key = 0x47
# 	Adventure_Key = 0x47
# 	Subspace_TrophyStand = 0x48
# 	Adventure_SmashPlate = 0x48
# 	Subspace_StockBall = 0x49
# 	Adventure_Stock = 0x49
# 	GreenGreens_Apple = 0x4A
# 	DxGreens_Apple = 0x4A
# 	MarioBros_Sidestepper = 0x4B
# 	Famicom_Clab = 0x4b
# 	MarioBros_Shellcreeper = 0x4C
# 	Famicom_Shell = 0x4c
# 	DistantPlanet_Pellet = 0x4D
# 	Earth_Pellet = 0x4D
# 	Summit_Vegetable = 0x4E
# 	Ice_Vegetable = 0x4E
# 	HomeRun_Sandbag = 0x4F
# 	Enemy_Auroros = 0x50
# 	Enemy_Aroaros = 0x50
# 	Enemy_Koopa1 = 0x51
# 	Enemy_Patapata = 0x51
# 	Enemy_Koopa2 = 0x52
# 	Enemy_PatapataG = 0x52
# 	Snake_CardboardBox = 0x53
# 	Snake_CBox = 0x53
# 	DiddyKong_Peanut = 0x54
# 	Diddy_Peanuts = 0x54
# 	Link_Bomb = 0x55
# 	Peach_Turnip = 0x56
# 	Peach_Daikon = 0x56
# 	ROB_Gyro = 0x57
# 	Robot_Gyro = 0x57
# 	DiddyKong_Peanut_Seed = 0x58
# 	Diddy_Peanuts_Seed = 0x58
# 	Snake_Grenade = 0x59
# 	ZeroSuitSamus_ArmorPiece = 0x5A
# 	SZeroSuit_Armor = 0x5A
# 	ToonLink_Bomb = 0x5B
# 	Wario_Bike = 0x5C
# 	Wario_Bike_A = 0x5D
# 	Wario_Bike_B = 0x5E
# 	Wario_Bike_C = 0x5F
# 	Wario_Bike_D = 0x60
# 	Wario_Bike_E = 0x61
# 	Pokemon_Torchic = 0x62
# 	Pokemon_Achamo = 0x62
# 	Pokemon_Celebi = 0x63
# 	Pokemon_Cerebi = 0x63
# 	Pokemon_Chikorita = 0x64
# 	Pokemon_Chicorita = 0x64
# 	Pokemon_Chikorita_Shot = 0x65
# 	Pokemon_Chicorita_Shot = 0x65
# 	Pokemon_Entei = 0x66
# 	Pokemon_Moltres = 0x67
# 	Pokemon_Fire = 0x67
# 	Pokemon_Munchlax = 0x68
# 	Pokemon_Gonbe = 0x68
# 	Pokemon_Deoxys = 0x69
# 	Pokemon_Groudon = 0x6A
# 	Pokemon_Gulpin = 0x6B
# 	Pokemon_Gokulin = 0x6B
# 	Pokemon_Staryu = 0x6C
# 	Pokemon_Hitodeman = 0x6C
# 	Pokemon_Staryu_Shot = 0x6D
# 	Pokemon_Hitodeman_Shot = 0x6D
# 	Pokemon_HoOh = 0x6E
# 	Pokemon_Houou = 0x6E
# 	Pokemon_HoOh_Shot = 0x6F
# 	Pokemon_Houou_Shot = 0x6F
# 	Pokemon_Jirachi = 0x70
# 	Pokemon_Snorlax = 0x71
# 	Pokemon_Kabigon = 0x71
# 	Pokemon_Bellossom = 0x72
# 	Pokemon_Kireihana = 0x72
# 	Pokemon_Kyogre = 0x73
# 	Pokemon_Kyogre_Shot = 0x74
# 	Pokemon_LatiasLatios = 0x75
# 	Pokemon_Lugia = 0x76
# 	Pokemon_Lugia_Shot = 0x77
# 	Pokemon_Manaphy = 0x78
# 	Pokemon_Weavile = 0x79
# 	Pokemon_Manyula = 0x79
# 	Pokemon_Electrode = 0x7A
# 	Pokemon_Marumine = 0x7A
# 	Pokemon_Metagross = 0x7B
# 	Pokemon_Mew = 0x7C
# 	Pokemon_Meowth = 0x7D
# 	Pokemon_Nyarth = 0x7D
# 	Pokemon_Meowth_Shot = 0x7E
# 	Pokemon_Nyarth_Shot = 0x7E
# 	Pokemon_Piplup = 0x7F
# 	Pokemon_Pochama = 0x7F
# 	Pokemon_Togepi = 0x80
# 	Pokemon_Togepy = 0x80
# 	Pokemon_Goldeen = 0x81
# 	Pokemon_Tosakinto = 0x81
# 	Pokemon_Gardevoir = 0x82
# 	Pokemon_Sirnight = 0x82
# 	Pokemon_Wobbuffet = 0x83
# 	Pokemon_Sonans = 0x83
# 	Pokemon_Suicune = 0x84
# 	Pokemon_Bonsly = 0x85
# 	Pokemon_Usohachi = 0x85
# 	Assist_Andross = 0x86
# 	Assist_Andross_Shot = 0x87
# 	Assist_Barbara = 0x88
# 	Assist_GrayFox = 0x89
# 	Assist_Cyborg = 0x89
# 	Assist_RayMKII = 0x8A
# 	Assist_CustomRobo = 0x8A
# 	Assist_RayMKII_Bomb = 0x8B
# 	Assist_CustomRobo_Bomb = 0x8B
# 	Assist_RayMKII_Gun = 0x8C
# 	Assist_CustomRobo_Gun = 0x8C
# 	Assist_SamuraiGoroh = 0x8D
# 	Assist_Goroh = 0x8D
# 	Assist_Devil = 0x8E
# 	Assist_Excitebike = 0x8F
# 	Assist_Jeff = 0x90
# 	Assist_Jeff_PencilBullet = 0x91
# 	Assist_Jeff_PencilRocket = 0x92
# 	Assist_Lakitu = 0x93
# 	Assist_Jugem = 0x93
# 	Assist_KnuckleJoe = 0x94
# 	Assist_Joe = 0x94
# 	Assist_KnuckleJoe_Shot = 0x95
# 	Assist_Joe_Shot = 0x95
# 	Assist_HammerBro = 0x96
# 	Assist_HammerBros = 0x96
# 	Assist_HammerBro_Hammer = 0x97
# 	Assist_HammerBros_Hammer = 0x97
# 	Assist_Helirin = 0x98
# 	Assist_Heririn = 0x98
# 	Assist_KatAna = 0x99
# 	Assist_KatAna_Ana = 0x9A
# 	Assist_JillDozer = 0x9B
# 	Assist_Kururi = 0x9B
# 	Assist_Lyn = 0x9C
# 	Assist_Lin = 0x9C
# 	Assist_LittleMac = 0x9D
# 	Assist_Metroid = 0x9E
# 	Assist_Nintendog = 0x9F
# 	Assist_Nintendogs = 0x9F
# 	Assist_Nintendog_Full = 0xA0
# 	Assist_Nintendogs_Hi = 0xA0
# 	Assist_MrResetti = 0xA1
# 	Assist_Resetsan = 0xA1
# 	Assist_Isaac = 0xA2
# 	Assist_Robin = 0xA2
# 	Assist_Isaac_Shot = 0xA3
# 	Assist_Robin_Shot = 0xA3
# 	Assist_Saki = 0xA4
# 	Assist_Saki_Shot1 = 0xA5
# 	Assist_Saki_Shot2 = 0xA6
# 	Assist_Shadow = 0xA7
# 	Assist_War_Infantry = 0xA8
# 	Assist_War_Soldier = 0xA8
# 	Assist_War_Infantry_Shot = 0xA9
# 	Assist_War_Soldier_Shot = 0xA9
# 	Assist_Starfy = 0xAA
# 	Assist_Stafy = 0xAA
# 	Assist_War_Tank = 0xAB
# 	Assist_War_Tank_Shot = 0xAC
# 	Assist_Tingle = 0xAD
# 	Assist_Lakitu_Spiny = 0xAE
# 	Assist_Jugem_Togezo = 0xAE
# 	Assist_Waluigi = 0xAF
# 	Assist_DrWright = 0xB0
# 	Assist_Wright = 0xB0
# 	Assist_DrWright_Building = 0xB1
# 	Assist_Wright_Buil = 0xB1
# 	Unknown1 = 0x7D1
# 	Unknown2 = 0x7D2
# 	Unknown3 = 0x7D3
# 	Unknown4 = 0x7D4
# 	Unknown5 = 0x7D5

files_to_skip = [""]

item_freqs = [(0x00, 5000, 1, 1, 24.0),
			  (0x03, 6, 1, 1, 27.0),
			  (0x03, 12, 1, 1, 4.0),
			  (0x03, 18, 1, 1, 4.0),
			  (0x07, 6, 1, 1, 40.0),
			  (0x07, 12, 1, 1, 5.0),
			  (0x07, 18, 1, 1, 5.0),
			  (0x09, 6, 1, 1, 135.0),
			  (0x09, 18, 1, 1, 15.0),
			  (0x0A, 6, 1, 1, 8.0),
			  (0x0A, 12, 1, 1, 1.0),
			  (0x0A, 18, 1, 1, 1.0),
			  (0x22, 6, 1, 1, 25.0),
			  (0x22, 12, 1, 1, 3.0),
			  (0x22, 18, 1, 1, 3.0),
			  (0x2a, 5000, 1, 1, 50.0),
			  (0x31, 5000, 1, 1, 7.0),
			  (0x20, 5000, 1, 1, 3.0),
			  (0x24, 5000, 1, 1, 7.0),
			  (0x40, 5000, 1, 1, 24.0),
			  (0x10, 5000, 1, 1, 6.0),
			  (0x27, 5000, 1, 1, 6.0),
			  (0x25, 5000, 1, 1, 5.0),
			  (0x26, 5000, 1, 1, 9.0),
			  (0x35, 5000, 1, 1, 8.0),
			  (0x3f, 5000, 1, 1, 7.0),
			  (0x42, 5000, 1, 1, 6.0),
			  (0x45, 5000, 1, 1, 15.0),
			  (0x0d, 5000, 1, 1, 12.0),
			  (0x18, 5000, 1, 1, 12.0),
			  (0x2c, 5000, 1, 1, 14.0),
			  (0x3d, 5000, 1, 1, 17.0),
			  (0x04, 5000, 1, 1, 15.0),
			  (0x1b, 5000, 1, 1, 2.0),
			  (0x1d, 5000, 1, 1, 9.0),
			  (0x1f, 5000, 1, 1, 15.0),
			  (0x21, 5000, 1, 1, 5.0),
			  (0x2e, 5000, 1, 1, 9.0),
			  (0x3a, 5000, 1, 1, 8.0),
			  (0x02, 5000, 1, 1, 14.0),
			  (0x06, 5000, 1, 1, 20.0),
			  (0x08, 0, 1, 1, 5.0),
			  (0x08, 8200, 1, 1, 5.0),
			  (0x0c, 5000, 1, 1, 11.0),
			  (0x12, 5000, 1, 1, 10.0),
			  (0x13, 5000, 1, 1, 7.0),
			  (0x1a, 5000, 1, 1, 12.0),
			  (0x1c, 5000, 1, 1, 9.0),
			  (0x28, 5000, 1, 1, 8.0),
			  (0x29, 5000, 1, 1, 14.0),
			  (0x34, 5000, 1, 1, 13.0),
			  (0x36, 5000, 1, 1, 13.0),
			  (0x38, 5000, 1, 1, 13.0),
			  (0x39, 5000, 1, 1, 9.0),
			  (0x41, 5000, 1, 1, 18.0),
			  (0x01, 5000, 1, 1, 8.0),
			  (0x32, 0, 1, 1, 6.0),
			  (0x32, 8234, 1, 1, 6.0),
			  (0x44, 5000, 1, 1, 10.0),
			  (0x3c, 5000, 1, 1, 10.0),
			  (0x43, 5000, 1, 1, 8.0),
			  (0x14, 5000, 1, 1, 5.0),
			  (0x2b, 5000, 1, 1, 10.0),
			  (0x37, 5000, 1, 1, 150.0)]

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

def main():
	isBuildPathSet = False
	# If build path is set, confirm intended dir
	if MainForm.BuildPath != '':
		meleeDir = MainForm.BuildPath + '/pf/stage/melee'
		isBuildPathSet = BrawlAPI.ShowYesNoPrompt("Update all stage .pacs inside\n" + meleeDir + "?\n\nSelect No to choose a different folder.","Update Stage ItmGens")
	
	# If build path not set, or previous prompt denied, prompt for new directory
	if not isBuildPathSet:
		meleeDir = BrawlAPI.OpenFolderDialog()
		# Quit if canceled
		if meleeDir == '':
			return
		
		# Final confirmation prompt
		if not BrawlAPI.ShowYesNoPrompt("Update all stage .pacs inside\n" + meleeDir + "?","Update Stage ItmGens"):
			return
	
	files = Directory.GetFiles(meleeDir)

	# Set up progress bar
	progressCounter = 0
	fileCount = len(files)
	progressBar = ProgressWindow(MainForm.Instance, "Updating", "Preparing Stage ItmGens", False)
	progressBar.Begin(0, fileCount, progressCounter)
	
	# Loop through pac files
	for file in files:
		
		# Check whether file should be opened
		if Path.GetFileName(file) in files_to_skip or Path.GetFileName(file).endswith(".pac"):
			continue
			
		progressBar.Caption = Path.GetFileName(file)
		
		# Open file
		fileOpened = BrawlAPI.OpenFile(file)
		if not fileOpened:
			continue
		
		# Loop through ItmTableGroup nodes in current pac
		for node in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
			if node.Id == 10000:
				itmFreqEntryNodes = []
				
				# Generate list of ItemFreqEntry nodes for common (vBrawl) items
				for freqNode in node.Children:
					if isCommonItem(freqNode.ItemID):
						itmFreqEntryNodes.append(freqNode)
				
				# Remove all common ItemFreqEntry nodes
				for freqNode in itmFreqEntryNodes:
					freqNode.Remove()
				
				# Create new item freq nodes
				for item_freq in item_freqs:
					freqNode = ItmFreqEntryNode()
					freqNode.ItemID = item_freq[0]
					freqNode.SubID = item_freq[1]
					if isContainer(item_freq[0]):
						freqNode.SubID += getContainerVariation(node.Children)
					freqNode.Minimum = item_freq[2]
					freqNode.Maximum = item_freq[3]
					freqNode.Frequency = item_freq[4]
					node.AddChild(freqNode)
	
		BrawlAPI.SaveFile()
		BrawlAPI.ForceCloseFile()
		# Update progress bar
		progressCounter += 1
		progressBar.Update(progressCounter)
	progressBar.Finish()
	BrawlAPI.ShowMessage("Finished converting ItmGens.", "Finished")

main()