def football(match1, match2, home):
    G1, G2 = map(int, match1.split(':'))
    G3, G4 = map(int, match2.split(':'))

    first_team = G1 + G3
    second_team = G2 + G4

    if first_team > second_team:
        return 0

    elif first_team == second_team:
        if home == 1:
            return 1
        else:
            return 0


    else:
        goals_to_win = second_team - first_team

        if home == 1:
            return goals_to_win
        else:
            return goals_to_win + 1

match1 = input()
match2 = input()
home = int(input())

print(football(match1, match2, home))
