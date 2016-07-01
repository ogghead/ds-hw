
from csv import DictReader, DictWriter

kHEADER = ["STATE", "DISTRICT", "DEM", "REP", "OTH"]

def total_districts(state, lines):
    total = []

    # Complete this function

    return total

if __name__ == "__main__":
    lines = list(DictReader(open("data/2014_election_results.csv")))
    output = DictWriter(open("district_totals.csv", 'w'), fieldnames=kHEADER)
    output.writeheader()

    for state in set(x["STATE"] for x in lines):
        total = total_districts(state, [x for x in lines if x["STATE"]==state])

        for ii in total:
            output.writerow(ii)
