"""Cybersecurity Asset Inventory System - Weekly Mini Project 01."""

import ipaddress
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
STATUSES = ["Secure", "Warning", "Vulnerable"]

LINE = "=" * 41
SEP = "-" * 41


# ---------- persistence ----------
def load_assets():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("[!] assets.json is corrupted or unreadable. Starting empty.")
        return []


def save_assets(assets):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(assets, f, indent=4)


# ---------- validated input helpers ----------
def prompt_text(label, default=None):
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{label}{suffix}: ").strip()
        if not value and default is not None:
            return default
        if value:
            return value
        print("[!] This field cannot be empty.")


def prompt_choice(label, options, default=None):
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{label} ({'/'.join(options)}){suffix}: ").strip()
        if not value and default is not None:
            return default
        for opt in options:
            if value.lower() == opt.lower():
                return opt
        print(f"[!] Invalid choice. Must be one of: {', '.join(options)}")


def prompt_ip(label, default=None):
    while True:
        suffix = f" [{default}]" if default else ""
        value = input(f"{label}{suffix}: ").strip()
        if not value and default is not None:
            return default
        try:
            return str(ipaddress.ip_address(value))
        except ValueError:
            print("[!] Invalid IP address (example: 192.168.1.10).")


def prompt_positive_int(label):
    while True:
        value = input(f"{label}: ").strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("[!] Enter a whole number greater than 0.")


def find_by_id(assets, asset_id):
    for asset in assets:
        if asset["asset_id"].lower() == asset_id.lower():
            return asset
    return None


def prompt_new_id(assets):
    while True:
        asset_id = prompt_text("Asset ID").upper()
        if find_by_id(assets, asset_id):
            print(f"[!] Asset ID {asset_id} already exists.")
        else:
            return asset_id


# ---------- display ----------
def print_asset(a):
    print(f"Asset ID : {a['asset_id']}")
    print(f"Asset Name : {a['asset_name']}")
    print(f"Asset Type : {a['asset_type']}")
    print(f"IP Address : {a['ip_address']}")
    print(f"OS : {a['os']}")
    print(f"Department : {a['department']}")
    print(f"Risk Level : {a['risk_level']}")
    print(f"Status : {a['status']}")


def count_where(assets, key, value):
    return sum(1 for a in assets if a[key] == value)


def print_summary(assets):
    print(LINE)
    print(f"Total Assets : {len(assets)}")
    print(f"Critical Assets : {count_where(assets, 'risk_level', 'Critical')}")
    print(f"High Risk Assets : {count_where(assets, 'risk_level', 'High')}")
    print(f"Medium Risk Assets : {count_where(assets, 'risk_level', 'Medium')}")
    print(f"Vulnerable Assets : {count_where(assets, 'status', 'Vulnerable')}")
    print(LINE)


# ---------- operations ----------
def add_assets(assets):
    count = prompt_positive_int("Enter number of assets")
    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        asset = {
            "asset_id": prompt_new_id(assets),
            "asset_name": prompt_text("Asset Name"),
            "asset_type": prompt_choice("Asset Type", ASSET_TYPES),
            "ip_address": prompt_ip("IP Address"),
            "os": prompt_text("Operating System"),
            "department": prompt_text("Department"),
            "risk_level": prompt_choice("Risk Level", RISK_LEVELS),
            "status": prompt_choice("Security Status", STATUSES),
        }
        assets.append(asset)
        save_assets(assets)
        print(f"[+] Asset {asset['asset_id']} added.")


def display_assets(assets):
    if not assets:
        print("[!] Inventory is empty.")
        return
    print(LINE)
    print(" CYBERSECURITY ASSET INVENTORY")
    print(LINE)
    for idx, a in enumerate(assets):
        print_asset(a)
        if idx < len(assets) - 1:
            print(SEP)
    print_summary(assets)


def search_assets(assets):
    print("Search by: 1) Asset ID  2) Name  3) Type  4) IP  5) Department  6) Risk Level  7) Status")
    fields = {
        "1": "asset_id", "2": "asset_name", "3": "asset_type", "4": "ip_address",
        "5": "department", "6": "risk_level", "7": "status",
    }
    choice = input("Choose (1-7): ").strip()
    if choice not in fields:
        print("[!] Invalid search option.")
        return
    key = fields[choice]
    term = prompt_text("Search term").lower()
    results = [a for a in assets if term in str(a[key]).lower()]
    if not results:
        print("[!] No matching assets found.")
        return
    print(f"\n{len(results)} match(es) found:")
    print(LINE)
    for idx, a in enumerate(results):
        print_asset(a)
        if idx < len(results) - 1:
            print(SEP)
    print(LINE)


def update_asset(assets):
    asset = find_by_id(assets, prompt_text("Enter Asset ID to update"))
    if not asset:
        print("[!] Asset not found.")
        return
    print("\nCurrent details:")
    print_asset(asset)
    print("\nPress Enter to keep the current value.")
    asset["asset_name"] = prompt_text("Asset Name", asset["asset_name"])
    asset["asset_type"] = prompt_choice("Asset Type", ASSET_TYPES, asset["asset_type"])
    asset["ip_address"] = prompt_ip("IP Address", asset["ip_address"])
    asset["os"] = prompt_text("Operating System", asset["os"])
    asset["department"] = prompt_text("Department", asset["department"])
    asset["risk_level"] = prompt_choice("Risk Level", RISK_LEVELS, asset["risk_level"])
    asset["status"] = prompt_choice("Security Status", STATUSES, asset["status"])
    save_assets(assets)
    print(f"[+] Asset {asset['asset_id']} updated.")


def delete_asset(assets):
    asset = find_by_id(assets, prompt_text("Enter Asset ID to delete"))
    if not asset:
        print("[!] Asset not found.")
        return
    print_asset(asset)
    confirm = input("Delete this asset? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print("[+] Asset deleted.")
    else:
        print("[-] Deletion cancelled.")


def security_summary(assets):
    if not assets:
        print("[!] Inventory is empty.")
        return
    print_summary(assets)
    urgent = [a for a in assets
              if a["risk_level"] in ("Critical", "High") and a["status"] != "Secure"]
    if urgent:
        print("\nNEEDS IMMEDIATE ATTENTION (Critical/High risk and not Secure):")
        for a in urgent:
            print(f" - {a['asset_id']} | {a['asset_name']} | "
                  f"{a['risk_level']} | {a['status']}")


# ---------- main ----------
def main():
    assets = load_assets()
    actions = {
        "1": add_assets, "2": display_assets, "3": search_assets,
        "4": update_asset, "5": delete_asset, "6": security_summary,
    }
    while True:
        print("\n" + LINE)
        print(" CYBERSECURITY ASSET INVENTORY SYSTEM")
        print(LINE)
        print("1. Add Assets\n2. Display All Assets\n3. Search Asset")
        print("4. Update Asset\n5. Delete Asset\n6. Security Summary\n7. Exit")
        choice = input("Select an option (1-7): ").strip()
        if choice == "7":
            print("Exiting. Stay secure.")
            break
        if choice in actions:
            actions[choice](assets)
        else:
            print("[!] Invalid option. Enter a number from 1 to 7.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nExiting. Stay secure.")
