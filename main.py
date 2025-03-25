from car.models import Car
import io
from car.serializers import CarSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def serialize_car_object(car: Car) -> bytes:
    car = Car.objects.get(id=car.id)
    serializer = CarSerializer(car)
    json = JSONRenderer().render(serializer.data)
    return json


def deserialize_car_object(json: bytes) -> Car:
    stream = io.BytesIO(json)
    data = JSONParser().parse(stream)
    serializer = CarSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()
