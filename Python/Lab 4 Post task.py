# Simple Reflex Agent
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
    

class Simple_Reflex_Agent:
    def __init__(self, room):
        self.room = room

    def perceive_temp(self):
        return self.room.get_temp()
    
    def read_theromostat(self):
        return self.room.get_thermostat()
    
    def adjust_thermostat(self, value = 0):
        if(value is not 0):
            self.room.set_thermostat(value)
            return
        
        current_temperature = self.perceive_temp()
        thermostat_setting = self.read_theromostat()

        if(current_temperature > 25):
            self.room.set_thermostat(thermostat_setting - 1)
        elif(current_temperature < 20):
            self.room.set_thermostat(thermostat_setting + 1)


    def simulate(self, minutes=10):
        print("\n\nSimulation for Simple Reflex Agent started for", minutes, "minutes")
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
Agent1 = Simple_Reflex_Agent(livingRoom)
Agent1.simulate()



# Model Based Agent
class Model_Based_Agent(Simple_Reflex_Agent):
    def __init__(self, room):
        super().__init__(room)
        self.model = {}  # Initialize an empty model
        
    def update_model(self, perception, action):
        self.model[perception] = action
    
    def decide_action(self, perception):
        if perception in self.model:
            return self.model[perception]
        else:
            return "No action found in model"
    
    def perceive_and_act(self):
        perception = self.perceive_temp()
        action = self.decide_action(perception)
        return action
    
    def simulate(self, minutes=10):
        print("\n\nSimulation for Model Based Agent started for", minutes, "minutes")
        for i in range(minutes):  # 10 iterations of the simulation in terms of minutes
            print("\ntime passed in minutes: ", i)
            current_room_temp = self.room.get_temp()
            current_thermostat_setting = self.room.get_thermostat()
            print("\t", self.room.name, ": Current temperature: ", current_room_temp)
            print("\t", self.room.name, ": Thermostat setting: ", current_thermostat_setting)

            action = self.perceive_and_act()
            print("\tAction taken based on perception:", action)

            if action == "increase":
                self.adjust_thermostat(current_thermostat_setting + 1) # based on knowledge, the model is increasing the thermostat setting
                self.room.update_temp(current_room_temp + 1)
            elif action == "decrease":
                self.adjust_thermostat(current_thermostat_setting - 1) # based on knowledge, the model is decreasing the thermostat setting
                self.room.update_temp(current_room_temp - 1)
            elif action == "maintain":
                pass
            else:
                print("\tApplying Simple Reflex Agent Rules")
                self.adjust_thermostat()
                current_thermostat_setting = self.room.get_thermostat()

                if(current_room_temp > current_thermostat_setting):
                    self.room.update_temp(current_room_temp - 1)
                    self.update_model(current_room_temp, "decrease")
                elif(current_room_temp < current_thermostat_setting):
                    self.room.update_temp(current_room_temp + 1)
                    self.update_model(current_room_temp, "increase")
                else:
                    self.update_model(current_room_temp, "maintain")
            

bedRoom = Room("bed room", 18)
Agent2 = Model_Based_Agent(bedRoom)
Agent2.simulate()
diningRoom = Room("dining room", 18)
Agent2.room = diningRoom
Agent2.simulate()
