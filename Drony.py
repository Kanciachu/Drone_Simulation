import Position
import pygame.draw


class Dron:
    def __init__(self, unit_name, unit_position, home_station, home_station_position, landing_sector):

        """ Drone is a class representing transport unit of a small drone. Drones
        are created by stations to which they are assigned

        Drone takes 4 arguments:
            - Unit_name - name of the drone unit
            - Unit_position - position of the drone
            - Home_station - primary station of drone
            - Home_station_position - position of primary station

        Drone fulfills tasks given by the station

        Later in development drones should have partially intelligent behavior deciding
        on next tasks by themselves

        Drone have other variables which hold important information regarding drone state:
            - State - current state of drone it tells us if drone is idle, currently occupied
            or returning to mother station
            - Charge - of onboard battery
            - Load - currently carried packages
            - Destination - current destination off the drone
            - Tasks - current tasks of the drone """

        self.unit_name = unit_name
        self.state = "IDLE"
        self.position = unit_position
        self.charge = 100.00
        self.load = []
        self.home_station = home_station
        self.home_station_position = home_station_position
        self.landing_sector = landing_sector
        self.destination = None
        self.tasks = []

    def start(self):

        """ Starts the operation loop which governs behavior of drone  """

        if self.tasks:
            task = self.tasks.pop(0)
            print(task)

    def task_delivery(self, destination, load):

        """ Creates delivery task for the drone and adds it to tasks queue """

        task = {
            "task" : "DELIVERY",
            "destination" : destination,
            "load" : load
        }
        self.add_task(task)
        self.task_return()

    def task_return(self):

        """ Creates return task for the drone and adds it to tasks queue """

        task = {
            "task" : "RETURN",
            "destination" : self.home_station_position,
        }
        self.add_task(task)

    def add_task(self, formated_task):

        """ Adds a task to task queue """

        self.tasks.append(formated_task)

    def draw(self, win):
        pygame.draw.circle(win,(255, 0, 0),(self.position.x, self.position.y), 5, 3)

    def show_tasks(self):

        """ Displays current tasks of the drone """

        print(f"{self.unit_name.upper()} :")
        for index, task in enumerate(self.tasks):
            print(f"TASK {index}:  {task['task']} to {task['destination'].display()}")