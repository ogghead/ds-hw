from collections import defaultdict
from csv import DictReader, DictWriter
import heapq

kHEADER = ["STATE", "DISTRICT", "MARGIN"]

def district_margins(state_lines):
    """
    Return a dictionary with districts as keys, and the difference in
    percentage between the winner and the second-place as values.

    @lines The csv rows that correspond to the districts of a single state
    """

    # Complete this function
    percentages = defaultdict(list)
    distWinner, distSecond = 0.0, 0.0
    dist = -1
    for x in state_lines:
        if x["D"] and x["D"] != "H" and x['GENERAL %'] != '' and x['FEC ID#'] != 'n/a':
            if int(x['D'][:2]) != dist:
                dist = int(x['D'][:2])
                #print(dist)
                distWinner, distSecond = 0.0, 0.0

            temp = x['GENERAL %'].replace(',', '.')
            temp = temp.replace('%', '')
            newtemp = float(temp)
            #print(newtemp, distWinner, distSecond)
            if x['GE WINNER INDICATOR'] == 'W':
                distWinner = newtemp
                #print('yay')
            elif newtemp > distSecond:
                distSecond = newtemp
                #print('yay2')
            if dist != -1 and distWinner != 0.0:
                percentages[dist] = (distWinner-distSecond)

    return percentages

def all_states(lines):
    """
    Return all of the states (column "STATE") in list created from a
    CsvReader object.  Don't think too hard on this; it can be written
    in one line of Python.
    """

    # Complete this function
    return set(d['STATE'] for d in lines)

def all_state_rows(lines, state):
    """
    Given a list of output from DictReader, filter to the rows from a single state.

    @state Only return lines from this state
    @lines Only return lines from this larger list
    """

    for ii in lines:
        if ii['STATE'] == state:
            yield (ii)

if __name__ == "__main__":
    # You shouldn't need to modify this part of the code
    lines = list(DictReader(open("../data/2014_election_results.csv")))
    output = DictWriter(open("district_margins.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()

    summary = {}
    for state in all_states(lines):
        margins = district_margins(all_state_rows(lines, state))

        for ii in margins:
            summary[(state, ii)] = margins[ii]

    for ii, mm in sorted(summary.items(), key=lambda x: x[1]):
        output.writerow({"STATE": ii[0], "DISTRICT": ii[1], "MARGIN": mm})
