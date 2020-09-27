import random
import math
import time
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)
        # Create friendships
        # you could create a list with all possible friendship combinations
        possible_friendships = []
        for user1 in self.users:
            for user2 in self.users:
                if (user1, user2) not in possible_friendships and (user2, user1) not in possible_friendships and user1 != user2:
                    possible_friendships.append((user1, user2))
        random.shuffle(possible_friendships)
        # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
        # shuffle the list
        # then grab the first N elements from the list

        total_friendships = num_users * avg_friendships
        for i in range(math.ceil(total_friendships/2)):
            self.add_friendship(possible_friendships[i][0], possible_friendships[i][1])

    # pick two random uer_ids
    # try to make them friends
    ## track number of friendships made
    # stop at required amount
    def linear_populate_graph(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(i)

        total_friendships = num_users * avg_friendships
        total_friends = 0
        while total_friends < total_friendships:
            friend_1 = random.randint(1, num_users)
            friend_2 = random.randint(1, num_users)
            friendship_made = self.add_friendship(friend_1, friend_2)
            if friendship_made:
                total_friends += 1

    def get_all_social_paths(self, user_id):
        """, visited = {}):
        
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Note that this is a dictionary, not a set
        visited = {}
        # !!!! IMPLEMENT ME

        queue = []
        queue.insert(0, [user_id])
        while len(queue) > 0:
            cur_path = queue.pop()
            cur_user = cur_path[-1]
            if cur_user not in visited:
                visited[cur_user] = cur_path
                friends = self.friendships[cur_user]
                for friend in friends:
                    path_copy = list(cur_path)
                    path_copy.append(friend)
                    queue.insert(0, path_copy)
        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populate_graph(10, 2)
    end_time = time.time()
    print(end_time-start_time)
    start_time = time.time()
    sg.linear_populate_graph(100000, 5)
    end_time = time.time()
    print(end_time-start_time)
    # print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
