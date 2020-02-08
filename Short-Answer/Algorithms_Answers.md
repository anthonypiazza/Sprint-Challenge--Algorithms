#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear - O(n) -> Worst case scenario: the while loop will always run n times before satisfying the stop condition


b) Linear Log - O(nlog(n)) -> Worst case scenario: the for loop runs n times so it is linear, and then within that for loop the while loop runs but because j is multiplied, the loops decrease and take up log(n) time


c) Constant - O(1) -> Worst case scenario: despite the recurion, all the operations are done in constant time

## Exercise II

def dropped_eggs(stories, egg_break_level):
    eggs = 3
    ok_to_toss_levels = []
    for story in stories:
        if story < egg_break_level:
            ok_to_toss_levels.append(story)
        elif story >= egg_break_level:
            print(f"Floor: {story} is too high to drop eggs from")


Runtime Complexity - O(n) -> generally we would expect it to run a few times less than the total number of inputs but in a worst case scenario the entire building would be ok to toss an egg off of so the function would run n times -- meaning it is linear.
