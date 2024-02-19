__author__ = "Kapedani, mawwwk"
__version__ = "1.0"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.NodeWrappers import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

from System.Windows.Forms import ToolStripMenuItem

SCRIPT_NAME = "Restore vBrawl ItemGen Data"
OPTION_NAME = "Restore vBrawl ItemGen Data"

START_MSG = "Revert stage item generation (ItemGen) data to a default Brawl item table, removing compatibility with builds using ItemEx.\n\n" + \
"NOTE: If used in an ItemEx build, reverting ItemGen data may fail to spawn certain items, such as containers.\n\n" + \
"Press OK to continue."

## Start enable check function
# Wrapper: ARCWrapper
def EnableCheck_rootARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.Children \
	and node.FindChild("2") is not None \
	and BrawlAPI.RootNode.FilePath.endswith(".pac"))

# Wrapper: ARCWrapper
def EnableCheck_ItmGenARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.FileIndex == 10000 \
	and node.Children \
	and "ItmFreqNode" in node.Children[0].NodeType \
	and BrawlAPI.RootNode.FilePath.endswith(".pac"))

## End enable check function
## Start loader functions

def restore_vBrawl_itemgen_rootARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
		
	updatedNodes = [] # ItmGen ARC nodes updated
	
	for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
		updatedNodes.append(groupNode.Parent.Parent.Parent) # Store ARC node
		updateItmTableGroupNode(groupNode, False)
	
	# Results
	if len(updatedNodes):
		BrawlAPI.ShowMessage("ItemGen data updated!\n\n" + nodeListToString(list(set(updatedNodes))), SCRIPT_NAME)
	# If no nodes updated
	else:
		BrawlAPI.ShowError("No ItmTableGroup nodes found in the current file.", "Error")

def restore_vBrawl_itemgen_ItmGenARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
		
	isUpdated = False
	
	for child in BrawlAPI.SelectedNode.GetChildrenRecursive():
		if "ItmTableGroupNode" in child.NodeType:
			isUpdated = True
			updateItmTableGroupNode(child, False)
	
	if isUpdated:
		BrawlAPI.ShowMessage(BrawlAPI.SelectedNode.Name + " data updated!", SCRIPT_NAME)
	else:
		BrawlAPI.ShowError("No ItmTableGroup nodes found inside the selected ARC.", "Error")

## End loader functions
## Start context menu add

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_rootARC, ToolStripMenuItem(OPTION_NAME, None, restore_vBrawl_itemgen_rootARC))

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_ItmGenARC, ToolStripMenuItem(OPTION_NAME, None, restore_vBrawl_itemgen_ItmGenARC))
