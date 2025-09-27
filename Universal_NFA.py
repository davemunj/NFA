class Universal_NFA:
    def __init__(self,filename):
        # read in NFA specification
        with open(filename, 'r') as f:
            descript = f.readline().strip()
            if descript == "Number of states":
                self.num_states = int(f.readline().strip())
            descript = f.readline().strip()
            if descript == "State outcomes":
                self.state_outcome = f.readline().strip().split()
            descript = f.readline().strip()
            if descript == "Alphabet":
                self.alphabet = f.readline().strip()

            descript = f.readline().strip()
            if descript == "Null transitions":
                null_transition_temp = f.readline().strip().split()
                self.null_transition = []
                for item in null_transition_temp:
                    item = list(item.split("|"))
                    self.null_transition.append(item)
                self.null_transition = [list(map(int, j)) for j in self.null_transition]

            descript = f.readline().strip()
            if descript == "Transitions":
                nfa_temp = []
                self.nfa = []
                for i in range(self.num_states):
                    nfa_temp.append(f.readline().split())
                for sublist in nfa_temp:
                    temp_sublist = []
                    for entry in sublist:
                        temp_entry = []
                        if "|" in entry:
                            temp_entry =  list(map(int, entry.split("|")) )
                        elif entry == 'e':
                            temp_entry = []
                        else:
                            temp_entry.append(int(entry))
                        temp_sublist.append(temp_entry)
                    self.nfa.append(temp_sublist)
                   # print("test")

    def simulate(self, test_input):
        curr_state = [0]
        new_state = curr_state.copy()

        # null transition from start
        for temp_state in new_state:
            for item in self.null_transition:
                if item[0] ==  temp_state:
                    if item[1] not in new_state:
                        new_state.append(item[1])
        new_state = list(set(new_state))
        curr_state = new_state.copy()
        print(f"States before 1st input are {new_state}")
        outcome = 'undecided'

        for i in range(len(test_input)):
            # transition based on input
            new_state = []
            column = self.alphabet.find(test_input[i])
            for temp_state in curr_state:
                next_state = set(self.nfa[temp_state][column])
                new_state = list(set(new_state) | next_state)

            # null transitions
            for temp_state in new_state:
                for item in self.null_transition:
                    if item[0] == temp_state:
                        if item[1] not in new_state:
                          new_state.append(item[1])
            new_state = list(set(new_state))
            print(f"States before {i + 2} _th input are {new_state}")

            if len(new_state) == 0:
                print(f"reject input on input {i+1}")
                curr_state = []
                outcome = "reject"
                break
            else:
                curr_state = new_state.copy()

        # check for accept state
        print(f"Possible states are {curr_state}")

        if outcome == "undecided":
            for temp_state in curr_state:
                if self.state_outcome[temp_state] == 'yes':
                    outcome = "accept"
                    break
                else:
                    outcome = "reject"
        print(outcome)

filename = "C:\\Users\\davem\\OneDrive\\Documents\\Programming\\Python\\NFA\\NFA_2.txt"
nfa = Universal_NFA(filename)
nfa.simulate("baaaabaaa")



