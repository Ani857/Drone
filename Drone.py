from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager
X = int(input("Enter height of drone in cm : "))
Y = int(input("Enter how far to fly in cm : "))
Z = int(input("Enter how many time to fly? : "))
if __name__ == '__main__':
    sim_key = '867b7926-79df-4cbf-9863-db2dae843a0d'
    distance == Y
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_up(x,'cm')
    while(Z>a):
        drone.fly_forward(distance, 'cm')
        drone.fly_backward(distance, 'cm')
        a=a+1
        drone.land()
    
from djitellopy import Tello
tello = Tello() 
tello.connect() 
tello.takeoff() 
tello.move_left(100) 
tello.rotate_counter_clockwise(90) 
tello.move_forward(100) 
tello.land()
