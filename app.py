import streamlit as st
import random
import time
from datetime import datetime



st.set_page_config(
    page_title="ROTAX 912 | Digital Twin",
    layout="wide",
    initial_sidebar_state="collapsed"
)



st.markdown(
    """
    <style>
    .stApp {
        background-color: #111416;
        color: #d5dad7;
    }

    .main .block-container {
        max-width: 1450px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    h1 {
        font-size: 25px !important;
        font-weight: 500 !important;
        letter-spacing: 1px;
        color: #dce1de;
    }

    h2 {
        font-size: 16px !important;
        font-weight: 500 !important;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        color: #bfc6c2;
        margin-top: 22px !important;
    }

    h3 {
        font-size: 13px !important;
        font-weight: 500 !important;
        color: #aab2ae;
    }

    div[data-testid="stMetric"] {
        background-color: #171b1d;
        border: 1px solid #343b38;
        padding: 10px 12px;
    }

    div[data-testid="stMetricLabel"] {
        color: #858f8a !important;
        font-size: 9px !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    div[data-testid="stMetricValue"] {
        color: #d7dcda !important;
        font-family: Consolas, monospace;
        font-size: 22px !important;
    }

    .stButton > button {
        background-color: #202523;
        color: #c9cfcc;
        border: 1px solid #46504b;
        border-radius: 2px;
        font-size: 10px;
        letter-spacing: 0.7px;
        min-height: 38px;
    }

    .stButton > button:hover {
        background-color: #292f2c;
        border-color: #68736d;
    }

    .stProgress > div > div > div {
        background-color: #708877;
    }

    .header-text {
        color: #7f8985;
        font-size: 10px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }

    .small-text {
        color: #7f8985;
        font-size: 11px;
    }

    </style>
    """,
    unsafe_allow_html=True
)



if "fault_type" not in st.session_state:
    st.session_state.fault_type = "NONE"

if "health" not in st.session_state:
    st.session_state.health = 100.0

if "rul" not in st.session_state:
    st.session_state.rul = 24.0

if "mission_survival" not in st.session_state:
    st.session_state.mission_survival = 98.0

if "event_log" not in st.session_state:
    st.session_state.event_log = []

if "running" not in st.session_state:
    st.session_state.running = True




FAULTS = {
    "NONE": "No active fault",
    "MISFIRE": "Misfire",
    "INJECTOR": "Injector abnormality",
    "COOLING": "Cooling degradation",
    "LUBRICATION": "Lubrication issue",
    "SENSOR": "Sensor drift / failure",
    "COMBUSTION": "Combustion instability",
    "OVERHEATING": "Overheating trend",
    "VIBRATION": "Abnormal vibration"
}




def generate_telemetry(fault):

    

    if fault == "NONE":

        rpm = random.uniform(2450, 2600)

        cht = [
            random.uniform(158, 170),
            random.uniform(160, 172),
            random.uniform(157, 169),
            random.uniform(159, 171)
        ]

        egt = [
            random.uniform(675, 705),
            random.uniform(678, 708),
            random.uniform(674, 704),
            random.uniform(680, 710)
        ]

        oil_pressure = random.uniform(4.6, 5.4)
        oil_temp = random.uniform(85, 98)
        fuel_flow = random.uniform(8.5, 10.2)
        vibration = random.uniform(1.0, 1.9)
        injection_timing = random.uniform(23.5, 25.0)
        battery_health = random.uniform(95, 100)
        alternator_health = random.uniform(95, 100)

    

    elif fault == "MISFIRE":

        rpm = random.uniform(2200, 2400)

        cht = [
            random.uniform(158, 172),
            random.uniform(160, 174),
            random.uniform(145, 160),
            random.uniform(160, 174)
        ]

        egt = [
            random.uniform(680, 710),
            random.uniform(682, 712),
            random.uniform(550, 625),
            random.uniform(684, 714)
        ]

        oil_pressure = random.uniform(4.0, 4.8)
        oil_temp = random.uniform(92, 105)
        fuel_flow = random.uniform(9.5, 12.0)
        vibration = random.uniform(3.5, 6.0)
        injection_timing = random.uniform(24.0, 27.5)
        battery_health = random.uniform(92, 98)
        alternator_health = random.uniform(92, 98)

    

    elif fault == "INJECTOR":

        rpm = random.uniform(2250, 2430)

        cht = [
            random.uniform(160, 174),
            random.uniform(162, 176),
            random.uniform(180, 202),
            random.uniform(161, 175)
        ]

        egt = [
            random.uniform(680, 710),
            random.uniform(684, 714),
            random.uniform(755, 830),
            random.uniform(685, 715)
        ]

        oil_pressure = random.uniform(4.0, 4.7)
        oil_temp = random.uniform(95, 108)
        fuel_flow = random.uniform(10.5, 13.0)
        vibration = random.uniform(3.0, 5.5)
        injection_timing = random.uniform(26.0, 29.0)
        battery_health = random.uniform(93, 98)
        alternator_health = random.uniform(93, 98)

  

    elif fault == "COOLING":

        rpm = random.uniform(2420, 2520)

        cht = [
            random.uniform(190, 210),
            random.uniform(192, 213),
            random.uniform(194, 216),
            random.uniform(191, 212)
        ]

        egt = [
            random.uniform(710, 750),
            random.uniform(712, 754),
            random.uniform(715, 756),
            random.uniform(713, 752)
        ]

        oil_pressure = random.uniform(4.2, 5.0)
        oil_temp = random.uniform(102, 118)
        fuel_flow = random.uniform(9.0, 11.0)
        vibration = random.uniform(2.0, 3.5)
        injection_timing = random.uniform(23.5, 25.5)
        battery_health = random.uniform(94, 99)
        alternator_health = random.uniform(94, 99)

    

    elif fault == "LUBRICATION":

        rpm = random.uniform(2350, 2490)

        cht = [
            random.uniform(170, 187),
            random.uniform(172, 189),
            random.uniform(171, 188),
            random.uniform(173, 190)
        ]

        egt = [
            random.uniform(695, 725),
            random.uniform(698, 728),
            random.uniform(696, 726),
            random.uniform(700, 730)
        ]

        oil_pressure = random.uniform(2.3, 3.5)
        oil_temp = random.uniform(108, 130)
        fuel_flow = random.uniform(9.0, 11.0)
        vibration = random.uniform(2.8, 4.6)
        injection_timing = random.uniform(23.5, 25.5)
        battery_health = random.uniform(92, 98)
        alternator_health = random.uniform(92, 98)

   

    elif fault == "SENSOR":

        rpm = random.uniform(2470, 2590)

        cht = [
            random.uniform(158, 171),
            random.uniform(160, 172),
            random.uniform(157, 170),
            random.uniform(159, 171)
        ]

        egt = [
            random.uniform(680, 710),
            random.uniform(680, 710),
            random.uniform(675, 705),
            random.uniform(680, 710)
        ]

        cht[2] += random.uniform(30, 55)

        oil_pressure = random.uniform(4.7, 5.4)
        oil_temp = random.uniform(86, 98)
        fuel_flow = random.uniform(8.5, 10.2)
        vibration = random.uniform(1.0, 2.0)
        injection_timing = random.uniform(23.5, 25.0)
        battery_health = random.uniform(95, 100)
        alternator_health = random.uniform(95, 100)

   

    elif fault == "COMBUSTION":

        rpm = random.uniform(2300, 2470)

        cht = [
            random.uniform(165, 182),
            random.uniform(166, 184),
            random.uniform(172, 190),
            random.uniform(164, 182)
        ]

        egt = [
            random.uniform(710, 755),
            random.uniform(700, 750),
            random.uniform(735, 780),
            random.uniform(705, 750)
        ]

        oil_pressure = random.uniform(4.0, 4.8)
        oil_temp = random.uniform(95, 108)
        fuel_flow = random.uniform(10.0, 12.5)
        vibration = random.uniform(3.0, 5.0)
        injection_timing = random.uniform(26.0, 29.0)
        battery_health = random.uniform(93, 98)
        alternator_health = random.uniform(93, 98)

   

    elif fault == "OVERHEATING":

        rpm = random.uniform(2380, 2500)

        cht = [
            random.uniform(195, 215),
            random.uniform(198, 218),
            random.uniform(200, 220),
            random.uniform(196, 216)
        ]

        egt = [
            random.uniform(735, 775),
            random.uniform(738, 780),
            random.uniform(740, 785),
            random.uniform(736, 778)
        ]

        oil_pressure = random.uniform(3.8, 4.7)
        oil_temp = random.uniform(110, 128)
        fuel_flow = random.uniform(9.5, 11.5)
        vibration = random.uniform(2.2, 3.8)
        injection_timing = random.uniform(23.5, 26.0)
        battery_health = random.uniform(94, 98)
        alternator_health = random.uniform(94, 98)

    

    elif fault == "VIBRATION":

        rpm = random.uniform(2430, 2550)

        cht = [
            random.uniform(162, 175),
            random.uniform(164, 177),
            random.uniform(162, 175),
            random.uniform(164, 177)
        ]

        egt = [
            random.uniform(680, 710),
            random.uniform(683, 713),
            random.uniform(681, 711),
            random.uniform(684, 714)
        ]

        oil_pressure = random.uniform(4.5, 5.2)
        oil_temp = random.uniform(88, 100)
        fuel_flow = random.uniform(8.8, 10.5)
        vibration = random.uniform(5.0, 8.0)
        injection_timing = random.uniform(23.5, 25.0)
        battery_health = random.uniform(94, 99)
        alternator_health = random.uniform(94, 99)

    else:

        return generate_telemetry("NONE")

    return {
        "rpm": rpm,
        "cht": cht,
        "egt": egt,
        "oil_pressure": oil_pressure,
        "oil_temp": oil_temp,
        "fuel_flow": fuel_flow,
        "vibration": vibration,
        "injection_timing": injection_timing,
        "battery_health": battery_health,
        "alternator_health": alternator_health
    }




def calculate_anomaly(data):

    score = 0.03

    if max(data["egt"]) > 730:
        score += 0.12

    if max(data["egt"]) > 780:
        score += 0.18

    if max(data["cht"]) > 180:
        score += 0.15

    if max(data["cht"]) > 200:
        score += 0.15

    if data["oil_pressure"] < 4.0:
        score += 0.18

    if data["oil_pressure"] < 3.0:
        score += 0.15

    if data["vibration"] > 3.0:
        score += 0.14

    if data["vibration"] > 5.0:
        score += 0.14

    if data["rpm"] < 2350:
        score += 0.12

    return min(score, 0.99)




def update_prediction(fault):

    if fault == "NONE":

        st.session_state.health += random.uniform(0.01, 0.05)

        st.session_state.rul += random.uniform(0.001, 0.01)

        st.session_state.mission_survival += random.uniform(
            0.005,
            0.02
        )

    else:

        severity = {
            "MISFIRE": 0.70,
            "INJECTOR": 0.55,
            "COOLING": 0.45,
            "LUBRICATION": 0.80,
            "SENSOR": 0.35,
            "COMBUSTION": 0.65,
            "OVERHEATING": 0.70,
            "VIBRATION": 0.50
        }.get(fault, 0.5)

        st.session_state.health -= random.uniform(
            severity * 0.20,
            severity * 0.50
        )

        st.session_state.rul -= random.uniform(
            severity * 0.025,
            severity * 0.07
        )

        st.session_state.mission_survival -= random.uniform(
            severity * 0.20,
            severity * 0.60
        )

    st.session_state.health = max(
        0,
        min(100, st.session_state.health)
    )

    st.session_state.rul = max(
        0,
        min(24, st.session_state.rul)
    )

    st.session_state.mission_survival = max(
        0,
        min(99, st.session_state.mission_survival)
    )




def activate_fault(fault):

    st.session_state.fault_type = fault

    timestamp = datetime.now().strftime("%H:%M:%S")

    st.session_state.event_log.insert(
        0,
        f"{timestamp}  {FAULTS[fault]} introduced"
    )

    st.session_state.event_log = (
        st.session_state.event_log[:6]
    )


def reset_engine():

    st.session_state.fault_type = "NONE"
    st.session_state.health = 100.0
    st.session_state.rul = 24.0
    st.session_state.mission_survival = 98.0

    timestamp = datetime.now().strftime("%H:%M:%S")

    st.session_state.event_log.insert(
        0,
        f"{timestamp}  Engine returned to nominal state"
    )

    st.session_state.event_log = (
        st.session_state.event_log[:6]
    )


st.title("UAV ENGINE HEALTH MONITORING SYSTEM")

st.markdown(
    '<div class="header-text">'
    'REAL-TIME DIGITAL TWIN | PROPULSION HEALTH & MISSION RELIABILITY'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

header1, header2, header3, header4 = st.columns(4)

with header1:
    st.caption("PLATFORM")
    st.write("MALE UAV")

with header2:
    st.caption("ENGINE")
    st.write("ROTAX 912")

with header3:
    st.caption("MISSION")
    st.write("ENDURANCE-07")

with header4:
    st.caption("TELEMETRY")
    st.write("LIVE")


st.header("Simulation Control")

b1, b2, b3, b4 = st.columns(4)

with b1:
    if st.button(
        "INJECT MISFIRE",
        use_container_width=True
    ):
        activate_fault("MISFIRE")

with b2:
    if st.button(
        "INJECT INJECTOR FAULT",
        use_container_width=True
    ):
        activate_fault("INJECTOR")

with b3:
    if st.button(
        "INJECT COOLING FAULT",
        use_container_width=True
    ):
        activate_fault("COOLING")

with b4:
    if st.button(
        "RESET ENGINE",
        use_container_width=True
    ):
        reset_engine()


data = generate_telemetry(
    st.session_state.fault_type
)

anomaly = calculate_anomaly(data)

update_prediction(
    st.session_state.fault_type
)


st.header("Engine Status")

if anomaly >= 0.70:
    engine_status = "CRITICAL"
elif anomaly >= 0.30:
    engine_status = "CAUTION"
else:
    engine_status = "NORMAL"


if st.session_state.mission_survival >= 80:
    mission_status = "GO"
elif st.session_state.mission_survival >= 50:
    mission_status = "CAUTION"
else:
    mission_status = "NO-GO"


status1, status2 = st.columns(2)

with status1:

    if engine_status == "NORMAL":
        st.success("ENGINE CONDITION\n\nNORMAL")
    elif engine_status == "CAUTION":
        st.warning("ENGINE CONDITION\n\nCAUTION")
    else:
        st.error("ENGINE CONDITION\n\nCRITICAL")


with status2:

    if mission_status == "GO":
        st.success("MISSION ASSESSMENT\n\nGO")
    elif mission_status == "CAUTION":
        st.warning("MISSION ASSESSMENT\n\nCAUTION")
    else:
        st.error("MISSION ASSESSMENT\n\nNO-GO")


st.header("Predictive Assessment")

p1, p2, p3, p4 = st.columns(4)

with p1:
    st.metric(
        "Engine Health Index",
        f"{st.session_state.health:.1f}%"
    )

with p2:
    st.metric(
        "Anomaly Index",
        f"{anomaly:.2f}"
    )

with p3:
    st.metric(
        "Estimated RUL",
        f"{st.session_state.rul:.1f} h"
    )

with p4:
    st.metric(
        "Mission Survival",
        f"{st.session_state.mission_survival:.1f}%"
    )


r1, r2 = st.columns(2)

with r1:

    with st.container(border=True):

        st.subheader("Remaining Useful Life")

        uncertainty = random.uniform(1.5, 3.0)

        st.write(
            f"RUL estimate: **{st.session_state.rul:.1f} h**"
        )

        st.write(
            f"Uncertainty: **± {uncertainty:.1f} h**"
        )

        st.write(
            f"Health index: **{st.session_state.health:.1f} / 100**"
        )

        st.progress(
            int(st.session_state.health)
        )


with r2:

    with st.container(border=True):

        st.subheader("Mission Reliability")

        st.write(
            "Mission survival probability: "
            f"**{st.session_state.mission_survival:.1f}%**"
        )

        st.write(
            f"Pre-flight decision: **{mission_status}**"
        )

        st.write(
            "Assessment based on current engine health "
            "and predicted degradation."
        )


st.header("Propulsion Telemetry")

t1, t2 = st.columns(2)


with t1:

    with st.container(border=True):

        st.subheader("Engine Operating Parameters")

        e1, e2 = st.columns(2)

        with e1:

            st.metric(
                "RPM",
                f"{data['rpm']:.0f}"
            )

            st.metric(
                "Fuel Flow",
                f"{data['fuel_flow']:.2f} L/h"
            )

            st.metric(
                "Oil Pressure",
                f"{data['oil_pressure']:.2f} bar"
            )

        with e2:

            st.metric(
                "Oil Temperature",
                f"{data['oil_temp']:.1f} °C"
            )

            st.metric(
                "Vibration RMS",
                f"{data['vibration']:.2f} mm/s"
            )

            st.metric(
                "Injection Timing",
                f"{data['injection_timing']:.1f}°"
            )


with t2:

    with st.container(border=True):

        st.subheader("Cylinder Thermal Condition")

        for i in range(4):

            cylinder = i + 1

            c1, c2, c3 = st.columns(3)

            with c1:
                st.write(f"**CYLINDER {cylinder}**")

            with c2:
                st.metric(
                    "CHT",
                    f"{data['cht'][i]:.0f} °C"
                )

            with c3:
                st.metric(
                    "EGT",
                    f"{data['egt'][i]:.0f} °C"
                )

with st.container(border=True):

    st.subheader("Electrical Subsystem")

    el1, el2 = st.columns(2)

    with el1:
        st.metric(
            "Battery Health",
            f"{data['battery_health']:.1f}%"
        )

    with el2:
        st.metric(
            "Alternator Health",
            f"{data['alternator_health']:.1f}%"
        )


st.header("Fault Assessment")

f1, f2 = st.columns(2)

with f1:

    with st.container(border=True):

        st.subheader("Causal Assessment")

        fault_name = FAULTS[
            st.session_state.fault_type
        ]

        st.write(
            f"Probable root cause: **{fault_name}**"
        )

        st.write(
            f"Anomaly index: **{anomaly:.2f}**"
        )

        if st.session_state.fault_type == "INJECTOR":

            st.write(
                "Affected area: **Fuel / combustion**"
            )

            st.write(
                "Observed evidence: cylinder EGT asymmetry, "
                "fuel-flow deviation and increased vibration."
            )

        elif st.session_state.fault_type == "MISFIRE":

            st.write(
                "Affected area: **Combustion**"
            )

            st.write(
                "Observed evidence: RPM reduction, cylinder "
                "EGT deviation and increased vibration."
            )

        elif st.session_state.fault_type == "COOLING":

            st.write(
                "Affected area: **Thermal management**"
            )

            st.write(
                "Observed evidence: elevated CHT/EGT "
                "and increased oil temperature."
            )

        elif st.session_state.fault_type == "LUBRICATION":

            st.write(
                "Affected area: **Lubrication system**"
            )

            st.write(
                "Observed evidence: reduced oil pressure, "
                "elevated oil temperature and vibration."
            )

        elif st.session_state.fault_type == "SENSOR":

            st.write(
                "Affected area: **Instrumentation**"
            )

            st.write(
                "Observed evidence: inconsistent telemetry "
                "channel behaviour."
            )

        elif st.session_state.fault_type == "COMBUSTION":

            st.write(
                "Affected area: **Combustion system**"
            )

            st.write(
                "Observed evidence: EGT variation, RPM "
                "deviation and vibration growth."
            )

        elif st.session_state.fault_type == "OVERHEATING":

            st.write(
                "Affected area: **Thermal system**"
            )

            st.write(
                "Observed evidence: increasing CHT/EGT "
                "and oil temperature."
            )

        elif st.session_state.fault_type == "VIBRATION":

            st.write(
                "Affected area: **Mechanical system**"
            )

            st.write(
                "Observed evidence: elevated vibration signature."
            )

        else:

            st.write(
                "Affected area: **None detected**"
            )

            st.write(
                "Observed evidence: telemetry remains within "
                "the simulated nominal operating state."
            )


# ------------------------------------------------------------
# RECOVERY RECOMMENDATION
# ------------------------------------------------------------

with f2:

    with st.container(border=True):

        st.subheader("Recovery Recommendation")

        recommendations = {

            "NONE":
                "Continue mission under current operating "
                "conditions while monitoring health trend.",

            "INJECTOR":
                "Reduce throttle and initiate recovery assessment.",

            "MISFIRE":
                "Reduce engine load and initiate recovery assessment.",

            "COOLING":
                "Reduce thermal loading and assess cooling condition.",

            "LUBRICATION":
                "Reduce engine load and initiate immediate "
                "recovery assessment.",

            "SENSOR":
                "Cross-check the affected telemetry channel "
                "against correlated engine parameters.",

            "COMBUSTION":
                "Reduce engine load and monitor combustion stability.",

            "OVERHEATING":
                "Reduce thermal loading and initiate "
                "recovery assessment.",

            "VIBRATION":
                "Reduce engine load and monitor vibration trend."
        }

        st.write(
            recommendations[
                st.session_state.fault_type
            ]
        )


if st.session_state.event_log:

    st.header("Event Log")

    with st.container(border=True):

        for event in st.session_state.event_log:

            st.write(
                f"`{event}`"
            )


if st.session_state.running:

    time.sleep(1)
    st.rerun()
