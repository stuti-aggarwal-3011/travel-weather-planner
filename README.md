# Travel Weather Planner

A clean, lightweight Python script designed to evaluate whether a commute is feasible based on real-world constraints: travel distance, active weather conditions, and personal transit options.

## 🚀 How It Works

The script systematically evaluates commuting logic using nested conditional control flows (`if`, `elif`, and `else`) arranged in ascending order of distance:

* **Falsy Check:** Instantly rejects invalid or zero-mile distances.
* **Short Commutes ($\le$ 1 mile):** Deemed feasible as long as it is not actively raining.
* **Medium Commutes ($\le$ 6 miles):** Requires a bicycle and clear weather.
* **Long Commutes (> 6 miles):** Requires motorized transport (a personal car or a ride-sharing application).

## 🛠️ Variables Evaluated

| Variable | Type | Description |
| :--- | :--- | :--- |
| `distance_mi` | `float` / `int` | The total transit distance in miles. |
| `is_raining` | `boolean` | Current precipitation status. |
| `has_bike` | `boolean` | Availability of a bicycle. |
| `has_car` | `boolean` | Availability of a personal vehicle. |
| `has_ride_share_app` | `boolean` | Access to on-demand ride applications. |

## 💻 Tech Stack
* **Language:** Python 3.x
* **Concepts:** Conditional logic, boolean algebra, control structures.
