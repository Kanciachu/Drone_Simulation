import pygame


class Ui:
    def __init__(self, position, win, station, city_builder):
        self.position = position
        self.width = 400
        self.height = 1000
        self.rect = self.get_rect()
        self.win = win
        self.station = station
        self.city_builder = city_builder
        self.font = pygame.font.Font("Roboto-Light.ttf", 18)

    def draw(self):
        pygame.draw.rect(self.win, (0, 0, 0), self.rect)
        pygame.draw.rect(self.win, (255, 255, 255), self.rect, 2)
        self.first_section()
        self.second_section()
        self.third_section()

    def get_rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def first_section(self):
        rect = pygame.Rect(self.position.x, self.position.y, 200, 50)
        pygame.draw.rect(self.win, (255, 255, 255), rect, 2)
        text = self.font.render(f"BUILDINGS : {len(self.city_builder.buildings_show)}", True, (255, 255, 255))
        self.win.blit(text, (self.position.x, self.position.y))

        rect = pygame.Rect(self.position.x + 200, self.position.y, 200, 50)
        pygame.draw.rect(self.win, (255, 255, 255), rect, 2)
        text = self.font.render(f"ORDERS : {len(self.station.orders)}", True, (255, 255, 255))
        self.win.blit(text, (self.position.x + 200, self.position.y))

        rect = pygame.Rect(self.position.x, self.position.y + 50, 200, 50)
        pygame.draw.rect(self.win, (255, 255, 255), rect, 2)
        text = self.font.render(f"DRONES : {len(self.station.drones)}", True, (255, 255, 255))
        self.win.blit(text, (self.position.x, self.position.y + 50))

        rect = pygame.Rect(self.position.x + 200, self.position.y + 50, 200, 50)
        pygame.draw.rect(self.win, (255, 255, 255), rect, 2,)

    def second_section(self):

        a = 1000
        b = 100
        temp = 0
        for x in range(4):
            for y in range(4):
                rect = pygame.Rect(a, b, 100, 100)
                pygame.draw.rect(self.win, (255, 255, 255), rect, 2)

                text = self.font.render(f"{self.station.drones[temp].unit_name}", True, (250, 250, 250))
                text2 = self.font.render(f"{self.station.drones[temp].state}", True, (255, 255, 255))

                self.win.blit(text, (a + 5, b + 5))
                self.win.blit(text2, (a + 20, b + 40))

                temp += 1

                b += 100
            b = 100
            a += 100

    def third_section(self):

        b = 500

        for order in self.station.orders[:10]:
            rect = pygame.Rect(1000, b, 400, 50)
            pygame.draw.rect(self.win, (255, 255, 255), rect, 2)

            text = self.font.render(f"{order.display_order()}", True, (250, 250, 250))
            self.win.blit(text, (1020, b + 5))

            b += 50
