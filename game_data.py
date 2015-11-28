class Location:

    def __init__(self, name, points, brief, full, item = [] ):
        '''Creates a new location.          
        ADD NEW ATTRIBUTES TO THIS CLASS HERE TO STORE DATA FOR EACH LOCATION.
        
        Data that could be associated with each Location object:
        a position in the world map,
        a brief description,
        a long description,
        a list of available commands/directions to move,
        items that are available in the location,
        and whether or not the location has been visited before.
        Store these as you see fit.

        This is just a suggested starter class for Location.
        You may change/add parameters and the data available for each Location class as you see fit.
  
        The only thing you must NOT change is the name of this class: Location.
        All locations in your game MUST be represented as an instance of this class.
        '''
        self.name = name
        self.points = points
        self.brief = brief
        self.full = full
        self.item = item

    def get_brief_description (self):
        '''Return str brief description of location.'''
        return(self.brief)

    def get_full_description (self):
        '''Return str long description of location.'''
        return(self.full)

    def available_actions(self):
        '''
        -- Suggested Method (You may remove/modify/rename this as you like) --
        Return list of the available actions in this location.
        The list of actions should depend on the items available in the location
        and the x,y position of this location on the world map.'''

    def get_available_item(self):
        '''

        :return: The item located here, if there is one
        '''
        return(self.item)

class Item:

    def __init__ (self, start, target, target_points, name):
        '''Create item referred to by string name, with integer "start"
        being the integer identifying the item's starting location,
        the integer "target" being the item's target location, and
        integer target_points being the number of points player gets
        if item is deposited in target location.

        This is just a suggested starter class for Item.
        You may change these parameters and the data available for each Item class as you see fit.
        Consider every method in this Item class as a "suggested method":
                -- Suggested Method (You may remove/modify/rename these as you like) --

        The only thing you must NOT change is the name of this class: Item.
        All item objects in your game MUST be represented as an instance of this class.
        '''

        self.name = name
        self.start = start
        self.target = target
        self.target_points = target_points

    def get_starting_location (self):
        '''Return int location where item is first found.'''

        return(self.start)

    def get_name(self):
        '''Return the str name of the item.'''

        return(self.name)

    def get_target_location (self):
        '''Return item's int target location where it should be deposited.'''

        return(self.target)

    def get_target_points (self):
        '''Return int points awarded for depositing the item in its target location.'''

        return(self.target_points)

class World:

    def __init__(self, mapdata, locdata, itemdata):
        '''
        Creates a new World object, with a map, and data about every location and item in this game world.

        You may ADD parameters/attributes/methods to this class as you see fit.
        BUT DO NOT RENAME OR REMOVE ANY EXISTING METHODS/ATTRIBUTES.

        :param mapdata: name of text file containing map data in grid format (integers represent each location, separated by space)
                        map text file MUST be in this format.
                        E.g.
                        1 -1 3
                        4 5 6
                        Where each number represents a different location, and -1 represents an invalid, inaccessible space.
        :param locdata: name of text file containing location data (format left up to you)
        :param itemdata: name of text file containing item data (format left up to you)
        :return:
        '''
        self.map = self.load_map(mapdata) # The map MUST be stored in a nested list as described in the docstring for load_map() below
        # self.locations ... You may choose how to store location and item data.
        self.load_locations(locdata) # This data must be stored somewhere. Up to you how you choose to do it...
        self.load_items(itemdata) # This data must be stored somewhere. Up to you how you choose to do it...

    def load_map(self, filename):
        '''
        THIS FUNCTION MUST NOT BE RENAMED OR REMOVED.
        Store map from filename (map.txt) in the variable "self.map" as a nested list of strings OR integers like so:
            1 2 5
            3 -1 4
        becomes [['1','2','5'], ['3','-1','4']] OR [[1,2,5], [3,-1,4]]
        RETURN THIS NEW NESTED LIST.
        :param filename: string that gives name of text file in which map data is located
        :return: return nested list of strings/integers representing map of game world as specified above
        '''
        tempfile = open(filename)
        lines = tempfile.readlines()
        tempfile.close
        i=0
        b=0
        c=[]
        for line in lines:
            a = line.split()
            c.append(a)
        return(c)


    def load_locations(self, filename):
        '''
        Store all locations from filename (locations.txt) into the variable "self.locations"
        however you think is best.
        Remember to keep track of the integer number representing each location.
        Make sure the Location class is used to represent each location.
        Change this docstring as needed.
        :param filename:
        :return:
        '''

        tempfile = open(filename)
        lines = tempfile.readlines()
        tempfile.close
        i=0
        b=0
        c=[]
        d = []
        for line in lines:
            i += 1
            line = line.rstrip('\n')
            if line != '':
                d.append(line)
            if line == 'END':
                d = d[:len(d)-1]
                c.append(d)
                d=[]
        return(c)


    def load_items(self, filename):
        '''
        Store all items from filename (items.txt) into ... whatever you think is best.
        Make sure the Item class is used to represent each item.
        Change this docstring accordingly.
        :param filename:
        :return:
        '''

        tempfile = open("items.txt")
        lines = tempfile.readlines()
        tempfile.close
        i=0
        b=0
        c=[]
        d = []
        lines = lines[1:]
        for line in lines:
            a = line.split()
            c.append(a)
        return(c)

    def get_location(self, x, y):
        '''Check if location exists at location (x,y) in world map.
        Return Location object associated with this location if it does. Else, return None.
        Remember, locations represented by the number -1 on the map should return None.
        :param x: integer x representing x-coordinate of world map
        :param y: integer y representing y-coordinate of world map
        :return: Return Location object associated with this location if it does. Else, return None.
        '''

        map = self.map
        return map[y-1][x-1]

