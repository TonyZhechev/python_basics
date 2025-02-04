import pygame
import math

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CENTER = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
HEX_RADIUS = 200
BALL_RADIUS = 10
GRAVITY = 0.5
FRICTION = 0.99
WALL_FRICTION = 0.1
COR = 0.8
ANGULAR_VELOCITY = 0.05

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0.0
        self.vy = 0.0

class Hexagon:
    def __init__(self, radius, center):
        self.radius = radius
        self.center = center
        self.angle = 0.0

    def get_vertices(self):
        return [(self.center[0] + self.radius * math.cos(self.angle + i * math.pi/3),
                 self.center[1] + self.radius * math.sin(self.angle + i * math.pi/3))
                for i in range(6)]

def closest_point_on_segment(A, B, C):
    ax, ay = A
    bx, by = B
    cx, cy = C
    abx, aby = bx - ax, by - ay
    t = ((cx - ax) * abx + (cy - ay) * aby) / (abx**2 + aby**2 + 1e-8)
    t = max(0, min(1, t))
    return (ax + t * abx, ay + t * aby)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

ball = Ball(CENTER[0], CENTER[1] - HEX_RADIUS + BALL_RADIUS + 5)
hexagon = Hexagon(HEX_RADIUS, CENTER)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hexagon.angle = (hexagon.angle + ANGULAR_VELOCITY) % (2 * math.pi)
    ball.vy += GRAVITY
    ball.vx *= FRICTION
    ball.vy *= FRICTION
    ball.x += ball.vx
    ball.y += ball.vy

    vertices = hexagon.get_vertices()
    for i in range(6):
        A, B = vertices[i], vertices[(i+1)%6]
        P = closest_point_on_segment(A, B, (ball.x, ball.y))
        dx, dy = ball.x - P[0], ball.y - P[1]
        distance = math.hypot(dx, dy)

        if distance < BALL_RADIUS:
            midpoint = ((A[0]+B[0])/2, (A[1]+B[1])/2)
            normal_x, normal_y = hexagon.center[0]-midpoint[0], hexagon.center[1]-midpoint[1]
            length = math.hypot(normal_x, normal_y)
            if length == 0:
                continue
            normal_x, normal_y = normal_x/length, normal_y/length

            # Wall velocity at collision point
            vw_x = -ANGULAR_VELOCITY * (P[1]-hexagon.center[1])
            vw_y = ANGULAR_VELOCITY * (P[0]-hexagon.center[0])

            # Relative velocity
            rel_vx = ball.vx - vw_x
            rel_vy = ball.vy - vw_y

            dp = rel_vx * normal_x + rel_vy * normal_y
            if dp < 0:
                # Collision response
                nc_x = dp * normal_x
                nc_y = dp * normal_y
                tc_x = rel_vx - nc_x
                tc_y = rel_vy - nc_y

                new_nc_x = -COR * nc_x
                new_nc_y = -COR * nc_y
                new_tc_x = tc_x * (1 - WALL_FRICTION)
                new_tc_y = tc_y * (1 - WALL_FRICTION)

                ball.vx = vw_x + new_nc_x + new_tc_x
                ball.vy = vw_y + new_nc_y + new_tc_y

                # Reposition ball
                penetration = BALL_RADIUS - distance
                ball.x += normal_x * penetration
                ball.y += normal_y * penetration

    screen.fill(WHITE)
    pygame.draw.polygon(screen, BLUE, vertices, 2)
    pygame.draw.circle(screen, RED, (int(ball.x), int(ball.y)), BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()