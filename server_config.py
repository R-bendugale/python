# Server configuration
server_ip = ("192.168.1.1",)  # tuple - cannot change
allowed_ips = ["192.168.1.10", "192.168.1.15"]  # list - can change

# Update allowed IPs
new_ip = input("Enter new allowed IP: ")
if new_ip not in allowed_ips:
    allowed_ips.append(new_ip)
    print("IP added successfully.")
else:
    print("IP already exists in the list.")

# Try to change server IP (not allowed)
print("\nTrying to change server IP...")
try:
    server_ip[0] = "10.0.0.1"
except TypeError:
    print("Error: Cannot change Server IP (it's stored in a tuple).")

# Show updated configuration
print("\nServer IP:", server_ip[0])
print("Allowed IPs:", allowed_ips)
