# ItemEx

BrawlCrate scripts to manage ItemGen (stage item generation) data in stage .pac files for use with the ItemEx codebase.

## Installation
*Python 3.11.x or newer recommended. Set the Python install path inside Tools > Settings > BrawlAPI tab.*  

In BrawlCrate, navigate to Tools > Settings > Updater tab, and click the Manage Subscriptions button.  
Click Add, then paste the link to this Github repo: https://github.com/markymawk/ItemEx  
These plug-ins will then be downloaded, and future updates will be pulled automatically!

## Usage
**To install ItemEx** data for an entire stage folder, run Plugins > ItemEx > Batch Convert Stage ItemGen.  
  _For P+ build modders, this is likely the only step you'll need._

To install itemEx data for a **single stage**, first open the stage .pac, locate the ItemGen ARC (usually at the bottom of the 2 ARC under Scene Data), right-click and select Plugins > **Convert Stage ItemGen**.

To revert ItemGen data back to a vBrawl table, use **Plugins > Batch Restore Brawl ItemGen** for a stage folder. For a single stage, right-click an ItmGen ARC and use the plugin menu.

----
### About ItemGen compatibility
In order to spawn any items affected by ItemEx, including containers (crates), Bumper, and Screw Attack, ItemGen data in each stage .pac must be converted accordingly. Using converted ItemGen data in non-ItemEx builds will have the same effect Using incomptatible ItemGen data is not known to cause crashes, but should be still avoided when possible.

An easy way to determine the format of an ItemGen is to check the ARC ItmGen > Item Generation 0 > Table 0 > Group 0, and count the instances of a container, such as a Barrel. ItemEx tables will use multiple of the same container (3 Barrels, 2 Capsules, etc.) while vBrawl tables use one of each. 

### Credits
ItemEx by Kapedani, Sammi Husky, KingJigglypuff, DukeItOut, MarioDox, mawwwk, soopercool101
