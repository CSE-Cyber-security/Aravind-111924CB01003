# Test Cases - Cybersecurity Asset Inventory

| ID | Feature | Input | Expected Result | Screenshot |
|----|---------|-------|-----------------|------------|
| TC01 | Add asset | Option 1, count 3, sample data | 3 assets saved to assets.json | 01-add-asset.png |
| TC02 | Display | Option 2 | All assets plus summary matching expected output | 02-display-assets.png |
| TC03 | Search by name | Option 3 > 2 > "router" | Core-Router returned | 03-search-asset.png |
| TC04 | Search no match | Option 3 > 2 > "zzz" | "No matching assets found" | - |
| TC05 | Update | Option 4, A101, Status > Warning | A101 status updated, persists after restart | 04-update-asset.png |
| TC06 | Delete | Option 5, throwaway asset, confirm y | Asset removed | 05-delete-asset.png |
| TC07 | Delete cancel | Option 5, A102, confirm n | Asset still present | - |
| TC08 | Summary | Option 6 | Correct counts + urgent-attention list | 06-security-summary.png |
| TC09 | Duplicate ID | Add "A101" again | Rejected, re-prompted | 07-input-validation.png |
| TC10 | Invalid type | Asset Type: "Laptop" | Rejected, re-prompted | 07-input-validation.png |
| TC11 | Invalid IP | IP: "999.1.1.1" | Rejected, re-prompted | 07-input-validation.png |
| TC12 | Empty OS | OS: (blank) | Rejected, re-prompted | 07-input-validation.png |
| TC13 | Invalid risk/status | Risk: "Severe" | Rejected, re-prompted | 07-input-validation.png |
| TC14 | Invalid count | Number of assets: "abc" or 0 | Rejected, re-prompted | - |
| TC15 | Invalid menu | Option 9 | "Invalid option" message | - |
| TC16 | Empty inventory | Delete all, then option 2 | "Inventory is empty" | - |
