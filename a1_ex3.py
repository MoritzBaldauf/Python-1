length = float(input("Length (meters): "))
width = float(input("Width (meters): "))
height = float(input("Height (meters): "))

print(f"Circumference: {2 * length + 2 * width:.2f} meters")
print(f"Volume: {length * width * height:.2f} cubic meters")
wall_area = 2 * length * height + 2 * width * height
print(f"Wall area: {wall_area:.2f} square meters")
n_windows = int(wall_area / 12)
print(f"Number of windows: {n_windows}")
window_area = 2 * n_windows
print(f"Needed paint: {(wall_area - window_area) * 0.75:.2f} liters")
