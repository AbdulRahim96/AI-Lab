class Room:
    def __init__(self, name, initial_temp):
        self.name = name
        self.temp = initial_temp
        self.thermostat = initial_temp
    
    def update_temp(self, val):
        self.temp = val

    def get_temp(self):
        return self.temp
    
    def set_thermostat(self, val):
        self.thermostat = val

    def get_thermostat(self):
        return self.thermostat
    

class agent:
    def __init__(self, room):
        self.room = room

    def perceive_temp(self):
        return self.room.get_temp()
    
    def read_theromostat(self):
        return self.room.get_thermostat()
    
    def adjust_thermostat(self):
        current_temperature = self.perceive_temp()
        thermostat_setting = self.read_theromostat()

        if(current_temperature > 25):
            self.room.set_thermostat(thermostat_setting - 1)
        elif(current_temperature < 20):
            self.room.set_thermostat(thermostat_setting + 1)


    def simulate(self, minutes=10):
        print("\n\nSimulation started for", minutes, "minutes")
        for i in range(minutes): # 10 iterations of the simulation in terms of minutes
            print("\ntime passed in minutes: ", i)
            current_room_temp = self.room.get_temp()
            current_thermostat_setting = self.room.get_thermostat()
            print("\t", self.room.name, ": Current temperature: ", current_room_temp)
            print("\t", self.room.name, ": Thermostat setting: ", current_thermostat_setting)

            self.adjust_thermostat()

            if(current_room_temp > current_thermostat_setting):
                self.room.update_temp(current_room_temp - 1)
            elif(current_room_temp < current_thermostat_setting):
                self.room.update_temp(current_room_temp + 1)

livingRoom = Room("living room", 18)
Agent1 = agent(livingRoom)
Agent1.simulate()

bedRoom = Room("bed room", 29)
Agent2 = agent(bedRoom)
Agent2.simulate(13)



