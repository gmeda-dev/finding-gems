from datetime import datetime
from django.conf import settings
from game.models import FoodTruck
from rest_framework import serializers
from django.db import models


class FoodTruckSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        return {
            "location_id": data["locationid"],
            "applicant": data["Applicant"],
            "facility_type": data["FacilityType"],
            "cnn": data["cnn"],
            "location_description": data["LocationDescription"],
            "address": data["Address"],
            "block_lot": data["blocklot"],
            "block": data["block"],
            "lot": data["lot"],
            "permit": data["permit"],
            "status": data["Status"],
            "food_items": data["FoodItems"],
            "x": val if (val := data.get("X")) else None,
            "y": val if (val := data.get("Y")) else None,
            "latitude": data["Latitude"],
            "longitude": data["Longitude"],
            "schedule": data["Schedule"],
            "days_hours": data["dayshours"],
            "noisent": data["NOISent"],
            "approved": datetime.strptime(
                date, settings.REST_FRAMEWORK["DATETIME_INPUT_FORMATS"][0]
            )
            if (date := data["Approved"])
            else None,
            "received": data["Received"],
            "prior_permit": data["PriorPermit"],
            "expiration_date": datetime.strptime(
                date, settings.REST_FRAMEWORK["DATETIME_INPUT_FORMATS"][0]
            )
            if (date := data["ExpirationDate"])
            else None,
            "fire": data["Fire Prevention Districts"],
            "police": data["Police Districts"],
            "supervisor": data["Supervisor Districts"],
            "zip": data["Zip Codes"],
            "neighborhoods": data["Neighborhoods (old)"],
        }

    class Meta:
        model = FoodTruck
        fields = (
            "location_id",
            "applicant",
            "facility_type",
            "cnn",
            "location_description",
            "address",
            "block_lot",
            "block",
            "lot",
            "permit",
            "status",
            "food_items",
            "x",
            "y",
            "latitude",
            "longitude",
            "schedule",
            "days_hours",
            "noisent",
            "approved",
            "received",
            "prior_permit",
            "expiration_date",
            "fire",
            "police",
            "supervisor",
            "zip",
            "neighborhoods",
        )
