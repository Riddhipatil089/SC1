import numpy as np

# 1) MEMBERSHIP FUNCTIONS (Triangular)
def triangular(x, a, b, c):
    x = np.array(x)

    left = np.where((b - a) == 0, 0, (x - a) / (b - a))
    right = np.where((c - b) == 0, 0, (c - x) / (c - b))

    return np.maximum(np.minimum(left, right), 0)

# 2) FUZZIFICATION
def fuzzify_temperature(t):
    return {
        "COLD": triangular(t, 0, 10, 20),
        "WARM": triangular(t, 15, 25, 35),
        "HOT":  triangular(t, 30, 35, 40)
    }

def fuzzify_humidity(h):
    return {
        "LOW":  triangular(h, 0, 25, 50),
        "HIGH": triangular(h, 30, 45, 60)
    }

# 3) RULE BASE (Mamdani)
def evaluate_rules(temp_f, hum_f):
    return {
        "SLOW":  min(temp_f["COLD"], hum_f["LOW"]),
        "FAST":  max(temp_f["HOT"], hum_f["HIGH"]),
        "MEDIUM": temp_f["WARM"]
    }
# 4) OUTPUT MEMBERSHIP FUNCTIONS
def fan_mf_slow(x):    return triangular(x, 0, 0, 50)
def fan_mf_medium(x):  return triangular(x, 30, 50, 70)
def fan_mf_fast(x):    return triangular(x, 60, 100, 100)

# 5) DEFUZZIFICATION (Centroid)

def defuzzify(rules):
    x = np.linspace(0, 100, 500)

    slow_curve   = np.minimum(rules["SLOW"],   fan_mf_slow(x))
    medium_curve = np.minimum(rules["MEDIUM"], fan_mf_medium(x))
    fast_curve   = np.minimum(rules["FAST"],   fan_mf_fast(x))

    agg = np.maximum(np.maximum(slow_curve, medium_curve), fast_curve)

    num = np.sum(x * agg)
    den = np.sum(agg)

    return num / den if den != 0 else 0

# 6) EXECUTION

temperature = 32
humidity = 40

temp_f = fuzzify_temperature(temperature)
hum_f  = fuzzify_humidity(humidity)

rules = evaluate_rules(temp_f, hum_f)

fan_speed = defuzzify(rules)

print("Temperature:", temperature)
print("Humidity:", humidity)
print("Fan Speed Output:", round(fan_speed, 2))
