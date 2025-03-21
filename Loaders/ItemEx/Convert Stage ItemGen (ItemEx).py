__author__ = "Kapedani, mawwwk"
__version__ = "1.1.1"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.NodeWrappers import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

from System.Windows.Forms import ToolStripMenuItem

ITEMEX_VERSION = "v1.1"
SCRIPT_NAME = "Convert Stage ItemGen Data " + ITEMEX_VERSION

OPTION_NAME = "Convert Stage ItemGen (ItemEx " + ITEMEX_VERSION + ")"

START_MSG = "Update stage item generation (ItemGen) data to be compatible with builds using ItemEx " + ITEMEX_VERSION + ".\n\n" + \
"NOTE: Converted stage .pacs may fail to spawn certain items, such as containers, in non-ItemEx builds.\n\n" + \
"Press OK to continue."

## Start enable check function
# Wrapper: ARCWrapper
def EnableCheck_rootARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.Children \
	and node.FindChild("2") is not None \
	and BrawlAPI.RootNode.FilePath.lower().endswith(".pac"))

# Wrapper: ARCWrapper
def EnableCheck_ItmGenARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.FileIndex == 10000 \
	and node.Children \
	and "ItmFreqNode" in node.Children[0].NodeType \
	and BrawlAPI.RootNode.FilePath.lower().endswith(".pac"))

## End enable check function
## Start loader functions

def convert_stage_itemgen_rootARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
		
	updatedNodes = [] # ItmGen ARC nodes updated
	
	for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
		updatedNodes.append(groupNode.Parent.Parent.Parent) # Store ARC node
		updateItmTableGroupNode(groupNode)
	
	# Results
	if len(updatedNodes):
		BrawlAPI.ShowMessage("ItemGen data updated!\n\n" + nodeListToString(list(set(updatedNodes))), SCRIPT_NAME)
	# If no nodes updated
	else:
		BrawlAPI.ShowError("No ItmTableGroup nodes found in the current file.", "Error")

def convert_stage_itemgen_ItmGenARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(START_MSG, SCRIPT_NAME):
		return
		
	isUpdated = False
	
	for child in BrawlAPI.SelectedNode.GetChildrenRecursive():
		if "ItmTableGroupNode" in child.NodeType:
			isUpdated = True
			updateItmTableGroupNode(child)
	
	if isUpdated:
		BrawlAPI.ShowMessage(BrawlAPI.SelectedNode.Name + " data updated!", SCRIPT_NAME)
	else:
		BrawlAPI.ShowError("No ItmTableGroup nodes found inside the selected ARC.", "Error")

## End loader functions
## Start context menu add

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_rootARC, ToolStripMenuItem(OPTION_NAME, None, convert_stage_itemgen_rootARC))

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_ItmGenARC, ToolStripMenuItem(OPTION_NAME, None, convert_stage_itemgen_ItmGenARC))
