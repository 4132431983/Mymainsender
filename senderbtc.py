import os
import subprocess

def transfer_btc(wallet_path, recipient_address, amount):
    # Check if the wallet.dat file exists
    if not os.path.isfile(wallet_path):
        print("Wallet file not found!")
        return

    # Command to transfer Bitcoin using Bitcoin Core CLI
    command = [
        'bitcoin-cli', 
        '-datadir=' + os.path.dirname(wallet_path), 
        'sendtoaddress', 
        recipient_address, 
        str(amount)
    ]

    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Transaction successful! Transaction ID: {result.stdout.strip()}")
        else:
            print(f"Error: {result.stderr.strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
wallet_path = '/home/userland/Btcpython.py/Wallet.dat'  # Update this path
recipient_address = 'bc1qwzuuzw8sq6ezgh9w3jq5jsszztw693ydnu6xge'  # Update with the recipient's address
amount = 18.0  # Amount of BTC to send

transfer_btc(wallet_path, recipient_address, amount)