from typing import List
import json


class CMD:
    UPDATE_CONFIG = "update_configuration"
    GET_TEMPERATURE = "get_temperature"
    GET_HUMIDITY = "get_humidity"
    GET_LIGHT_INTENSITY = "get_light_intensity"
    GET_LIGHT_INTENSITIES = "get_light_intensities"
    GET_FAN_SPEED = "get_fan_speed"
    GET_FAN_SPEEDS = "get_fan_speeds"
    GET_PUMP_STATUS = "get_pump_status"
    ON_LIGHT = "turn_on_light"
    OFF_LIGHT = "turn_off_light"
    ON_LIGHTS = "turn_on_lights"
    OFF_LIGHTS = "turn_off_lights"
    ON_FANS = "turn_on_fans"
    OFF_FANS = "turn_off_fans"
    ON_PUMP = "turn_on_pump"
    OFF_PUMP = "turn_off_pump"



class IO:
    def __init__(self, id: int):
        self.id = id
        
    def send(self, msg: str):
        print(msg)

    def recv(self) -> str:
        pass

    def _build_json(self, cmd: str, args: dict) -> str:
        json_params = {"shelf": self.id, "cmd": cmd, "param": args}
        return json.dumps(json_params)

    def _pop_self(self, args: dict) -> dict:
        args.pop("self")
        return args

    # === ACTUATORS METHODS ===
    def turn_on_light(self, light_id: int, intensity: int) -> None:
        assert 0 <= intensity <= 100

        msg = self._build_json(CMD.ON_LIGHT, self._pop_self(locals()))

        self.send(msg)
        
    def turn_on_lights(self, intensity: int) -> None:
        assert 0 <= intensity <= 100

        msg = self._build_json(CMD.ON_LIGHTS, self._pop_self(locals()))

        self.send(msg)

    def turn_off_light(self, light_id: int) -> None:
        msg = self._build_json(CMD.OFF_LIGHT, self._pop_self(locals()))

        self.send(msg)

    def turn_off_lights(self) -> None:
        msg = self._build_json(CMD.OFF_LIGHTS, self._pop_self(locals()))

        self.send(msg)

    def turn_on_fans() -> None:
        pass

    def turn_off_fans() -> None:
        pass


    # === GETTER METHODS ===
    def get_temperature(self) -> float:
        msg = self._build_json(CMD.GET_TEMPERATURE, {})

        self.send(msg)

        temperature = self.recv()

        # TODO add verification

        return temperature

    def get_humidity(self) -> int:
        msg = self._build_json(CMD.GET_HUMIDITY, {})

        self.send(msg)

        humidity = self.recv()

        # TODO add verification

        return humidity
        

    def get_light_intensity(self, light_id: int) -> int:
        msg = self._build_json(CMD.GET_LIGHT_INTENSITY, self._pop_self(locals))

        self.send(msg)

        intensity = self.recv()

        # TODO add verification
        # TODO raw value ([0, 255] or in %)

        return intensity

    def get_light_intensities(self) -> List[int]:
        msg = self._build_json(CMD.GET_LIGHT_INTENSITIES, {})

        self.send(msg)

        intensities = self.recv()

        # TODO add verification

        return intensities