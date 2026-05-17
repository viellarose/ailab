print("State = (MonkeyPos, BoxPos, OnBox, HasBanana)")

# Initial State
state = ('A', 'C', False, False)
print("Initial State:", state)

# Rule 1: Monkey moves to box
if state == ('A', 'C', False, False):
    state = ('C', 'C', False, False)
    print(state)

# Rule 2: Monkey pushes box to banana
if state == ('C', 'C', False, False):
    state = ('B', 'B', False, False)
    print(state)

# Rule 3: Monkey climbs box
if state == ('B', 'B', False, False):
    state = ('B', 'B', True, False)
    print(state)

# Rule 4: Monkey gets banana
if state == ('B', 'B', True, False):
    state = ('B', 'B', True, True)
    print(state)

# Goal Check
if state == ('B', 'B', True, True):
    print("Goal achieved")