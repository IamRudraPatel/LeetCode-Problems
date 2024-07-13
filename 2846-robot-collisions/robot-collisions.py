class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        index = {}
        for i in range(n):
            index[positions[i]] = i
        positions.sort()
        recentRobot = []
        for robot in positions:
            while (recentRobot) and (healths[index[robot]]!=0) and (directions[index[recentRobot[-1]]]=='R') and (directions[index[robot]]=='L'):
                health1, health2 = healths[index[recentRobot[-1]]], healths[index[robot]]
                if health1 == health2:
                    healths[index[recentRobot.pop()]] = 0
                    healths[index[robot]] = 0
                elif health1 > health2:
                    healths[index[recentRobot[-1]]] -= 1
                    healths[index[robot]] = 0
                else: 
                    healths[index[recentRobot.pop()]] = 0
                    healths[index[robot]] -= 1
            if (healths[index[robot]]!=0): 
                recentRobot.append(robot)
        answer = []
        for idx in index.values():
            health = healths[idx]
            if health != 0:
                answer.append(health)
        return answer