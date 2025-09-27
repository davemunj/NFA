

#define NFA
state_outcome = ['no','no','yes']
nfa = [[[0,1],[0]],[[], [2]], [[2],[]]]
#nfa= []
#for sublist in nfa_list:
#    nfa = nfa.append(set(sublist))
nfa_null = [[2,0]]
alphabet = 'ab'
test_input = 'aaaabbbba'
curr_state = [0]
new_state = curr_state.copy()
#null transition from start
for item in nfa_null:
    if item[0] == 0:
        new_state.append(item[1])
curr_state = new_state.copy()
print(f"States before 1st input are {new_state}")

for i in range(len(test_input)):
    # input transition
    new_state = []
    column = alphabet.find(test_input[i])
    for temp_state in curr_state:
        next_state = set(nfa[temp_state][column])
        new_state = list( set(new_state) |next_state)

    #null transitions
    for temp_state in new_state:
        for item in nfa_null:
            if item[0] == temp_state:
                new_state.append(item[1])
    new_state = list(set(new_state))
    print(f"States before {i + 2} _th input are {new_state}")

    if len(new_state) == 0:
        print(f"reject input on input {i}")
        break
    else:curr_state = new_state.copy()

#check for accept state
print(f"Possible states are {curr_state}")

outcome = "reject"
for temp_state in curr_state:
    if state_outcome[temp_state] == 'yes':
        outcome = "accept"
        break
print(outcome)



# filename = "C:\\Users\\davem\\OneDrive\\Documents\\Programming\\Python\\DFA\\NFA_1.txt"
# with open(filename, 'r') as f:
#     num_states = int(f.readline().strip())
#     state_outcome = f.readline().split()
#     alphabet = f.readline().strip()
#     #dfa = []
#     for i in range(num_states):
#         dfa.append(f.readline().split())
#     dfa = [list( map(int,j) ) for j in dfa]
#     #dfa = list(map(int ,dfa))
#
#
# input = "abbbbabaa"
#
# state = 0
# for i in range(len(input)):
#     column = int(alphabet.find(input[i]) );
#     state = dfa[state][column];
# print(state_outcome[state])
#


#solve NFA
## determine possible state transitions
