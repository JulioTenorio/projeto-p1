def move(self):
    # Define o próximo waypoint como alvo
    if self.target_waypoint < len(self.waypoints):
        self.target = Vector2(self.waypoints[self.target_waypoint])
        self.movement = self.target - self.pos
    else:
        # O inimigo chegou ao final do caminho
        self.kill()

    # Calcula a distância até o alvo
    dist = self.movement.length()
    # Verifica se a distância restante é maior ou igual à velocidade do inimigo
    if dist >= self.speed:
        self.pos += self.movement.normalize() * self.speed
    else:
        if dist != 0:
            self.pos += self.movement.normalize() * dist
        self.target_waypoint += 1
