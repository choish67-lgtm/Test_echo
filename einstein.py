def main():
    mass = int(input("m: "))
    light_speed = 3 * pow(10,8) 
    LightSpeed_squared = squared(light_speed)
    print("E:", mass * LightSpeed_squared)

def squared(n):
    return n * n

if __name__ == "__main__":
    main()
