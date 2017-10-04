import copy
import collections


class State:

    def __init__(self, missi_left, carni_left,
                 missi_right, carni_right, boat_pos, path_taken):
        self.missi_left = missi_left
        self.carni_left = carni_left
        self.missi_right = missi_right
        self.carni_right = carni_right
        self.boat_pos = boat_pos
        self.path_taken = path_taken

    def is_success(self):
        # Success if all have been moved to right side
        if (self.missi_left == 0 and self.carni_left == 0 and self.missi_right > 0 and self.carni_right > 0):
            return True
        else:
            return False

    def valid_state(self):
        # Check for missi's being outnumbered
        if (self.missi_left > 0 and self.missi_left < self.carni_left):
            return False
        if (self.missi_right > 0 and self.missi_right < self.carni_right):
            return False
        if (self.missi_right < 0 or self.missi_left < 0 or self.carni_right < 0 or self.carni_left < 0):
            return False

        return True

    def __eq__(self, other):
        if(self.missi_left == other.missi_left and self.missi_right == other.missi_right
           and self.carni_left == other.carni_left and self.carni_right == other.carni_right
           and self.boat_pos == other.boat_pos):
            return True
        return False

    def print_state(self):
        print("Left: " + str(self.missi_left) + "M , " + str(self.carni_left) +
              "C\nRight: " + str(self.missi_right) + "M , " +
              str(self.carni_right) + "C"
              + " boat pos: " + self.boat_pos + "\n")

    def to_string(self):
        state_def = str("Left: " + str(self.missi_left) + "M , " + str(self.carni_left) +
                        "C\nRight: " + str(self.missi_right) +
                        "M , " + str(self.carni_right) + "C"
                        + " boat pos: " + self.boat_pos + "\n")
        return state_def

    def print_path(self):
        for nodes in self.path_taken:
            print(nodes.to_string())
        return None


def move_one(cur_state, who):
    # Updates the path taken
    cur_state.path_taken.append(cur_state)
    if cur_state.boat_pos == "left":
        if who == "missi":
            new_state = State(cur_state.missi_left - 1, cur_state.carni_left,
                              cur_state.missi_right + 1, cur_state.carni_right,
                              "right", cur_state.path_taken)
            print("Sent 1M right")
        else:
            new_state = State(cur_state.missi_left, cur_state.carni_left - 1,
                              cur_state.missi_right, cur_state.carni_right + 1,
                              "right", cur_state.path_taken)
            print("Sent 1C right")
    else:
        if who == "missi":
            new_state = State(cur_state.missi_left + 1, cur_state.carni_left,
                              cur_state.missi_right - 1, cur_state.carni_right,
                              "left", cur_state.path_taken)
            print("Sent 1M left")
        else:
            new_state = State(cur_state.missi_left, cur_state.carni_left + 1,
                              cur_state.missi_right, cur_state.carni_right - 1,
                              "left", cur_state.path_taken)
            print("Sent 1C left")
    return new_state


def move_two(cur_state, who1, who2):
    # Updates the path taken
    cur_state.path_taken.append(cur_state)
    new_boat_pos = ""
    sent = [0, 0]
    if cur_state.boat_pos == "left":
        new_boat_pos = "right"
        if who1 == "missi":
            new_state = State(cur_state.missi_left - 1, cur_state.carni_left,
                              cur_state.missi_right + 1, cur_state.carni_right,
                              new_boat_pos, cur_state.path_taken)
            sent[0] += 1
        else:
            new_state = State(cur_state.missi_left, cur_state.carni_left - 1,
                              cur_state.missi_right, cur_state.carni_right + 1,
                              new_boat_pos, cur_state.path_taken)
            sent[1] += 1

        if who2 == "missi":
            new_state = State(new_state.missi_left - 1, new_state.carni_left,
                              new_state.missi_right + 1, new_state.carni_right,
                              new_boat_pos, cur_state.path_taken)
            sent[0] += 1
        else:
            new_state = State(new_state.missi_left, new_state.carni_left - 1,
                              new_state.missi_right, new_state.carni_right + 1,
                              new_boat_pos, cur_state.path_taken)
            sent[1] += 1
    else:
        new_boat_pos = "left"
        if who1 == "missi":
            new_state = State(cur_state.missi_left + 1, cur_state.carni_left,
                              cur_state.missi_right - 1, cur_state.carni_right,
                              new_boat_pos, cur_state.path_taken)
            sent[0] += 1
        else:
            new_state = State(cur_state.missi_left, cur_state.carni_left + 1,
                              cur_state.missi_right, cur_state.carni_right - 1,
                              new_boat_pos, cur_state.path_taken)
            sent[1] += 1

        if who2 == "missi":
            new_state = State(new_state.missi_left + 1, new_state.carni_left,
                              new_state.missi_right - 1, new_state.carni_right,
                              new_boat_pos, cur_state.path_taken)
            sent[0] += 1
        else:
            new_state = State(new_state.missi_left, new_state.carni_left + 1,
                              new_state.missi_right, new_state.carni_right - 1,
                              new_boat_pos, cur_state.path_taken)
            sent[1] += 1

    print("Sent " + str(sent[0]) + "M , " +
          str(sent[1]) + "C - " + new_boat_pos)

    return new_state


def solve(cur_state, explored):
    # Moving when unable. need to make sure there are people there to move
    if cur_state.is_success():
        # No need to explore further the conditions are met
        cur_state.path_taken.append(cur_state)
        return cur_state

    cur_state.print_state()

    if not cur_state.valid_state() or cur_state in explored:
        # If the state isn't valid (invalid move) then move up a level.
        return None

    explored.append(cur_state)

    # Will return the success state with the path on success
    # Returns nothing on failure
    branch1 = solve(move_one(copy.deepcopy(cur_state),
                             "missi"), copy.deepcopy(explored))
    branch2 = solve(move_one(copy.deepcopy(cur_state),
                             "carni"), copy.deepcopy(explored))
    branch3 = solve(move_two(copy.deepcopy(cur_state),
                             "missi", "missi"), copy.deepcopy(explored))
    branch4 = solve(move_two(copy.deepcopy(cur_state),
                             "missi", "carni"), copy.deepcopy(explored))
    branch5 = solve(move_two(copy.deepcopy(cur_state),
                             "carni", "carni"), copy.deepcopy(explored))

    paths = [branch1, branch2, branch3, branch4, branch5]
    good_paths = []
    for path in paths:
        if path is not None:
            # If it is the success node create an inital good path list
            if type(path) is not list:
                good_paths.append(path)
            else:
                # If it isn't the initial success node, append to good path list
                for p in path:
                    good_paths.append(p)

    # If there are no good paths then it cannot be solved. return None
    if len(good_paths) == 0:
        return None

    return good_paths


def main():
    initial_state = State(3, 3, 0, 0, "left", [])
    explored = []
    print("Solving . . . \n")
    results = solve(initial_state, explored)

    count = 1
    for res in results:
        print("\nSolution #" + str(count) +
              ":\n----------------------------------")
        res.print_path()
        count += 1


if __name__ == "__main__":
    main()
