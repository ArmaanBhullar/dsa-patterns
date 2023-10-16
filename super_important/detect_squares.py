"""
https://leetcode.com/problems/detect-squares/description/
"""
class DetectSquares:
    from collections import defaultdict
    def __init__(self):
        self.points = []  # point_id to coords
        self.x_points_map = defaultdict(list)  # x coord -> point_id ls
        self.y_points_map = defaultdict(list)  # y coor -> point_id ls
        self.points_rev = defaultdict(list)  # coords to point_id list
        self.num_points = 0

    def add(self, point: List[int]) -> None:
        self.points.append((point[0], point[1]))
        self.x_points_map[point[0]].append(self.num_points)
        self.y_points_map[point[1]].append(self.num_points)
        self.points_rev[(point[0], point[1])].append(self.num_points)
        self.num_points += 1

    def get_fourth_point(self, ls) -> Tuple[int]:
        final_point_x, final_point_y = set(), set()
        for x_, y_ in ls:
            if x_ in final_point_x:
                final_point_x.remove(x_)
            else:
                final_point_x.add(x_)
            if y_ in final_point_y:
                final_point_y.remove(y_)
            else:
                final_point_y.add(y_)
        x_can, y_can = list(final_point_x)[0], list(final_point_y)[0]
        return (x_can, y_can)

    def count(self, point: List[int]) -> int:
        x, y = point
        count = 0
        # print(self.points)
        for idx in range(len(self.points)):
            point = self.points[idx]
            x_dist = abs(point[0] - x)
            y_dist = abs(point[1] - y)
            if x_dist == y_dist and x_dist > 0:
                point_1 = (x, point[1])
                point_2 = (point[0], y)
                if point_1 in self.points_rev and point_2 in self.points_rev:
                    count += len(self.points_rev[point_1]) * len(self.points_rev[point_2])
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)