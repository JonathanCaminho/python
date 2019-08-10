motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)
too_expensive = motorcycles[3]
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for Book author.")