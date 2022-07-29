from Position import Position
from random import randint
from Building import CityBuilder, Station
from Ui import Ui

import pygame
pygame.init()

WIDTH, HEIGHT = 1400, 1000
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drones Simulation")
FONT = pygame.font.SysFont("comicsans", 10)
STATIONS = []
ORDERS = []


def main():
    run = True
    clock = pygame.time.Clock()
    city_builder = CityBuilder()

    station = Station(f"station", Position(randint(0, 1000), randint(0, 1000), 0))
    STATIONS.append(station)
    station.create_drone("MAX")
    city_builder.build_city(20, STATIONS)
    time_elapsed = 0
    unfinished_orders = 0
    ui = Ui(Position(1000, 0, 0), WIN, station, city_builder)
    while run:
        time = clock.tick(60)
        if city_builder.buildings:
            city_builder.transport_next()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for building in city_builder.buildings_show:
            building.draw(WIN, FONT)

        for drone in station.drones:
            drone.draw(WIN)

        ui.draw()

        time_elapsed += time

        if city_builder.orders:
            station.add_order(city_builder.orders.pop(0))

        if time_elapsed > 1000:
            if unfinished_orders <= 10:
                city_builder.generate_orders(1)
                unfinished_orders += 1
            time_elapsed = 0

        if time_elapsed > 990:
            print(f"city builder:{len(city_builder.orders)}")
            print(f"station :{len(station.orders)}")

        pygame.display.update()
    pygame.quit()


main()
