from enum import Enum

from django.db import models
from django.contrib.auth.models import User


class InvestModel(models.Model):
    invest_money = models.IntegerField()
    income_bonus = models.IntegerField(verbose_name="bonus income per minute")

    class Meta:
        abstract = True


class UserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)


class Plane(models.Model):
    plane_id = models.BigAutoField(primary_key=True)
    packing_time = models.DurationField()
    travel_income = models.IntegerField()


class Cargo(models.Model):
    cargo_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)
    base_income = models.IntegerField()


class CargoImprovement(InvestModel):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


class PlaneCargo(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    count = models.IntegerField()


class UserPlane(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    packing_finished = models.BooleanField(default=False)


class UserContract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plane, on_delete=models.CASCADE)


class UserWarehouse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    last_recount_time = models.DateTimeField(auto_now_add=True)


class WarehouseImprovement(InvestModel):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)


class UserCargoInvestment(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invest_money = models.IntegerField(default=0)

    class Meta:
        unique_together = [["cargo", "user"]]


class UserWarehouseImprovement(models.Model):
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    invest_money = models.IntegerField(default=0)

    class Meta:
        unique_together = [["cargo", "user"]]


class BonusType(str, Enum):
    PACKING_TIME = 'packing_type'
    INCOME_INCREASE = 'income_increase'


BONUS_PLANE_CHOICES = (
    (BonusType.PACKING_TIME, 'Packing Time reduction in seconds'),
    (BonusType.INCOME_INCREASE, 'More money')
)


class PlaneImprovement(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    done_plane = models.IntegerField()
    bonus_type = models.CharField(choices=BONUS_PLANE_CHOICES)
    bonus_value = models.IntegerField()


class UserPlaneImprovement(models.Model):
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    done_plane = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
