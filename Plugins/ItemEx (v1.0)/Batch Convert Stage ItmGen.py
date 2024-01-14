__author__ = "Kapedani, mawwwk"
__version__ = "0.9.6"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

SCRIPT_NAME = "Convert Stage ItemGen Data v1.0"
ITEMEX_VERSION = "v1.0"
# Enter file names to skip over, i.e. STGEXAMPLE.pac
FILES_TO_SKIP = [""]

def main():
	# Show starting info prompt
	START_MSG = "Automatically update stage item generation (ItemGen) data to be compatible with builds using ItemEx " + ITEMEX_VERSION + ".\n\n" + \
	"NOTE: Converted stages may no longer be compatible with non-ItemEx builds when items are enabled. This process is irreversible!\n\n" + \
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
		if not BrawlAPI.ShowYesNoPrompt("Update all stage .pacs inside\n" + meleeDir + "?", SCRIPT_NAME):
			return

	# Initialize file list and progress bar
	files = Directory.GetFiles(meleeDir)
	progressCounter = 0
	changedPacsCount = 0
	notChangedPacsCount = 0
	progressBar = ProgressWindow(MainForm.Instance, "Updating", "Converting stage ItemGen data", False)
	progressBar.Begin(0, len(files), progressCounter)
	
	# Loop through pac files
	for file in files:
		
		# Check whether file should be opened
		if Path.GetFileName(file) in FILES_TO_SKIP or not Path.GetFileName(file).lower().endswith(".pac"):
			continue
		
		# Open file
		if not BrawlAPI.OpenFile(file):
			continue
		
		progressBar.Caption = Path.GetFileName(file)
		
		# Store item data lists to determine if anything was changed
		oldItemList = []
		newItemList = []
		
		# Loop through ItmTableGroup nodes in current pac
		for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
			update = updateItmTableGroupNode(groupNode, True)
			if update:
				oldItemList.append(update[0])
				newItemList.append(update[1])
		
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
	RESULTS_MSG = "Finished converting ItemGen data!\n\n" + \
	".pac files changed: " + str(changedPacsCount) + "\n" + \
	".pac files unaffected: " + str(notChangedPacsCount)
	BrawlAPI.ShowMessage(RESULTS_MSG, SCRIPT_NAME)

main()