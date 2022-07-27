from Drony import Dron
from Position import Position
from random import randint
from Building import CityBuilder, Station
import pygame
pygame.init()

WIDTH, HEIGHT = 1000,1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drones Simulation")
FONT = pygame.font.SysFont("comicsans", 10)
stations = []


def main():
    run = True
    clock = pygame.time.Clock()
    city_builder = CityBuilder()

    station = Station(f"station", Position(randint(0, 1000), randint(0, 1000), 0), 20)
    stations.append(station)
    station.create_drone(10)
    city_builder.build_city(500, stations)
    while run:
        clock.tick(60)
        if city_builder.buildings:
            city_builder.transport_next()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for building in city_builder.buildings_show:
            building.draw(WIN, FONT)



        for drone in station.drones:
            drone.draw(WIN)

        pygame.display.update()
    pygame.quit()

main()