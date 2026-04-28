import numpy as np
from collections import Counter

# -------- INPUT --------
input_value = int(input("Enter the input value: "))
direction_value = int(input("Enter the direction number: "))


# ---------------- LOAD TIME ----------------
t = np.load(f"Direction{direction_value}_yearly_module0_block_data_time_{2000 + input_value}.npy")

tmin = np.min(t)
tmax = np.max(t)


# -------- LOAD EDGES --------
all_edges = []

for l in range(16):
    fname = f"Direction{direction_value}_yearly_module_block_{2000 + input_value}_{l}.npy"
    x = np.load(fname)
    all_edges.extend(x)

all_edges = np.array(all_edges)

#-------- STEP 1: COUNT --------
counts = Counter(all_edges)

# -------- STEP 2: REMOVE VALUES APPEARING 16 TIMES --------
filtered = [val for val in all_edges if counts[val] < 16]

# remove duplicates + sort
filtered = np.array(sorted(set(filtered)))

print("After removing common edges:")
print(filtered)

# -------- STEP 3: 30-DAY MERGING --------
window = 30.0
merged = []

for val in filtered:
    if not merged or (val - merged[-1]) >= window:
        merged.append(val)

merged = np.array(merged)

print("\nFinal merged edges:")
print(merged)

# ---------------- STEP 3: EDGE CORRECTION (NOW HERE) ----------------
bin_width = 0.125
merged = merged - (bin_width / 2.0)   # subtract 0.0625

print("\nAfter edge correction (centers):")
print(merged)
# ---------------- STEP 4: BOUNDARY CONDITION ----------------
final_data = []

for val in merged:
    if tmin + window <= val <= tmax - window:
        final_data.append(val)

# always include last boundary
if len(final_data) == 0 or final_data[-1] != tmax:
    final_data.append(tmax)

final_data = np.array(final_data)

print("\nFinal merged edges:")
print(final_data)

# -------- SAVE --------
np.save(f"Direction{direction_value}_yearly_Window_raw_{2000+input_value}",final_data)
