import os
import fastf1
import matplotlib.pyplot as plt

# 1. Set up the cache (saves downloaded data so it loads faster next time)
os.makedirs("cache", exist_ok=True)
fastf1.Cache.enable_cache("cache")

# 2. Load the 2024 British GP qualifying session
session = fastf1.get_session(2024, "Silverstone", "Q")
session.load()

# 3. Find each driver's fastest lap
ver_lap = session.laps.pick_drivers("VER").pick_fastest()
ham_lap = session.laps.pick_drivers("HAM").pick_fastest()

print("Verstappen fastest lap:", ver_lap["LapTime"])
print("Hamilton fastest lap:  ", ham_lap["LapTime"])

# 4. Get car telemetry and add distance along the lap
ver_tel = ver_lap.get_car_data().add_distance()
ham_tel = ham_lap.get_car_data().add_distance()

# 5. Plot speed against distance for both drivers
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(ver_tel["Distance"], ver_tel["Speed"], label="Verstappen")
ax.plot(ham_tel["Distance"], ham_tel["Speed"], label="Hamilton")
ax.set_xlabel("Distance (m)")
ax.set_ylabel("Speed (km/h)")
ax.legend()
plt.title("2024 British GP Qualifying – Fastest Lap Speed Comparison")
plt.savefig("speed_traces.png", dpi=150)
plt.show()