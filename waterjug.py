print("Water Jug Problem Using Production Rules")
print("State = (Jug1, Jug2)")

state = (0, 0)
print("Initial State:", state)

# Rule 1: Fill Jug2
if state == (0, 0):
    print("Rule: Fill Jug2")
    state = (0, 3)
    print(state)

# Rule 2: Pour Jug2 into Jug1
if state == (0, 3):
    print("Rule: Pour Jug2 into Jug1")
    state = (3, 0)
    print(state)

# Rule 3: Fill Jug2 again
if state == (3, 0):
    print("Rule: Fill Jug2 Again")
    state = (3, 3)
    print(state)

# Rule 4: Pour Jug2 into Jug1 until full
if state == (3, 3):
    print("Rule: Pour Jug2 into Jug1")
    state = (4, 2)
    print(state)

# Goal State
if state == (4, 2):
    print("Goal Achieved")