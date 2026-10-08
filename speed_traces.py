import matplotlib.pyplot as plt

ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(ver_tel["Distance"], ver_tel["Speed"], label="Verstappen")
ax.plot(ham_tel["Distance"], ham_tel["Speed"], label="Hamilton")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Speed (km/h)")
ax.legend()
plt.title("2024 British GP Qualifying – Fastest Lap Speed Comparison")
plt.savefig("speed_traces.png", dpi=150)
plt.show()