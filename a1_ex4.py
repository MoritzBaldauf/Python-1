print("=" * 50)
print("PC Parts Store - Order")
print("=" * 50)
n_cables = int(input("Number of cables: "))
n_monitors = int(input("Number of monitors: "))
n_keyboards = int(input("Number of keyboards: "))
cable_price = 9.90
monitor_price = 249.99
keyboard_price = 27.50
cable_total = n_cables * cable_price
monitor_total = n_monitors * monitor_price
keyboard_total = n_keyboards * keyboard_price
print(f"{n_cables:3d} cables ({cable_price:.2f} EUR each) = {cable_total:.2f} EUR")
print(f"{n_monitors:3d} monitors ({monitor_price:.2f} EUR each) = {monitor_total:.2f} EUR")
print(f"{n_keyboards:3d} keyboards ({keyboard_price:.2f} EUR each) = {keyboard_total:.2f} EUR")
print("-" * 50)
print(f"Total: {cable_total + monitor_total + keyboard_total:.2f} EUR")
print("=" * 50)
