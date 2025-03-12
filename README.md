# ItemEx

BrawlCrate scripts to manage ItemGen (stage item generation) data in stage .pac files for use with the ItemEx codebase.

## Installation
*BrawlCrate v0.42 or newer recommended. Compatibility with older versions not guaranteed.*  

In BrawlCrate, navigate to Tools > Settings > Updater tab, and click the Manage Subscriptions button.  
Click Add, then paste the link to this Github repo: https://github.com/markymawk/ItemEx  
These plug-ins will then be downloaded, and future updates will be pulled automatically!

## Usage
**To install ItemEx** data for an entire stage folder, run Plugins > ItemEx > Batch Convert Stage ItemGen.  
  _For P+ build modders, this is likely the only step you'll need._

To install itemEx data for a **single stage**, first open the stage .pac and locate the ItemGen ARC (located inside the 2 ARC, often under Scene Data), then right-click it and select Plugins > **Convert Stage ItemGen**.

To revert ItemGen data back to a vBrawl table, use **Plugins > Batch Restore Brawl ItemGen** for a stage folder. For a single stage, right-click an ItmGen ARC and use the plugin menu.

----
### About ItemGen compatibility
For stages in ItemEx builds, ItemGen data in each stage .pac must be converted in order to spawn any items affected by ItemEx, such as containers (crates), Bumper, and Screw Attack. Likewise, using an ItemEx stage .pac in non-ItemEx builds will have the same effect. Using incompatible ItemGen data is not known to cause crashes, but should be still avoided when possible.

An easy way to determine the format of an ItemGen is to check the ARC ItmGen > Item Generation 0 > Table 0 > Group 0, and count the instances of any container. ItemEx tables will use multiple of the same container (3 Barrels, 2 Capsules, etc.) while vBrawl tables use one of each. 

### ItemEx credits
* Core functionality: Sammi Husky, Kapedani
* In-game toggles, implementation, & item development: Kapedani, DukeItOut, MarioDox
* In-game UI: mawwwk
* BrawlAPI stage scripting: mawwwk, Kapedani
* BrawlCrate formatting & implementation: soopercool101
