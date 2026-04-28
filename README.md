# grapes3-efficiency-correction
Code for automated mitigation of long-term efficiency variations in the GRAPES-3 muon telescope (Paul et al., 2025)

## Data Availability

The raw GRAPES-3 muon and atmospheric pressure data are not publicly available due to collaboration policies.

This repository provides intermediate data products starting from the Bayesian block stage through to the final efficiency correction.

## How to Run

Run the scripts sequentially:

1. bayesian_block.py        
2. merge_threshold.py
3. reference_module_blockwise.py
4. store_reference_module.py
5. stitch_reference_module.py
6. stitching.py
7.  efficiency_correction.py

Each script will prompt for:
- Year offset (e.g., 11 for 2011)
- Direction number =225 
