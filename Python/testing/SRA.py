import time

class Room:
    def __init__(self, initial_temperature=20):
        self.temperature = initial_temperature
        self.thermostat_setting = initial_temperature

    def update_temperature(self, new_temperature):
        self.temperature = new_temperature

    def get_temperature(self):
        return self.temperature

    def set_thermostat(self, new_setting):
        self.thermostat_setting = new_setting

    def get_thermostat(self):
        return self.thermostat_setting

class Agent:
    def __init__(self, room):
        self.room = room

    def perceive_temperature(self):
        return self.room.get_temperature()

    def adjust_thermostat(self):
        current_temperature = self.perceive_temperature()
        thermostat_setting = self.room.get_thermostat()

        if current_temperature > 25:
            self.room.set_thermostat(thermostat_setting - 1)
        elif current_temperature < 20:
            self.room.set_thermostat(thermostat_setting + 1)

def simulate(agent, room, duration=10):
    for i in range(duration):
        current_temperature = room.get_temperature()
        thermostat_setting = room.get_thermostat()

        print(f"Time: {i}, Temperature: {current_temperature}, Thermostat: {thermostat_setting}")

        agent.adjust_thermostat()

        # Simulate temperature change
        if current_temperature > thermostat_setting:
            room.update_temperature(current_temperature - 1)
        elif current_temperature < thermostat_setting:
            room.update_temperature(current_temperature + 1)

        time.sleep(1)

print("Simple reflex agent")
room = Room(29)
agent = Agent(room)

simulate(agent, room)

# Model Based Agent
class ModelBasedAgent:
    def __init__(self, room):
        self.room = room
        self.predicted_temperature = room.get_temperature()

    def perceive_temperature(self):
        return self.room.get_temperature()

    def predict_temperature(self):
        return self.predicted_temperature

    def adjust_thermostat(self):
        current_temperature = self.perceive_temperature()
        thermostat_setting = self.room.get_thermostat()

        if current_temperature > 25 or self.predicted_temperature > 25:
            self.room.set_thermostat(thermostat_setting - 1)
        elif current_temperature < 20 or self.predicted_temperature < 20:
            self.room.set_thermostat(thermostat_setting + 1)

    def update_model(self):
        current_temperature = self.perceive_temperature()
        thermostat_setting = self.room.get_thermostat()

        if current_temperature > thermostat_setting:
            self.predicted_temperature -= 1
        elif current_temperature < thermostat_setting:
            self.predicted_temperature += 1

def simulate(agent, room, duration=10):
    for i in range(duration):
        current_temperature = room.get_temperature()
        thermostat_setting = room.get_thermostat()

        print(f"Time: {i}, Temperature: {current_temperature}, Thermostat: {thermostat_setting}")

        agent.adjust_thermostat()
        agent.update_model()

        time.sleep(0.5)

print("Model based agent")
room = Room(27)
agent = ModelBasedAgent(room)

simulate(agent, room)