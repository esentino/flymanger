from django.db import models
from django.contrib.auth.models import User


class InvestModel(models.Model):
    invest_money = models.IntegerField()
    income_bonus = models.IntegerField(verbose_name="bonus money per minute")

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


class PlainCargo(models.Model):
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
