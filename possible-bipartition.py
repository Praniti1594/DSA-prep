# https://leetcode.com/problems/possible-bipartition/
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        BLUE, GREEN = 1, -1
        dislike=defaultdict(list)
        for a,b in dislikes:
            dislike[a].append(b)
            dislike[b].append(a)

        color_of = {}

        for person in range(1, n+1):
            if person in color_of:
                continue

            color_of[person]= BLUE
            bfs_queue = deque([(person, BLUE)])

            while bfs_queue:

                cur, color= bfs_queue.popleft()
                for enemy in dislike[cur]:
                    if enemy not in color_of:
                        color_of[enemy]= -1*color
                        bfs_queue.append((enemy, color_of[enemy]))
                    elif color_of[enemy]==color:
                        return False
                
        return True




        
