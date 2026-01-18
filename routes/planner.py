from auth import login_required
from data import ISLAND_DESTINATIONS
from database import get_db
from datetime import datetime
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from data import INDIAN_DESTINATIONS, DESTINATION_ITINERARIES

planner = Blueprint("planner", __name__)


def calculate_trip_plan(destination, days, people, hotel_type, travel_mode, travel_class):
    destination = destination.lower().strip()
    travel_mode = travel_mode.lower().strip()


    travel_class = travel_class.lower().strip()

    destination = destination.lower().strip()
    is_international = destination not in INDIAN_DESTINATIONS



    # -----------------------------
    # HOTEL COST
    # -----------------------------
    DOMESTIC_HOTEL = {
        "budget": 2500,
        "standard": 5000,
        "luxury": 9000
    }

    INTERNATIONAL_HOTEL = {
        "budget": 7000,
        "standard": 14000,
        "luxury": 25000
    }

    rooms = max(1, (people + 1) // 2)
    hotel_rates = INTERNATIONAL_HOTEL if is_international else DOMESTIC_HOTEL
    hotel_cost = hotel_rates[hotel_type.lower()] * days * rooms

    # -----------------------------
    # FOOD COST
    # -----------------------------
    food_daily = 3000 if is_international else 1000
    food_cost = food_daily * days * people

    # -----------------------------
    # TRANSPORT COST (THIS IS THE CORE FIX)
    # -----------------------------
    transport_cost = 0
    visa_cost = 0

    # 🚆 TRAIN (DOMESTIC ONLY)
    if travel_mode == "train":
        if is_international:
            raise ValueError("Train is not available for international trips")

        if travel_class == "sleeper":
            one_way = 1200
        elif travel_class == "third ac":
            one_way = 2000
        elif travel_class == "second ac":
            one_way = 2800
        elif travel_class == "first ac":
            one_way = 4200
        else:
            raise ValueError("Invalid train class")

        # round trip × people
        transport_cost = one_way * 2 * people

    # ✈️ FLIGHT
    elif travel_mode == "flight":

        # 🌍 INTERNATIONAL FLIGHT
        if is_international:
            if travel_class == "economy":
                one_way = 75000
            elif travel_class == "premium economy":
                one_way = 120000
            elif travel_class == "business":
                one_way = 200000
            elif travel_class == "first class":
                one_way = 300000
            else:
                raise ValueError("Invalid international flight class")

            transport_cost = one_way * 2 * people
            visa_cost = 10000 * people

        # 🇮🇳 DOMESTIC FLIGHT
        else:
            if travel_class == "economy":
                one_way = 6000
            elif travel_class == "business":
                one_way = 15000
            else:
                raise ValueError("Invalid domestic flight class")

            transport_cost = one_way * 2 * people

    else:
        raise ValueError("Invalid travel mode")

    # -----------------------------
    # ACTIVITIES
    # -----------------------------
    activities_daily = 2000 if is_international else 800
    activities_cost = activities_daily * days * people

    # -----------------------------
    # TOTAL
    # -----------------------------
    total_budget = (
        hotel_cost +
        food_cost +
        transport_cost +
        activities_cost +
        visa_cost
    )

    # -----------------------------
    # ITINERARY
    # -----------------------------
    places = DESTINATION_ITINERARIES.get(destination, [])
    itinerary = []

    for day in range(1, days + 1):
        if day <= len(places):
            itinerary.append(f"Day {day}: {places[day - 1]}")
        else:
            itinerary.append(f"Day {day}: Leisure / Exploration")

    return {
        "hotel_cost": hotel_cost,
        "food_cost": food_cost,
        "transport_cost": transport_cost,
        "activities_cost": activities_cost,
        "visa_cost": visa_cost,
        "total_budget": total_budget,
        "itinerary": itinerary,
        "is_international": is_international
    }


@planner.route("/plan-trip", methods=["GET", "POST"])
@login_required
def plan_trip():
    if request.method == "POST":
        conn = None
        try:
            # 🔐 Extra safety: session must exist
            user_id = session.get("user_id")
            if not user_id:
                flash("Session expired. Please login again.", "warning")
                return redirect(url_for("login"))

            destination_raw = request.form.get("destination", "")
            destination = destination_raw.strip().lower()

            # 🛡️ Validate required fields
            start_date = request.form.get("start_date")
            if not start_date:
                flash("Please select a start date.", "danger")
                return render_template("planner.html")

            days = int(request.form.get("days") or 0)
            people = int(request.form.get("people") or 1)

            hotel_type = request.form.get("hotel_type")
            travel_mode = request.form.get("travel_mode")
            travel_class = request.form.get("travel_class")

            if not destination or days <= 0 or people <= 0:
                flash("Please fill all trip details correctly.", "danger")
                return render_template("planner.html")

            # ❌ No train allowed for island destinations
            if (
                destination in ISLAND_DESTINATIONS
                and travel_mode
                and travel_mode.lower() == "train"
            ):
                flash(
                    "Train is not available for island destinations like Andaman or Lakshadweep.",
                    "danger"
                )
                return render_template(
                    "planner.html",
                    destination=destination_raw,
                    start_date=start_date,
                    days=days,
                    people=people,
                    hotel_type=hotel_type,
                    travel_mode=travel_mode,
                    travel_class=travel_class
                )

            # ✅ Calculate trip (your logic untouched)
            result = calculate_trip_plan(
                destination,
                days,
                people,
                hotel_type,
                travel_mode,
                travel_class
            )

            # 🛡️ Safety check for calculation
            if not result or "total_budget" not in result:
                raise ValueError("Trip calculation failed")

            # ✅ SAVE TRIP TO DATABASE
            conn = get_db()
            conn.execute("""
                INSERT INTO trips (
                    user_id,
                    destination,
                    start_date,
                    days,
                    people,
                    hotel_type,
                    travel_mode,
                    travel_class,
                    total_budget,
                    created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                destination,
                start_date,
                days,
                people,
                hotel_type,
                travel_mode,
                travel_class,
                result["total_budget"],
                datetime.utcnow().isoformat()
            ))
            conn.commit()

            # ✅ SUCCESS PAGE
            return render_template(
                "trip-result.html",
                destination=destination.title(),
                days=days,
                people=people,
                hotel_type=hotel_type,
                travel_mode=travel_mode,
                travel_class=travel_class,
                budget=result["total_budget"],
                **result
            )

        except Exception as e:
            # 🔥 Render-safe logging
            print("PLAN TRIP ERROR:", str(e))

            flash("Something went wrong while planning your trip.", "danger")
            return render_template("planner.html")

        finally:
            # 🧹 Always close DB (prevents Render crashes)
            if conn:
                conn.close()

    return render_template("planner.html")



@planner.route("/my-trips")
@login_required
def my_trips():
    user_id = session.get("user_id")

    if not user_id:
        flash("Session expired. Please login again.", "warning")
        return redirect(url_for("login"))

    conn = get_db()
    trips = conn.execute(
        """
        SELECT *
        FROM trips
        WHERE user_id = ?
        ORDER BY created_at DESC
        """,
        (user_id,)
    ).fetchall()
    conn.close()

    return render_template("my_trips.html", trips=trips)


@planner.route("/delete-trip/<int:trip_id>", methods=["POST"])
@login_required
def delete_trip(trip_id):
    user_id = session.get("user_id")

    if not user_id:
        flash("Session expired. Please login again.", "warning")
        return redirect(url_for("login"))

    conn = get_db()
    conn.execute(
        "DELETE FROM trips WHERE id = ? AND user_id = ?",
        (trip_id, user_id)
    )
    conn.commit()
    conn.close()

    flash("🗑️ Trip deleted successfully!", "success")
    return redirect(url_for("planner.my_trips"))

