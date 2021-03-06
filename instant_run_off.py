# COMP 202 A3
# Name: Spencer Beatty
# ID: 260898452

from single_winner import *

################################################################################

def votes_needed_to_win(ballots, num_winners):
    '''
    (list) -> int
    takes a ballot form of votes, counts the total number of votes and divides it by
    number of winners +1, it rounds that number down to the nearest unit and then
    adds one more.
    >>> votes_needed_to_win([{'cpc': 3, 'ndp': 5,}, {'ndp': 3, 'green': 5}, {'cpc': 2, 'ndp': 5}], 1)
    2

    >>> votes_needed_to_win(['g']*20, 2)
    7

    >>> h = ['green0', 'green2', 'orange2']
    >>> r = ['orange1', 'blue3', 'cyan3']
    >>> votes_needed_to_win([h]*10 + [r]*5, 3)
    4

    >>> votes_needed_to_win([{'cpc': 3, 'ndp': 5,}, {'ndp': 3, 'green': 5}, {'ndp': 3, 'green': 5}, {'cpc': 2, 'ndp': 5}], 1)
    3

    >>> votes_needed_to_win([{'cpc': 3}], 1)
    1
    '''
    # creates a length based on how many votes have been cast.
    ballot_length = (len(ballots))

    # if the ballot divided by the number of winners is an integer then the
    # votes needed to win are calculated based on the formula ballot_length/ (num_winners+1)
    # and then 1 is added however if it is not an integer only 0.5 is added and then at the
    # end it is rounded down to an int.
    if type(ballot_length % (num_winners + 1)) == int:
        needed_to_win = ballot_length/(num_winners + 1) + 1
    else:
        needed_to_win = (ballot_length/(num_winners + 1)) + 0.5

    return int(needed_to_win)

def has_votes_needed(result, votes_needed):
    '''
    (dict) -> bool
    given a dictionary decide if the party with the most votes has enough votes to win
    the election and return a bool

    >>> has_votes_needed({'ndp': 4, 'liberal': 3, 'green': 2}, 4)
    True
    >>> has_votes_needed({'ndp': 2, 'liberal': 5}, 5)
    True
    >>> has_votes_needed({'ndp': 3, 'liberal': 4}, 5)
    False
    >>> has_votes_needed({'ndp': 3, 'liberal': 3}, 3)
    True
    >>> has_votes_needed({'GREEN1': 5, 'NDP1': 3, 'GREEN2': 0, 'NDP2': 0, 'NDP3': 0, 'BLOC1': 0}, 2)
    True
    >>> has_votes_needed({}, 1)
    False
    '''
    # checks to make sure the result is not empty, then iterates through the elements of result
    # and checks if any of the options have enough votes if they do the function returns True,
    # if not the function returns False.
    if len(result) == 0:
        return False
    for i in result:
        if result[i] >= votes_needed:
            return True
        
    return False


################################################################################


def eliminate_candidate(ballots, to_eliminate):
    '''
    (list) -> list
    given a list of ballots and a list of candidates to eliminate returns a list
    that has only the candidates not deemed to be eliminated.

    >>> eliminate_candidate([['ndp', 'liberal'], ['green', 'ndp'], ['ndp', 'bloc']], ['liberal', 'ndp'])
    [[], ['green'], ['bloc']]

    >>> eliminate_candidate([['ndp', 'liberal'], ['green', 'bloc'], ['ndp', 'green']], ['liberal', 'ndp', 'green', 'bloc'])
    [[], [], []]

    >>> eliminate_candidate([['ndp', 'liberal'], ['green', 'bloc'], ['ndp', 'green']], ['green'])
    [['ndp', 'liberal'], ['bloc'], ['ndp']]

    >>> eliminate_candidate([['GREEN3', 'NDP2', 'NDP3', 'BLOC1'], ['NDP2', 'NDP3', 'BLOC1', 'NDP3']], ['BLOC1'])
    [['GREEN3', 'NDP2', 'NDP3'], ['NDP2', 'NDP3', 'NDP3']]

    >>> eliminate_candidate([['green']], ['blue'])
    [['green']]

    >>> b = [['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]
    >>> eliminate_candidate(b, ['LIBERAL', 'NDP'])
    [[], ['GREEN'], ['BLOC']]
    >>> b
    [['NDP', 'LIBERAL'], ['GREEN', 'NDP'], ['NDP', 'BLOC']]
    '''
    # creates final_list
    final_list = []
    # creates an empty list, takes the ballots input and recreates it as a new list as to not
    # change the initial input. 
    for i in ballots:
        s = []
        for j in i:
            s.append(j)
        final_list.append(s)
    
    # Then it iterates through the values in the list to_eliminate,
    # if a value in to_eliminate is equal to an element in the final list it removes it, until
    # there are no more terms in the to_eliminate list.
    for h in to_eliminate:
        for i in final_list:
            for j in i:
                if h == j:
                   i.remove(j)
    return final_list

################################################################################


def count_irv(ballots):
    '''
    (list) -> dict
    given a list of ranked ballots eliminates non winners and returns votes based
    on the other rankings put in the ballot. Returns a dictionary of results.

    >>> pr_dict(count_irv([['ndp'], ['green', 'ndp', 'bloc'], ['liberal', 'ndp'], ['liberal'], ['ndp', 'green'], ['bloc', 'green', 'ndp'], ['bloc', 'cpc'], ['liberal', 'green'], ['ndp']]))
    {'bloc': 0, 'cpc': 0, 'green': 0, 'liberal': 3, 'ndp': 5}

    >>> random.seed(0)
    >>> pr_dict(count_irv([['ndp'], ['ndp', 'green'], ['green', 'ndp'], ['green']]))
    {'green': 0, 'ndp': 3}

    >>> random.seed(1)
    >>> pr_dict(count_irv([['ndp'], ['ndp', 'green'], ['green', 'ndp'], ['green']]))
    {'green': 3, 'ndp': 0}
    '''

    t = []
    votes_needed = votes_needed_to_win(ballots, 1)
    # given a list of ranked ballots takes the single winners from those ballots

    first_choices = count_first_choices(ballots)
    # if there is a winner decided break, if not continue
    
    while (not has_votes_needed(first_choices, votes_needed)):
        
    #finds who to eliminate then turns to_eliminate into a list
        to_eliminate = (last_place(first_choices))
        t.append(to_eliminate)
    #eliminates them and sets ballots to the new value
        result = eliminate_candidate(ballots, t)
        first_choices = count_first_choices(result)

    for i in t:
        first_choices[i] = 0

    
    
    return first_choices

################################################################################

if __name__ == '__main__':
    doctest.testmod()
