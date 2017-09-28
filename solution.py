class State:

     def __init__(self, missi_left, carni_left,
                missi_right, carni_right, boat_pos):
         self.missi_left = missi_left
         self.carni_left = carni_left
         self.missi_right = missi_right
         self.carni_right = carni_right
         self.boat_pos = boat_pos

    def is_success(self):
        #Success if all have been moved to right side
        if self.missi_left == 0 and self.carni_right == 0:
            return True
        else:
            return False

    def valid_state(self):
        #Check for missi's being outnumbered
        if self.missi_left > 0 and self.missi_left < self.carni_left:
            return False
        if self.missi_right > 0 and self.missi_right < self.carni_right:
            return False

        return True

def move_one(cur_state,who):
    new_boat_pos = ""

    if cur_state.boat_pos == "left":
        new_boat_pos = "right"
    else:
        new_boat_pos = "left"

    if who == "missi":
        new_state = State(cur_state.missi_left-1,cur_state.carni_left,
                            cur_state.missi_right+1,cur_state.carni_right,
                            new_boat_pos)
    else:
        new_state = State(cur_state.missi_left,cur_state.carni_left-1,
                            cur_state.missi_right,cur_state.carni_right+1,
                            new_boat_pos)
    return new_state

def move_two(cur_state,who1,who2):
    new_boat_pos = ""

    if cur_state.boat_pos == "left":
        new_boat_pos = "right"
    else:
        new_boat_pos = "left"

    if who1 == "missi":
        new_state = State(cur_state.missi_left-1,cur_state.carni_left,
                            cur_state.missi_right+1,cur_state.carni_right,
                            new_boat_pos)
    else:
        new_state = State(cur_state.missi_left,cur_state.carni_left-1,
                            cur_state.missi_right,cur_state.carni_right+1,
                            new_boat_pos)

    if who2 == "missi":
        new_state = State(cur_state.missi_left-1,cur_state.carni_left,
                            cur_state.missi_right+1,cur_state.carni_right,
                            new_boat_pos)
    else:
        new_state = State(cur_state.missi_left,cur_state.carni_left-1,
                            cur_state.missi_right,cur_state.carni_right+1,
                            new_boat_pos)

    return new_state

def dfs(cur_state):
    #Move 1M
    #Move 1C
    #Move two 2M
    #Move two 2C
    #Move 1M 1C

    return

def solve(initial_state):
    if initial_state.is_success():
        return initial_state
    dfs(inital_state)


    return count

def main():


    print("Hello")


if __name__ == "__main__":
    main()
