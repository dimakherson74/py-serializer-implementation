from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_power = serializers.IntegerField()
    is_broken = serializers.BooleanField()

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data(
            "manufacturer", instance.manufacturer
        )
        instance.model = validated_data("model", instance.model)
        instance.horse_power = validated_data(
            "horse_power", instance.horse_power
        )
        instance.is_broken = validated_data("is_broken", instance.is_broken)
        instance.save()
        return instance

    class Meta:
        model = Car
