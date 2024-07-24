def read_input(filename):
    """
    Reads the input file and extracts the number of users (U), number of movies (M), and
    the preferences of each user.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    U, M = map(int, lines[0].strip().split())  # Read number of users and movies
    preferences = []

    for line in lines[1:]:
        parts = list(map(int, line.strip().split()))
        user_id = parts[0]  # User ID
        ranking = parts[1:]  # User's movie ranking
        preferences.append((user_id, ranking))

    return U, M, preferences

def count_inversions(arr):
    """
    Counts the number of inversions in the array using a simple O(n^2) approach.
    """
    inversions = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def user_preference_distance(preferences, x):
    """
    Computes the distance (in terms of inversions) between user x's preferences and all
    other users' preferences.
    """
    user_x = preferences[x - 1][1]  # Get preferences of user x
    distances = []

    for user_id, user_pref in preferences:
        if user_id == x:
            continue

        # Create the array A based on user x and the current user
        A = [0] * len(user_x)
        for idx, movie in enumerate(user_x):
            position_in_user_pref = user_pref.index(movie)
            A[idx] = position_in_user_pref + 1  # Positions are 1-based

        # Count inversions in array A
        num_inversions = count_inversions(A)
        distances.append((user_id, num_inversions))

    return distances

def main(input_file, x):
    """
    Main function to read input, compute distances, and print the results.
    """
    U, M, preferences = read_input(input_file)
    distances = user_preference_distance(preferences, x)

    for user_id, num_inversions in distances:
        print(f"User {user_id} has {num_inversions} inversions compared to user {x}")

# Example usage:
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/test_5_5.txt', 1)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/test_5_10.txt', 1)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/test_10_5.txt', 1)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/test_50_100.txt', 1)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/test_100_50.txt', 1)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/input_1000_5.txt', 100)
#print("")
#main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/input_1000_5.txt', 29)
#print("")
main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/input_1000_100.txt', 1)
#print("")
main('/Users/anastasiiatrofymova/projects/sigma-internship/algorithms-kpi/input_1000_100.txt', 178)