# World Class
#
# Stores the map in a useful way,
# keeps track of cell info, loads
# new maps from files, and answers
# questions about the map.
#
# 2014/3/21
# written by Michael Shawn Redmond

from config import *
import rectangle
import pygame
import os

class World:
    def __init__(self, position, width, height, layout_file=None):
        self.position = position
        self.width = self.safe_assign("Width", width, int, WORLD_DEFAULT_WIDTH)
        self.height = self.safe_assign("Height", height, int, WORLD_DEFAULT_HEIGHT)
        self.cell_width = TILE_WIDTH
        self.cell_height = TILE_HEIGHT
        self.tower_locations = []
        self.layout = []
        self.tile_types = []
        self.start_cell = None
        if layout_file is not None:
            self.load_from_file(layout_file)
            
    # attempts to assign a variable called var_name (for debugging)
    # to a value of value but assigns it to value: default
    # if the original type cannot be casted into desired_type
    def safe_assign(self, var_name, value, desired_type, default):
        if type(desired_type) != type(type(int)):
            print "Desired_type was not a valid type"
            print "Defaulting to type(str)"
            desired_type = str
        if type(value) != desired_type:
            print str(var_name) + " expected to be " + str(desired_type)
            print "Attempting Cast..."
            try:
                value = desired_type(value)
            except:
                print "Unable to convert ", type(value), " to type " + str(desired_type)
                print "Defaulting to", default
                value = default
            print "Type-cast completed"
        return value

    # attempts to open the world file and store the information
    # does nothing if the file was invalid in any way
    def load_from_file(self, layout_file):
        if not os.path.exists(layout_file):
            print "Error loading world file " + layout_file + ": File was not found."
            print "File will not be loaded"
            return
        f = open(layout_file, 'rb')
        fin = [line.strip() for line in f.readlines()]
        f.close()
        data = fin[0].split()
        dim = [0, 0]
        try:
            dim[0] = int(data[0])
            dim[1] = int(data[1])
            if len(data) != 4:
                raise Exception("Invalid layout description\n" + str(dim))
            self.start_cell = (int(data[2]), int(data[3]))
            layout = []
            fin = fin[1:]
            for line in fin:
                if len(line) != dim[0]:
                    raise Exception("Invalid/Mismatched width\n" + str(line))
                else:
                    layout.append(line)
            if len(layout) != dim[1]:
                l = ""
                for i in layout:
                    l += i + '\n'
                l = l.strip()
                raise Exception("Invalid/Mismatched height\n" + l)
        except Exception, e:
            print "Error loading world file " + layout_file + ": Invalid formatting"
            print e
            return False
        row_size = self.width/self.cell_width
        col_size = self.height/self.cell_height
        filled_rows = int(dim[0])
        filled_cols = int(dim[1])
        empty_rows = row_size - filled_rows
        empty_cols = col_size - filled_cols
        for i in range(len(layout)):
            fill = empty_rows*'0'
            layout[i] = layout[i] + fill
        for i in range(empty_cols):
            fill = row_size*'0'
            layout.append(fill)
        self.layout = []
        for j in range(len(layout)):
            r_row = []
            t_row = []
            t_locations = []
            for i in range(len(layout[j])):
                tile = layout[j][i]
                if tile == '0':
                    img = GRASS_IMG
                else:
                    img = PATH_IMG
                x = self.position[0] + (i)*self.cell_width
                y = self.position[1] + (j)*self.cell_height
                t_row.append(int(tile))
                
                # tower location default to 0
                t_locations.append(0)
                
                r_row.append(rectangle.Rectangle((x, y), self.cell_width, self.cell_height, img))
            self.layout.append(r_row)
            self.tile_types.append(t_row)
            self.tower_locations.append(t_locations)
        return True
        
    def next_path_from(self, position, prev=None):
        current = self.get_cell_at(position)
        if prev is not None:
            previous = self.get_cell_at(prev)
        candidates = []
        
        has_top = self.has_cell(self.get_cell_at((position[0], position[1]-1)))
        has_left = self.has_cell(self.get_cell_at((position[0]-1, position[1])))
        has_right = self.has_cell(self.get_cell_at((position[0]+1, position[1])))
        has_bottom = self.has_cell(self.get_cell_at((position[0], position[1]+1)))
        if has_top:
            # topleft
            can = 
            # top
            # topright
        # left
        # right
        # bottomleft
        # bottom
        # bottomright

    def paint(self, surface):
        for row in self.layout:
            for cell in row:
                cell.paint(surface)

    def get_cell_at(self, position):
        for j in range(len(self.layout)):
            for i in range(len(self.layout[0])):
                if self.layout[j][i].is_inside(position):
                    return self.loc_to_cell(i, j)
        return None
        
    def get_start(self):
        return self.loc_to_cell(self.start_cell[0], self.start_cell[1])

    def loc_to_cell(self, i, j):
        # where i is the column, j is the row
        return j*(self.width/self.cell_width) + i

    def cell_to_loc(self, cell_num):
        i = cell_num%(self.width/self.cell_width)
        j = cell_num/(self.width/self.cell_width)
        return i, j

    def get_cell_top_left(self, cell_num):
        i, j = self.cell_to_loc(cell_num)
        return self.layout[j][i].get_position()
        
    def get_cell_center(self, cell_num):
        i, j = self.cell_to_loc(cell_num)
        return self.layout[j][i].get_center()

    def cell_is_path(self, cell_num):
        i, j = self.cell_to_loc(cell_num)
        return self.tile_types[j][i] == 1
        
    def occupy_cell(self, cell_num):
        i, j = self.cell_to_loc(cell_num)
        self.tower_locations[j][i] = 1
    
    def occupy_area(self, pos, dims):
        x_span = dims[0] / self.cell_width
        y_span = dims[1] / self.cell_height
        for i in range(x_span):
            for j in range(y_span):
                p = (pos[0] + i*self.cell_width, pos[1] + j*self.cell_height)
                cell_num = self.get_cell_at(p)
                self.occupy_cell(cell_num)
    
    def has_cell(self, cell_num):
        if cell_num is None or cell_num >= (self.width/self.cell_width)*(self.height/self.cell_height):
            return False
        return True
    
    def is_occupied(self, cell_num):
        i, j = self.cell_to_loc(cell_num)
        return self.tower_locations[j][i] == 1

    def can_build(self, pos, dims):
        # assumes that the object's size is a whole amount of tiles
        x_span = dims[0] / self.cell_width
        y_span = dims[1] / self.cell_height
        for i in range(x_span):
            for j in range(y_span):
                p = (pos[0] + i*self.cell_width, pos[1] + j*self.cell_height)
                cell_num = self.get_cell_at(p)
                if not self.has_cell(cell_num) or self.cell_is_path(cell_num) or self.is_occupied(cell_num):
                    return False
        return True

    def is_inside(self, position):
        if position[0] >= self.position[0] and position[0] < self.position[0] + self.width:
            if position[1] >= self.position[1] and position[1] < self.position[1] + self.height:
                return True
        return False

    def __str__(self):
        board = ""
        for row in self.layout:
            line = ""
            for cell in row:
                line += str(cell)
            board += line + '\n'
        return board
