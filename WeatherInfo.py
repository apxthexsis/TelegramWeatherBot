from attr import dataclass
from gettext import gettext as _
@dataclass
class WeatherInfo:
    temperature: float
    feels_like: float
    temp_min: float
    temp_max: float
    desc: str



    @classmethod
    def from_dict(cls, data: dict) -> "WeatherInfo":
        return cls(
            temperature=data["main"]["temp"],
            temp_min=data["main"]["temp_min"],
            temp_max=data["main"]["temp_max"],
            desc=data["weather"][0]["main"],
            feels_like=data["main"]["feels_like"],
        )

    def translateData(self):
        return (_("Temperature: {}\nFeels like: {}\nMinimal: {}\nMaximal: {}\nWeather: {}").format(self.temperature, self.feels_like, self.temp_min, self.temp_max, self.desc))