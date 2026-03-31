# The Set-Covering Problem

# Sets
station_needed = set(["mt","wa","or","id","nv","ut","ca","ca"])

# Hash Map for States & Stations
stations = {}
stations["K1"] = set(["id","nv","ut"])
stations["K2"] = set(["wa","id","mt"])
stations["K3"] = set(["or","nv","ca"])
stations["K4"] = set(["nv",'ut'])
stations["K5"] = set(["ca","az"])

# Final Stations
final_stations = set()


while station_needed:
    best_station = None
    states_covered = set()
    for station,state in stations.items():
        covered = station_needed & state
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    station_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)