# ItemEx

BrawlCrate scripts to manage ItemGen (stage item generation) data in stage .pac files for use with the ItemEx codebase.

## Installation
*Python 3.11.x or newer recommended. Set the Python install path inside Tools > Settings > BrawlAPI tab.*  

In BrawlCrate, navigate to Tools > Settings > Updater tab, and click the Manage Subscriptions button.  
Click add, then paste the link to this Github repo: https://github.com/markymawk/ItemEx  
These plug-ins will then be downloaded, and future updates will be pulled automatically!

## Usage
* **To install ItemEx** data for an entire stage folder, run Plugins > ItemEx > Batch Convert Stage ItemGen. For P+ build modders, this is likely the only step you'll need.

* To install itemEx data for a **single stage**, first open the stage .pac, locate the ItemGen ARC (usually at the bottom of the 2 ARC under Scene Data), right-click and select Plugins > **Convert Stage ItemGen**.

* ItemGen data can be reverted back to a vBrawl table using **Batch Restore Brawl ItemGen** for a stage folder, or in the right-click plugin menu for a single stage.
----
### About ItemGen compatibility
In order to spawn any items affected by ItemEx, including containers (crates), Bumper, and Screw Attack, ItemGen data in each stage .pac must be up-to-date. Using incomptatible ItemGen data is not known to cause crashes, but should be still avoided when possible. 

### Credits
ItemEx by Kapedani, Sammi Husky, KingJigglypuff, DukeItOut, MarioDox, mawwwk
