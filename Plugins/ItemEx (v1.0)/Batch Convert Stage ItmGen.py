__author__ = "Kapedani, mawwwk"
__version__ = "0.9.3"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

SCRIPT_NAME = "Convert Stage ItemGen Data v1.0"
ITEMEX_VERSION = "v1.0"
files_to_skip = [""]

def main():
	# Show starting info prompt
	startMsg = "Automatically update stage item generation data (ItemGen) to be compatible with builds using ItemEx " + ITEMEX_VERSION + ".\n\n" + \
	"NOTE: Converted stages may no longer be compatible with non-ItemEx builds. This process is irreversible!\n\n" + \
	"Press OK to continue to folder selection."
	if not BrawlAPI.ShowOKCancelPrompt(startMsg, SCRIPT_NAME):
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
	fileCount = len(files)
	progressCounter = 0
	progressBar = ProgressWindow(MainForm.Instance, "Updating", "Converting stage ItemGen data", False)
	progressBar.Begin(0, fileCount, progressCounter)
	
	# Loop through pac files
	for file in files:
		
		# Check whether file should be opened
		if Path.GetFileName(file) in files_to_skip or not Path.GetFileName(file).endswith(".pac"):
			continue
		
		progressBar.Caption = Path.GetFileName(file)
		
		# Open file
		fileOpened = BrawlAPI.OpenFile(file)
		if not fileOpened:
			continue
		
		# Loop through ItmTableGroup nodes in current pac
		for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
			updateItmTableGroupNode(groupNode)
	
		BrawlAPI.SaveFile()
		BrawlAPI.ForceCloseFile()
		
		# Update progress bar
		progressCounter += 1
		progressBar.Update(progressCounter)
	
	# Results
	progressBar.Finish()
	BrawlAPI.ShowMessage("Finished converting ItemGen data!", SCRIPT_NAME)

main()