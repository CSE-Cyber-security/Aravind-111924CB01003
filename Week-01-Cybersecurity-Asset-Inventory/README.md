# Week 01 - Cybersecurity Asset Inventory System

CLI tool for a security admin to add, search, update, delete, and display IT assets,
classified by type and risk level, with JSON persistence.

## Features
- CRUD for assets (Workstation, Server, Router, Switch, Application)
- Risk levels: Low / Medium / High / Critical
- Security status: Secure / Warning / Vulnerable
- Search by ID, name, type, IP, department, risk, or status
- Security summary that flags Critical/High assets that aren't Secure
- Persistent storage in `data/assets.json`

## Validation
- Duplicate Asset IDs rejected
- IP validated with Python's `ipaddress` module (IPv4/IPv6)
- Type, risk, and status restricted to allowed values (case-insensitive)
- No empty fields; numeric inputs checked

## Run
```bash
python src/asset_inventory.py
```
Requires Python 3.8+. No external dependencies.

## Structure
```
Week-01-Cybersecurity-Asset-Inventory/
├── src/asset_inventory.py
├── data/assets.json
├── tests/test_cases.md
├── screenshots/
└── README.md
```

## Notes
The sample input in the brief leaves the OS field blank for A101, but the expected output
shows "Windows 11". This implementation treats OS as required.
