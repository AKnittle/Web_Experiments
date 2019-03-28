"""Prototype of game"""

#import pygame

"""Class used to describe points in 2D space"""


class GeoPoint:

    def __init__(self, x_coord, y_coord, data=None):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.data = data

    # Returns Coordinates as a tuple (x, y)
    def get_coords(self):
        coords = (self.x_coord, self.y_coord)
        return coords

    def print_point(self):
        x = str(self.x_coord)
        y = str(self.y_coord)
        point = "(" + x + ", " + y + ")"
        if self.data is not None:
            point = point + " Value: " + str(self.data)
        print(point)


"""Using GeoPoints to describe a shape with n number of nodes"""


class Shape:
    """
    point_list: List of points with no duplicates
    edge_list: List of edges between points in point_list with no duplicates
    tag_back: When False it means edges can not be bidirectional and must be one way (ie. A ---> B)
    """

    def __init__(self, point_list=None, edge_list=None, tag_back=False):
        self.point_list = point_list
        self.edge_list = edge_list
        self.tag_back = tag_back

    # Adds point to point_list
    def add_point(self, point, connect_last_point=False):
        if self.point_list is None:
            self.point_list = [point]
            return True
        else:
            if point in self.point_list:
                # Point is already in point_list
                # TODO: Add check for deep comparison: x, y, and data
                print("Point already exists")
                return False
            if connect_last_point:
                # Get Last Point added to point_list
                last_point = self.point_list[len(self.point_list) - 1]
                edge = (last_point, point)
                # Add new edge and point to their respective lists
                if self.edge_list is None:
                    self.edge_list = [edge]
                else:
                    self.edge_list.append(edge)
                self.point_list.append(point)
            else:
                # Add new Point to point_list
                self.point_list.append(point)
            return True

    # Adds edge from already existing points in point_list
    def add_edge(self, point_a, point_b):
        if point_a not in self.point_list and point_b not in self.point_list:
            # One or Both points are missing within point_list
            print("Ensure both points have already been added")
            return False
        edge = (point_a, point_b)
        if edge not in self.edge_list:
            # No A -> B
            if not self.tag_back:
                # No "tag backs" in affect. Ensure no edge already exists in the other direction (ie. A <->B)
                rev_edge = (point_b, point_a)
                if rev_edge not in self.edge_list:
                    # No edge A <- B exists
                    self.edge_list.append(edge)
                    return True
                else:
                    # Edge A <- B DOES exist
                    print("No 'Tag-Backs' in affect. Can not create bidirectional edges.")
                    return False
            # "tag backs" not in affect. New edge MAY be a bidirectional edge
            self.edge_list.append(edge)
            return True
        print("Edge already exists")
        return False

    # Draws shape by creating a list of points connected by edges.
    def draw_shape(self):
        connected_edges = []
        for edge in self.edge_list:
            point_a = edge[0]
            point_b = edge[1]
            coords_a = point_a.get_coords()
            coords_b = point_b.get_coords()
            edge = (coords_a, coords_b)
            connected_edges.append(edge)
        return connected_edges


def main():
    #pygame.init()
    sample_points = [(1, 1), (2, 0)]
    sample_shape = Shape()
    point = GeoPoint(0, 0)
    sample_shape.add_point(point)
    for i in sample_points:
        point = GeoPoint(i[0], i[1])
        sample_shape.add_point(point, True)
    print(sample_shape.draw_shape())


if __name__ == "__main__":
    main()
