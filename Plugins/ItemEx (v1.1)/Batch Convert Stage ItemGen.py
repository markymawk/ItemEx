__author__ = "Kapedani, mawwwk"
__version__ = "1.1"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

SCRIPT_NAME = "Convert Stage ItemGen Data v1.1"
ITEMEX_VERSION = "v1.1"
# Enter file names to skip over, i.e. STGEXAMPLE.pac
FILES_TO_SKIP = [
"STGBELLTOWER.pac",
"STGBELLTOWER_R_PS2_BELLTOWER.pac",
"STGPOKEFLOATS_L_POKEFLOATS2.pac"
]

def main():
	# Show starting info prompt
	START_MSG = "Update stage item generation (ItemGen) data to be compatible with builds using ItemEx " + ITEMEX_VERSION + ".\n\n" + \
	"NOTE: Converted stages may fail to spawn certain items, such as containers, in non-ItemEx builds.\n\n" + \
	"Press OK to continue to folder selection."
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
	
	isBuildPathSet = False
	# If build path is set, confirm intended dir
	if MainForm.BuildPath != '':
		meleeDir = MainForm.BuildPath + '\\pf\\stage\\melee\\'
		isBuildPathSet = BrawlAPI.ShowYesNoPrompt("Default build path detected.\n\nUpdate all stage .pacs inside\n" + meleeDir + "?\n\nSelect No to choose a different folder.", SCRIPT_NAME)
	
	# If build path not set, or previous prompt denied, prompt for new directory
	if not isBuildPathSet:
		meleeDir = BrawlAPI.OpenFolderDialog()
		# Quit if canceled
		if meleeDir == '':
			return
		
		# Final confirmation prompt
		if not BrawlAPI.ShowOKCancelPrompt("Updating all stage .pacs inside:\n" + meleeDir + "\n\nPress OK to continue.", SCRIPT_NAME):
			return

	# Initialize file list and progress bar
	files = Directory.GetFiles(meleeDir)
	changedPacsCount = 0
	notChangedPacsCount = 0
	progressBar = ProgressWindow(MainForm.Instance, "Updating", "Converting stage ItemGen data", False)
	progressCounter = 0
	progressBar.Begin(0, len(files), progressCounter)
	
	# Loop through pac files
	for file in files:
		
		# Check whether file should be opened
		if Path.GetFileName(file) in FILES_TO_SKIP or not Path.GetFileName(file).lower().endswith(".pac"):
			continue
		
		# Attempt to open file, but skip if unable to
		if not BrawlAPI.OpenFile(file):
			continue
		
		progressBar.Caption = Path.GetFileName(file)
		
		# Initialize item data lists to later determine if anything was changed
		oldItemList = []
		newItemList = []
		
		# Loop through ItmTableGroup nodes in current pac
		for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
			if groupNode.Id != 10000:
				continue
			oldItemList.append(getItemFreqTable(groupNode))
			updateItmTableGroupNode(groupNode)
			# Populate item data lists
			newItemList.append(getItemFreqTable(groupNode))
		
		# If item lists are the same, skip saving file to save time
		if oldItemList == newItemList:
			notChangedPacsCount += 1
		else:
			BrawlAPI.SaveFile()
			changedPacsCount += 1
		
		BrawlAPI.ForceCloseFile()
		
		# Update progress bar
		progressCounter += 1
		progressBar.Update(progressCounter)
	
	# Results
	progressBar.Finish()
	RESULTS_MSG = "Finished converting ItemGen data!\n" + \
	"Stage .pac files modified: " + str(changedPacsCount)
	
	if notChangedPacsCount:
		RESULTS_MSG += "\n\nSome files already use updated ItemGen data or were unaffected.\nStage .pac files unmodified: " + str(notChangedPacsCount)
	
	BrawlAPI.ShowMessage(RESULTS_MSG, SCRIPT_NAME)

main()