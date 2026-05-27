from counter import Counter

c = Counter("OK", 10)
print("No problem")
c = Counter("Not OK", -5) # Should report ValueError
