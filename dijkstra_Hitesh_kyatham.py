import heapq as hq
import numpy as np
import cv2

class Graph:
    def __init__(self, start_index, goal_index):
        self.map = np.zeros((1200,500,3))
        self.map_Generator()
        cv2.imshow("",cv2.rotate(self.map, cv2.ROTATE_90_COUNTERCLOCKWISE))
        cv2.waitKey(0)
        if(self.check_Obstacle(start_index) or self.check_Obstacle(goal_index)):
          raise Exception("Start or Goal indices are in Obstacle space.")
        self.graph = {tuple(start_index): [-1,-1]}
        fps = 30
        frame_shape = cv2.rotate(self.map, cv2.ROTATE_90_COUNTERCLOCKWISE).shape
        print(frame_shape)
        self.out = cv2.VideoWriter('hkyatham_661.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_shape[1], frame_shape[0]))
        # self.obstacle_indices
      
    def map_Generator(self):
      # Define conditions
      x = np.arange(1200).reshape((1200, 1))
      y = np.arange(500).reshape((1, 500))

      condition1 = (x < 5) | (y < 5) | (x > 1194) | (y > 494)
      condition2 = (x > 95) & (x < 180) & (y > 95)
      condition3 = (x > 270) & (x < 355) & (y < 405)
      condition4 = (x < 1105) & (x > 1015) & (y < 455) & (y > 45)
      condition5 = (x > 895) & (x <= 1015) & (y > 45) & (y < 130)
      condition6 = (x > 895) & (x <= 1015) & (y > 370) & (y < 455)
      condition7 = (
          ((y + (x / np.sqrt(3)) - 100 + (10/np.sqrt(3)) - (650 / np.sqrt(3))) > 0) &
          ((y - (x / np.sqrt(3)) - 400 - (10/np.sqrt(3)) + (650 / np.sqrt(3))) < 0) &
          ((y - (x / np.sqrt(3)) - 100 + (10/np.sqrt(3)) + (650 / np.sqrt(3))) > 0) &
          ((y + (x / np.sqrt(3)) - 400 - (10/np.sqrt(3)) - (650 / np.sqrt(3))) < 0) &
          (x > 650 - 5 - 75 * np.sqrt(3)) &
          (x < 650 + 5 + 75 * np.sqrt(3))
      )

      # condition8 = (x < 5) | (y < 5) | (x > 1194) | (y > 494)
      condition9 = (x > 100) & (x < 175) & (y > 100)
      condition10 = (x > 275) & (x < 350) & (y < 400)
      condition11 = (x < 1100) & (x > 1020) & (y < 450) & (y > 50)
      condition12 = (x > 900) & (x <= 1020) & (y > 50) & (y < 125)
      condition13 = (x > 900) & (x <= 1020) & (y > 375) & (y < 450)
      condition14 = (
          ((y + (x / np.sqrt(3)) - 100 - (650 / np.sqrt(3))) > 0) &
          ((y - (x / np.sqrt(3)) - 400 + (650 / np.sqrt(3))) < 0) &
          ((y - (x / np.sqrt(3)) - 100 + (650 / np.sqrt(3))) > 0) &
          ((y + (x / np.sqrt(3)) - 400 - (650 / np.sqrt(3))) < 0) &
          (x > 650 - 75 * np.sqrt(3)) &
          (x < 650 + 75 * np.sqrt(3))
      )

      # Combine all conditions
      final_condition = condition1 | condition2 | condition3 | condition4 | condition5 | condition6 | condition7
      self.obstacle_indices = np.vstack(np.where(final_condition == True)).T
      # Update values based on the combined condition
      # Replace with your desired value
      self.map[final_condition] = [0,0,255]
      self.map[condition9 | condition10 | condition11 | condition12 | condition13 | condition14] = [255,0,0]

    def check_Obstacle(self, index):
      return np.any(np.all(self.obstacle_indices == index, axis=1))
    
    def Up(self, current_position, cost):
      new_position = current_position.copy()
      new_position[1]+=1
    #   print(current_position)
      if(self.check_Obstacle(new_position)):
        # print("Inside up if")
        return (cost, current_position)
      else:
        # print("Inside up else")
        return (cost+1,new_position)
    
    def UpRight(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]+=1
      new_position[1]+=1
      
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1.4,new_position)
    
    def Right(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]+=1
      # new_position[1]+=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1,new_position)

    def DownRight(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]+=1
      new_position[1]-=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1.4,new_position)

    def Down(self, current_position, cost):
      new_position = current_position.copy()
      # new_position[0]-=1
      new_position[1]-=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1,new_position)

    def DownLeft(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]-=1
      new_position[1]-=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1.4,new_position)

    def Left(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]-=1
      # new_position[1]-=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1,new_position)

    def UpLeft(self, current_position, cost):
      new_position = current_position.copy()
      new_position[0]-=1
      new_position[1]+=1
      if(self.check_Obstacle(new_position)):
        return (cost, current_position)
      else:
        return (cost+1.4,new_position)

    def node_exists(self, index):
        return tuple(index) in self.graph
    
    def perform_action(self, index, cost, i):
        if(i == 0):
            return self.Up(index, cost)
        elif(i == 1):
            return self.UpRight(index, cost)
        elif(i == 2):
            return self.Right(index, cost)
        elif(i == 3):
            return self.DownRight(index, cost)
        elif(i == 4):
            return self.Down(index, cost)
        elif(i == 5):
            return self.DownLeft(index, cost)
        elif(i == 6):
            return self.Left(index, cost)
        else:
            return self.UpLeft(index, cost)

    def Dijstra(self, start_index, goal_index):

      queue = []
      d = [0 , start_index]
    #   print("Executed till here: 1")
      #print([index,0,initial_state])
      #new = pd.DataFrame(columns=self.nodeIndex.columns, data=[[index,0,initial_state]])
      # Overwrite original dataframe
      #self.nodeIndex = pd.concat([self.nodeIndex, new], axis=0)
      hq.heappush(queue, d)

      while len(queue):

        cost, index = hq.heappop(queue)
        self.map[index[0]][index[1]] = [0,255,0]
        if(index == goal_index):
            return 0

        # for i in range(4):
        # print("Executed till here: 2")
        for i in range(8):
            d = self.perform_action(index, cost, i)
            
            #print(new_state,i)
            if not self.node_exists(d[1]):
                self.graph[tuple(d[1])] = index
                if(d not in queue):
                    hq.heappush(queue, d)
            else:
                for i in queue:
                    if(i[1]==d[1]):
                        if(i[0]>d[0]):
                            queue[queue.index(i)] = d
                            self.graph[tuple(i[1])] = index
        hq.heapify(queue)
        # cv2.imshow("",cv2.rotate(self.map, cv2.ROTATE_90_COUNTERCLOCKWISE))
        # cv2.waitKey(0)
        self.out.write(cv2.rotate(self.map, cv2.ROTATE_90_COUNTERCLOCKWISE))
    
    def backTracking(self, goal_index):
        i = goal_index
        while (i != [-1,-1]):
            self.map[i[0]][i[1]] = [255, 255, 255]
            i = self.graph[tuple(i)]
        self.out.write(cv2.rotate(self.map, cv2.ROTATE_90_COUNTERCLOCKWISE))
            


if __name__ == '__main__':
    start_index = [10,10]
    goal_index = [200,50]
    g = Graph(start_index,goal_index)
    g.Dijstra(start_index,goal_index)
    g.backTracking(goal_index)
    g.out.release()
    cv2.imshow("Shortest_Path",cv2.rotate(g.map, cv2.ROTATE_90_COUNTERCLOCKWISE))
    cv2.waitKey(0)
    # Create VideoWriter object for output video
    cv2.destroyAllWindows()