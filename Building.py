from math import floor
from random import randint
from Drony import Dron
from Position import Position
from Order import Order

import pygame.draw


class Building:

    """Building is a class representing simple building with it inhabitants. Buildings will occasionally
    decide to order a packages.

     This class is extremely messy and needs a lot of rework"""

    def __init__(self, unit_name, position, width, height):
        self.unit_name = unit_name
        self.position = position
        self.width = width
        self.height = height
        self.top = self.position.x - self.width / 2
        self.left = self.position.y - self.height / 2
        self.bottom = self.position.x + self.width / 2
        self.right = self.position.y + self.height / 2
        self.people = floor(width ** 2 / 5)
        self.rect = pygame.Rect(self.top, self.left, self.width, self.height)

    def draw(self, win, font):

        """This function will draw rectangles representing buildings
        there is posibility of drawing number of building alongside with it by
        decommenting code"""

        pygame.draw.rect(win, (255,255,255), self.rect, 2)
        #text = font.render(f"{self.unit_name}", 1, (255,255,255))
        #win.blit(text, (self.position.x, self.position.y))


class CityBuilder:

    """ City Builder is a class that builds structure of the city. It's main purpose it to create
     buildings that don't overlap. It has 2 list buildings and buildings to show. Buildings
     to show is a list which will progressively by populated with buildings from buildings list"""

    def __init__(self):
        self.buildings = []
        self.buildings_show = []

    def build_city(self, number, stations):

        """Function Build_city will create buildings in number specified with [ number - int ] parameter
        the buildings will not overlap.

        functions will check if currently generated building overlaps another one it will be discarded
        and a new one will be generated"""

        for station in stations:
            self.buildings.append(station)

        while len(self.buildings) != number:

            # Generate random building
            width_height = randint(10, 100)
            position_temp = Position(randint(0, 1000), randint(0, 1000), 0)
            top = position_temp.x - width_height / 2
            left = position_temp.y - width_height / 2
            bottom = position_temp.x + width_height / 2
            right = position_temp.y + width_height / 2

            # Set flag as True
            flag = True

            # Compare created building to other in list
            for building in self.buildings:

                # If buildings don't overlap continue
                if (building.top >= bottom
                        or building.bottom <= top
                        or building.right <= left
                        or building.left >= right):
                    continue

                # If buildings overlap
                else:
                    flag = False
                    break

            # If building not overlap append it to buildings array
            if flag or len(self.buildings) == 0:
                print(f"Building created. Current amount {len(self.buildings)}")
                self.buildings.append(Building(f"{len(self.buildings)}",
                                                position_temp,
                                                width_height,
                                                width_height))

    def transport_next(self):

        """ FOR VISUALIZATION PURPOSE - functions transports building from one list to another"""

        self.buildings_show.append(self.buildings.pop(0))

    def show_buildings(self):

        """Displays information about building created and number of buildings created so far"""

        for building in self.buildings:
            print(f"{building.unit_name} : {building.position.x} , {building.position.x}")


class Station:
    def __init__(self, unit_name, position, capacity):

        """Station is a class representing docking station for drones
        station takes orders from clients. After receiving order it will
        assign drone to complete given task

        Station takes 3 argument:
            - Unit_name - name of the station
            - Position  - position of the station
            - Capacity  - maximum number of drones that can be operated by station"""

        self.unit_name = unit_name
        self.next_unit_name = 0
        self.position = position
        self.capacity = capacity
        self.width = 40
        self.height = 40
        self.top = self.position.x - self.width / 2
        self.left = self.position.y - self.height / 2
        self.bottom = self.position.x + self.width / 2
        self.right = self.position.y + self.height / 2
        self.people = floor(self.width ** 2 / 5)
        self.rect = pygame.Rect(self.top, self.left, self.width, self.height)
        self.landing_sectors = self.generate_landing_sectors()
        self.range = None
        self.drones = []
        self.orders = []

    def start(self):

        """ Starts a station """

        #        HOW SHOULD IT WORK
        # 1. STATION STARTS
        # 2. IT CREATES MAXIMUM NUMBER OF DRONES / OR IT WAITS FOR ORDER
        #

        self.create_drone(20)

    def draw(self, win, FONT):

        """This function will draw rectangle representing station
        there is posibility of drawing number of building alongside with it by
        decommenting code"""

        pygame.draw.rect(win, (0, 0, 255), self.rect, 2)
        #text = FONT.render(f"{self.unit_name}", 1, (255,255,255))
        #win.blit(text, (self.position.x, self.position.y))

    def add_order(self, order):

        """ Receives and adds order to order queue """

        self.orders.append(order)

    def create_drone(self, amount = 1):

        """ Creates drone and adds it to drones list"""

        if len(self.drones) >= self.capacity:
            print("Maximum Drone Capacity Reached")
        else:
            for x in range(amount):
                landing_sector = self.landing_sectors.pop(0)
                self.drones.append(Dron(f"Dron_{self.next_unit_name}",
                                        landing_sector,
                                        self.unit_name,
                                        self.position,
                                        landing_sector))

            self.next_unit_name += 1
            print(f"STATION {self.unit_name}: {amount} drones created".upper())

    def drone_decommission(self, drone_index):
        self.landing_sectors.append(self.drones[drone_index].landing_sector)

    def generate_landing_sectors(self):
        list_ = []
        for y in range(5, self.width, 10):
            for x in range(5, self.height, 10):
                list_.append(Position(self.top + x, self.left + y, 0))
        return list_

    def create_orders(self, amount):

        """ Creates orders in number specified by [ amount - int ] parameter """

        for x in range(amount):
            self.add_order(Order(Position(randint(0,200),
                                          randint(0,200),
                                          randint(0,200),),
                                        randint(1,20),))

    def show_orders(self):

        """ Displays current orders """

        for order in self.orders:
            order.display_order()
