__author__ = "Kapedani, mawwwk"
__version__ = "0.9.3"

from BrawlCrate.API import BrawlAPI
from BrawlLib.SSBB.ResourceNodes import *
from BrawlLib.Internal import *
from BrawlLib.Internal.Windows.Forms import *
from BrawlCrate.NodeWrappers import *
from BrawlCrate.UI import *
from System.IO import *
from ItemExLib import *

from System.Windows.Forms import ToolStripMenuItem

SCRIPT_NAME = "Convert Stage ItemGen Data v1.0"
ITEMEX_VERSION = "v1.0"

OPTION_NAME = "Convert Stage ItemGen (ItemEx " + ITEMEX_VERSION + ")"

startMsg = "Automatically update stage item generation data (ItemGen) to be compatible with builds using ItemEx " + ITEMEX_VERSION + ".\n\n" + \
"NOTE: Converted stages may no longer be compatible with non-ItemEx builds. This process is irreversible!\n\n" + \
"Press OK to continue."

## Start enable check function
def EnableCheck_rootARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.Children \
	and node.FindChild("2") is not None \
	and BrawlAPI.RootNode.FilePath.endswith(".pac"))

def EnableCheck_ItmGenARC(sender, event_args):
	node = BrawlAPI.SelectedNode
	
	sender.Enabled = (node is not None \
	and node.Children \
	and node.FileIndex == 10000 \
	and "ItmFreqNode" in node.Children[0].NodeType \
	and BrawlAPI.RootNode.FilePath.endswith(".pac"))
## End enable check function

## Start loader functions

def convert_stage_itemgen_rootARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(startMsg, SCRIPT_NAME):
		return
	
	for groupNode in BrawlAPI.NodeListOfType[ItmTableGroupNode]():
		updateItmTableGroupNode(groupNode)
	
	BrawlAPI.ShowMessage("Stage ItemGen data updated!", SCRIPT_NAME)
	
def convert_stage_itemgen_ItmGenARC(sender, event_args):
	if not BrawlAPI.ShowOKCancelPrompt(startMsg, SCRIPT_NAME):
		return
	
	for child in BrawlAPI.SelectedNode.GetChildrenRecursive():
		if "ItmTableGroupNode" in child.NodeType:
			updateItmTableGroupNode(child)
	
	BrawlAPI.ShowMessage("Stage ItemGen data updated!", SCRIPT_NAME)
## End loader functions
## Start context menu add

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_rootARC, ToolStripMenuItem(OPTION_NAME, None, convert_stage_itemgen_rootARC))

BrawlAPI.AddContextMenuItem(ARCWrapper, "", "Convert stage ItemGen", EnableCheck_ItmGenARC, ToolStripMenuItem(OPTION_NAME, None, convert_stage_itemgen_ItmGenARC))
