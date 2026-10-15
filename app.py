from flask import Flask, render_template, request, redirect, url_for, flash

from exoplanets import (
    get_all_exoplanets,
    search_exoplanets,
    get_statistics,
    get_most_common_method,
    get_discovery_methods,
    get_exoplanet_by_id,
    add_exoplanet,
    update_exoplanet,
    delete_exoplanet,
)

from logger import log_info, log_error


app = Flask(__name__)
app.secret_key = "horizon-local-project-key"


@app.route("/")
def home():
    """Display the main Horizon page with search, filters and statistics."""
    try:
        name = request.args.get("name", "").strip()
        method = request.args.get("method", "").strip()
        sort_by = request.args.get("sort", "planet_name").strip()

        start_year_text = request.args.get("start_year", "").strip()
        end_year_text = request.args.get("end_year", "").strip()

        start_year = int(start_year_text) if start_year_text.isdigit() else None
        end_year = int(end_year_text) if end_year_text.isdigit() else None

        if not name and not method and start_year is None and end_year is None:
            planets = get_all_exoplanets()
        else:
            planets = search_exoplanets(
                name=name,
                method=method,
                start_year=start_year,
                end_year=end_year,
                sort_by=sort_by,
            )

        statistics = get_statistics() or {}
        common_method = get_most_common_method() or {}
        methods = get_discovery_methods()

        log_info(
            "Home/search | "
            f"name={name!r} | method={method!r} | "
            f"start_year={start_year!r} | end_year={end_year!r} | "
            f"sort={sort_by!r}"
        )

        return render_template(
            "index.html",
            planets=planets,
            statistics=statistics,
            common_method=common_method,
            methods=methods,
            current_name=name,
            current_method=method,
            current_sort=sort_by,
            current_start_year=start_year_text,
            current_end_year=end_year_text,
        )

    except Exception as error:
        log_error(f"Home route error: {error}")
        flash("An error occurred while loading Horizon.", "error")

        return render_template(
            "index.html",
            planets=[],
            statistics={
                "total_planets": 0,
                "earliest_discovery": "N/A",
                "latest_discovery": "N/A",
            },
            common_method={"discovery_method": "N/A"},
            methods=[],
            current_name="",
            current_method="",
            current_sort="planet_name",
            current_start_year="",
            current_end_year="",
        )


@app.route("/add", methods=["GET", "POST"])
def add():
    """Display and process the Add Exoplanet form."""
    try:
        methods = get_discovery_methods()

        if request.method == "GET":
            return render_template("add.html", methods=methods)

        planet_name = request.form.get("planet_name", "").strip()
        host_star = request.form.get("host_star", "").strip()
        discovery_year_text = request.form.get("discovery_year", "").strip()
        discovery_method = request.form.get("discovery_method", "").strip()
        orbital_period_text = request.form.get("orbital_period_days", "").strip()
        radius_text = request.form.get("radius_earth", "").strip()
        mass_text = request.form.get("mass_earth", "").strip()
        distance_text = request.form.get("distance_pc", "").strip()
        temperature_text = request.form.get("equilibrium_temp_k", "").strip()

        if not planet_name:
            flash("Planet name is required.", "error")
            return render_template("add.html", methods=methods)

        try:
            discovery_year = int(discovery_year_text) if discovery_year_text else None
            orbital_period = float(orbital_period_text) if orbital_period_text else None
            radius = float(radius_text) if radius_text else None
            mass = float(mass_text) if mass_text else None
            distance = float(distance_text) if distance_text else None
            temperature = float(temperature_text) if temperature_text else None
        except ValueError:
            flash("Please enter valid numerical values.", "error")
            return render_template("add.html", methods=methods)

        success = add_exoplanet(
            planet_name,
            host_star or None,
            discovery_year,
            discovery_method or None,
            orbital_period,
            radius,
            mass,
            distance,
            temperature,
        )

        if success:
            log_info(f"Exoplanet added: {planet_name}")
            flash("Exoplanet added successfully.", "success")
            return redirect(url_for("home"))

        log_error(f"Failed to add exoplanet: {planet_name}")
        flash(
            "Could not add the exoplanet. The planet name may already exist.",
            "error",
        )
        return render_template("add.html", methods=methods)

    except Exception as error:
        log_error(f"Add route error: {error}")
        flash("An error occurred while adding the exoplanet.", "error")
        return redirect(url_for("home"))


@app.route("/update/<int:planet_id>", methods=["GET", "POST"])
def update(planet_id):
    """Display and process the Update Exoplanet form."""
    try:
        planet = get_exoplanet_by_id(planet_id)
        methods = get_discovery_methods()

        if planet is None:
            flash("Exoplanet not found.", "error")
            return redirect(url_for("home"))

        if request.method == "GET":
            return render_template(
                "update.html",
                planet=planet,
                methods=methods,
            )

        planet_name = request.form.get("planet_name", "").strip()
        host_star = request.form.get("host_star", "").strip()
        discovery_year_text = request.form.get("discovery_year", "").strip()
        discovery_method = request.form.get("discovery_method", "").strip()
        orbital_period_text = request.form.get("orbital_period_days", "").strip()
        radius_text = request.form.get("radius_earth", "").strip()
        mass_text = request.form.get("mass_earth", "").strip()
        distance_text = request.form.get("distance_pc", "").strip()
        temperature_text = request.form.get("equilibrium_temp_k", "").strip()

        if not planet_name:
            flash("Planet name is required.", "error")
            return render_template(
                "update.html",
                planet=planet,
                methods=methods,
            )

        try:
            discovery_year = int(discovery_year_text) if discovery_year_text else None
            orbital_period = float(orbital_period_text) if orbital_period_text else None
            radius = float(radius_text) if radius_text else None
            mass = float(mass_text) if mass_text else None
            distance = float(distance_text) if distance_text else None
            temperature = float(temperature_text) if temperature_text else None
        except ValueError:
            flash("Please enter valid numerical values.", "error")
            return render_template(
                "update.html",
                planet=planet,
                methods=methods,
            )

        success = update_exoplanet(
            planet_id,
            planet_name,
            host_star or None,
            discovery_year,
            discovery_method or None,
            orbital_period,
            radius,
            mass,
            distance,
            temperature,
        )

        if success:
            log_info(f"Exoplanet updated: ID={planet_id}")
            flash("Exoplanet updated successfully.", "success")
        else:
            log_error(f"Update failed: ID={planet_id}")
            flash("No changes were made.", "error")

        return redirect(url_for("home"))

    except Exception as error:
        log_error(f"Update route error for ID={planet_id}: {error}")
        flash("An error occurred while updating the exoplanet.", "error")
        return redirect(url_for("home"))


@app.route("/delete/<int:planet_id>", methods=["POST"])
def delete(planet_id):
    """Delete an exoplanet by database ID."""
    try:
        success = delete_exoplanet(planet_id)

        if success:
            log_info(f"Exoplanet deleted: ID={planet_id}")
            flash("Exoplanet deleted successfully.", "success")
        else:
            log_error(f"Delete failed: ID={planet_id}")
            flash("Planet could not be deleted.", "error")

    except Exception as error:
        log_error(f"Delete route error for ID={planet_id}: {error}")
        flash("An error occurred while deleting the exoplanet.", "error")

    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(error):
    """Handle unknown routes."""
    log_error(f"404 error: {request.path}")
    flash("Page not found.", "error")
    return redirect(url_for("home"))


if __name__ == "__main__":
    log_info("Horizon application started")
    app.run(
        host="127.0.0.1",
        port=5001,
        debug=False,
    )
