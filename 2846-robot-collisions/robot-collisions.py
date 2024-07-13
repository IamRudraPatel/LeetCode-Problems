class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        n = len(positions)
        index = {robot: i for i, robot in enumerate(positions)}
        positions.sort()
        recentRobot = []
        for robot in positions:
            i = index[robot]
            if directions[i]=='R':
                recentRobot.append(i)
            else: 
                while (recentRobot) and (healths[i]!=0) and (directions[recentRobot[-1]]=='R'):
                    health1, health2 = healths[recentRobot[-1]], healths[i]
                    if health1 == health2:
                        healths[recentRobot.pop()] = 0
                        healths[i] = 0
                    elif health1 > health2:
                        healths[recentRobot[-1]] -= 1
                        healths[i] = 0
                    else: 
                        healths[recentRobot.pop()] = 0
                        healths[i] -= 1
                if healths[i]: 
                    recentRobot.append(i)
        return [h for h in healths if h>0]