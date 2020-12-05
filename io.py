from typing import List


class IO:
    def __init__(self, id: int):
        self.id = id

    # === ACTUATORS METHODS ===
    def _send_and_check(cmd: str) -> bool:
        pass

    def turn_on_light(light_id: int, intensity: int) -> None:
        assert 0 <= intensity <= 100
        pass

    def turn_on_lights(intensity: int) -> None:
        pass

    def turn_off_light(light_id: int) -> None:
        pass

    def turn_off_lights() -> None:
        pass

    def turn_on_fans() -> None:
        pass

    def turn_off_fans() -> None:
        pass


    # === GETTER METHODS ===
    def get_temperature() -> float:
        pass

    def get_humidity() -> int:
        pass

    def get_light_intensity(light_id: int) -> int:
        pass

    def get_light_intensities() -> List[int]:
        pass