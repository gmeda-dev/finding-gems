import os
from csv import DictReader
from decimal import Decimal

import requests
from django.contrib import messages
from django.db.models import F
from django.db.models.functions import Sqrt, Power
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.edit import BaseFormView, FormView

from game.forms import DifficultyForm, FindGemForm
from game.models import FoodTruck
from game.serializers import FoodTruckSerializer


class IndexView(FormView):
    template_name = "index.html"
    form_class = FindGemForm
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.GET.get("reset"):
            if self.request.session.get("difficulty"):
                del self.request.session["difficulty"]

        if self.request.session.get("difficulty"):
            context["gem_form"] = self.form_class()
            if pk_found := self.request.session.get("pk_found"):
                context["food_trucks"] = FoodTruck.objects.filter(pk__in=pk_found)
        else:
            context["difficulty_form"] = DifficultyForm()

        return context

    def post(self, request, *args, **kwargs):
        if difficulty := Decimal(self.request.session.get("difficulty")):
            form = self.form_class(data=self.request.POST)
            if form.is_valid():
                latitude = Decimal(form.cleaned_data.get("latitude"))
                longitude = Decimal(form.cleaned_data.get("longitude"))
                food_trucks = (
                    FoodTruck.objects.annotate(
                        distance=Sqrt(  # distance between two points
                            Power(latitude - F("latitude"), 2)
                            + Power(longitude - F("longitude"), 2)
                        )
                    )
                    .exclude(pk__in=self.request.session["pk_found"])
                    .order_by("distance")[:difficulty]
                )
                for food_truck in food_trucks:
                    self.request.session["score"] += int(
                        50 / food_truck.distance
                    )  # bigger the distance => smaller the score
                if food_truck_count := food_trucks.count():
                    self.request.session["pk_found"] += food_trucks.values_list(
                        "pk", flat=True
                    )
                    messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Congrats! You found {food_truck_count} new gems!",
                    )
                    if (
                        len(self.request.session["pk_found"])
                        == FoodTruck.objects.count()
                    ):
                        score = self.request.session["score"]
                        messages.add_message(
                            request,
                            messages.SUCCESS,
                            f"GAME OVER! Your score is {score}, click RESET and try to beat it.",
                        )
            else:
                messages.add_message(request, messages.ERROR, form.errors)
        else:
            messages.add_message(request, messages.ERROR, "No difficulty selected.")

        return super().post(request, *args, **kwargs)


class SetDiffcultyView(BaseFormView):
    http_method_names = ["post"]
    form_class = DifficultyForm
    success_url = "/"

    def form_valid(self, form):
        self.request.session["difficulty"] = form.cleaned_data["difficulty"]
        self.request.session["score"] = 0
        self.request.session["pk_found"] = []
        if FoodTruck.objects.count() == 0:
            FOOD_TRUCKS_CSV_FILE = "food-truck-data.csv"
            response = requests.get(
                "https://raw.githubusercontent.com/RAKT-Innovations/P1-django-take-home-assignment/main/food-truck-data.csv"
            )

            with open(FOOD_TRUCKS_CSV_FILE, "w") as f:
                f.write(response.text)

            with open(FOOD_TRUCKS_CSV_FILE, "r") as f:
                reader = DictReader(f)
                serializer = FoodTruckSerializer(data=list(reader), many=True)
                if serializer.is_valid():
                    serializer.save()

            os.remove(FOOD_TRUCKS_CSV_FILE)

        return redirect(reverse("index"))
