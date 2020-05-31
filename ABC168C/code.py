import math

def main():
  A,B,H,M = list(map(int, input().split()))

  angle_per_hour = 360 / 12
  angle_per_minute = 360 / 60

  angle_hour_hand = math.radians(H * angle_per_hour + M * (angle_per_hour / 60))
  angle_minute_hand = math.radians(M * angle_per_minute)

  hour_x = A * math.cos(angle_hour_hand)
  hour_y = A * math.sin(angle_hour_hand)
  minute_x = B * math.cos(angle_minute_hand)
  minute_y = B * math.sin(angle_minute_hand)

  dx = hour_x - minute_x
  dy = hour_y - minute_y

  print(math.sqrt(dx ** 2 + dy ** 2))


if __name__ == "__main__":
  main()