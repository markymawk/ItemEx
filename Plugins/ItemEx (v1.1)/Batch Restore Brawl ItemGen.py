__author__ = "Kapedani, mawwwk"
__version__ = "1.1.1"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.UI import * # MainForm CompabibilityMode
from ItemExLib import *
from System.IO import * # Directory.GetFiles
#from mawwwkLib import *

SCRIPT_NAME = "Restore Brawl ItemGen Data"

# Enter file names to skip over, i.e. "STGEXAMPLE.pac"
FILES_TO_SKIP = []

def main():
	# Show starting info prompt
	START_MSG = "Revert stage item generation (ItemGen) data to vBrawl behavior, replacing it with a generic Brawl item table.\n\n" + \
	"NOTE: Stages without ItemEx-compatible ItemGen data may fail to spawn certain items, such as containers.\n\n" + \
	"Press OK to continue to folder selection."
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
	
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
	
	# Enable compatibility mode to avoid corrupting older imports
	MainForm.Instance.CompatibilityMode = True
	
	# Loop through pac files
	for file in files:
		
		# Check whether file should be opened
		if Path.GetFileName(file) in FILES_TO_SKIP or not Path.GetFileName(file).lower().endswith(".pac"):
			continue
		
		# Attempt to open file, but skip if unable to
		if not BrawlAPI.OpenFile(file):
			continue
		
		# If root node has no children, skip this file
		if not (BrawlAPI.RootNode and BrawlAPI.RootNode.HasChildren):
			continue
			
		progressBar.Caption = Path.GetFileName(file)
		
		# Initialize item data lists to later determine if anything was changed
		oldItemList = []
		newItemList = []
			
		itmTableGroupNodes = []
		# Loop through children nodes to find ARCs (namely 2 ARC)
		for node in BrawlAPI.RootNode.Children:
			if not isinstance(node, ARCNode):
				continue
			
			# Loop through children nodes to find ARCs (namely ItmGen)
			for childNode in node.Children:
				if not isinstance(childNode, ARCNode):
					continue
				if childNode.FileIndex != 10000:
					continue
				
				# ItmFreqNode
				for itemFreqNode in childNode.Children:
					if not isinstance(itemFreqNode, ItmFreqNode):
						continue
					
					# ItmTableNode
					for itemTableNode in itemFreqNode.Children:
						for tableGroupNode in itemTableNode.Children:
							# ItemTableGroupNode
							itmTableGroupNodes.append(tableGroupNode)
		
		# Loop through ItmTableGroup nodes in current pac
		for groupNode in itmTableGroupNodes:
			if groupNode.Id != 10000:
				continue
			oldItemList.append(getItemFreqTable(groupNode))
			
			# Set to False to use vBrawl item table
			updateItmTableGroupNode(groupNode, False)
			
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
	
	# Restore compatibility mode setting
	MainForm.Instance.CompatibilityMode = False
	
	# Results
	progressBar.Finish()
	resultsMsg = "Finished reverting to vBrawl ItemGen data!\n" + \
	"Stage .pac files modified: " + str(changedPacsCount)
	
	if notChangedPacsCount:
		resultsMsg += "\n\nSome files already use this ItemGen data or were unaffected.\nStage .pac files unmodified: " + str(notChangedPacsCount)
	
	BrawlAPI.ShowMessage(resultsMsg, SCRIPT_NAME)

main()