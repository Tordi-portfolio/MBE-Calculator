from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def underground_withdrawal(request):

    result = None
    unit = ""

    if request.method == "POST":

        Np = float(request.POST.get('Np'))
        Bo = float(request.POST.get('Bo'))
        Rp = float(request.POST.get('Rp'))
        Rs = float(request.POST.get('Rs'))
        Bg = float(request.POST.get('Bg'))
        Wp = float(request.POST.get('Wp'))
        Bw = float(request.POST.get('Bw'))

        F = (Np * (Bo + ((Rp - Rs) * Bg))) + (Wp * Bw)

        result = round(F, 4)
        unit = "STB"

    return render(
        request,
        'underground_withdrawal.html',
        {'result': result, 'unit': unit}
    )


# OIL EXPANSION
def oil_expansion(request):

    result = None
    unit = ""

    if request.method == "POST":

        Bo = float(request.POST.get("Bo"))
        Boi = float(request.POST.get("Boi"))

        Eo = Bo - Boi

        result = round(Eo, 6)
        unit = "RB/STB"

    return render(
        request,
        "oil_expansion.html",
        {"result": result, "unit": unit}
    )


# GAAS CAP 
def gas_cap_expansion(request):

    result = None
    unit = ""

    if request.method == "POST":

        Boi = float(request.POST.get("Boi"))
        Bg = float(request.POST.get("Bg"))
        Bgi = float(request.POST.get("Bgi"))

        Eg = Boi * ((Bg / Bgi) - 1)

        result = round(Eg, 6)
        unit = "RB/STB"

    return render(
        request,
        "gas_cap_expansion.html",
        {"result": result, "unit": unit}
    )


def formation_water_expansion(request):

    result = None
    unit = ""

    if request.method == "POST":

        Boi = float(request.POST.get("Boi"))
        cf = float(request.POST.get("cf"))

    if request.method == "POST":

        Boi = float(request.POST.get("Boi"))
        cf = float(request.POST.get("cf"))
        cw = float(request.POST.get("cw"))
        Swi = float(request.POST.get("Swi"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))

        dP = Pi - P

        Efw = Boi * ((cf + (cw * Swi)) * dP) / (1 - Swi)

        result = round(Efw, 6)
        unit = "STB"

    return render(
        request,
        "formation_water_expansion.html",
        {"result": result, "unit": unit}
    )



def general_mbe(request):

    result = None
    unit = ""

    if request.method == "POST":

        F = float(request.POST.get("F"))
        Eo = float(request.POST.get("Eo"))
        Eg = float(request.POST.get("Eg"))
        Efw = float(request.POST.get("Efw"))
        m = float(request.POST.get("m"))
        We = float(request.POST.get("We"))
        Bw = float(request.POST.get("Bw"))

        numerator = F - (We * Bw)
        denominator = Eo + (m * Eg) + Efw

        if denominator != 0:
            N = numerator / denominator
        else:
            N = 0

        result = round(N, 4)
        unit = ""

    return render(
        request,
        "general_mbe.html",
        {"result": result, "unit": unit}
    )



def gas_fvf(request):

    result = None
    unit = ""

    if request.method == "POST":

        Z = float(request.POST.get("Z"))
        T = float(request.POST.get("T"))
        P = float(request.POST.get("P"))

        Bg = (0.02827 * Z * T) / P

        result = round(Bg, 6)
        unit = "RB/SCF"

    return render(
        request,
        "gas_fvf.html",
        {"result": result, "unit": unit}
    )


def gas_cap_ratio(request):

    result = None
    unit = ""

    if request.method == "POST":

        Vg = float(request.POST.get("Vg"))
        Vo = float(request.POST.get("Vo"))

        if Vo != 0:
            m = Vg / Vo
        else:
            m = 0

        result = round(m, 6)
        unit = ""
    return render(
        request,
        "gas_cap_ratio.html",
        {"result": result, "unit": unit}
    )



def recovery_factor(request):

    result = None
    unit = ""

    if request.method == "POST":

        Np = float(request.POST.get("Np"))
        N = float(request.POST.get("N"))

        if N != 0:
            RF = (Np / N) * 100
        else:
            RF = 0

        result = round(RF, 4)
        unit = "%"

    return render(
        request,
        "recovery_factor.html",
        {"result": result, "unit": unit}
    )



def ogip(request):

    result = None
    unit = ""

    if request.method == "POST":

        P = float(request.POST.get("P"))
        V = float(request.POST.get("V"))
        Z = float(request.POST.get("Z"))
        T = float(request.POST.get("T"))

        if Z != 0 and T != 0:
            G = (P * V) / (Z * T)
        else:
            G = 0

        result = round(G, 4)
        unit = "MSCF"
    return render(
        request,
        "ogip.html",
        {"result": result, "unit": unit}
    )


def schilthuis_water_influx(request):

    result = None
    unit = ""

    if request.method == "POST":

        C = float(request.POST.get("C"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))

        We = C * (Pi - P)

        result = round(We, 4)
        unit = "STB"

    return render(
        request,
        "schilthuis.html",
        {"result": result, "unit": unit}
    )


def van_everdingen_hurst(request):

    result = None
    unit = ""

    if request.method == "POST":

        C = float(request.POST.get("C"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))
        dt = float(request.POST.get("dt"))
        n = int(request.POST.get("n"))

        # simplified cumulative approach
        We = C * (Pi - P) * dt * n

        result = round(We, 4)
        unit = "STB"

    return render(
        request,
        "van_everdingen_hurst.html",
        {"result": result, "unit": unit}
    )


import math

def fetkovich_water_influx(request):

    result = None
    unit = ""

    if request.method == "POST":

        C = float(request.POST.get("C"))
        alpha = float(request.POST.get("alpha"))
        t = float(request.POST.get("t"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))

        We = C * (1 - math.exp(-alpha * t)) * (Pi - P)

        result = round(We, 4)
        unit = "STB"

    return render(
        request,
        "fetkovich.html",
        {"result": result, "unit": unit}
    )


def gas_material_balance(request):

    result = None
    unit = ""

    if request.method == "POST":

        p = float(request.POST.get("p"))
        z = float(request.POST.get("z"))
        pi = float(request.POST.get("pi"))
        zi = float(request.POST.get("zi"))
        Gp = float(request.POST.get("Gp"))

        denominator = 1 - ((p / z) / (pi / zi))

        if denominator != 0:
            G = Gp / denominator
        else:
            G = 0

        result = round(G, 4)
        unit = ""

    return render(
        request,
        "gas_material_balance.html",
        {"result": result, "unit": unit}
    )


def volumetric_oil_reservoir(request):

    result = None
    unit = ""

    if request.method == "POST":

        A = float(request.POST.get("A"))
        h = float(request.POST.get("h"))
        phi = float(request.POST.get("phi"))
        Swi = float(request.POST.get("Swi"))
        Boi = float(request.POST.get("Boi"))

        N = (7758 * A * h * phi * (1 - Swi)) / Boi

        result = round(N, 2)
        unit = "STB"
    return render(
        request,
        "volumetric_oil_reservoir.html",
        {"result": result, "unit": unit}
    )


def gas_cap_drive_reservoir(request):

    result = None
    unit = ""

    if request.method == "POST":

        F = float(request.POST.get("F"))
        Eo = float(request.POST.get("Eo"))
        Eg = float(request.POST.get("Eg"))
        m = float(request.POST.get("m"))

        denominator = Eo + (m * Eg)

        if denominator != 0:
            N = F / denominator
        else:
            N = 0

        result = round(N, 2)
        unit = "STB"

    return render(
        request,
        "gas_cap_drive_reservoir.html",
        {"result": result, "unit": unit}
    )


def water_drive_reservoir(request):

    result = None
    unit = ""

    if request.method == "POST":

        F = float(request.POST.get("F"))
        We = float(request.POST.get("We"))
        Bw = float(request.POST.get("Bw"))
        Eo = float(request.POST.get("Eo"))

        denominator = Eo

        if denominator != 0:
            N = (F - (We * Bw)) / denominator
        else:
            N = 0

        result = round(N, 2)
        unit = "STB"

    return render(
        request,
        "water_drive_reservoir.html",
        {"result": result, "unit": unit}
    )


def combination_drive_reservoir(request):

    result = None
    unit = ""

    if request.method == "POST":

        F = float(request.POST.get("F"))
        We = float(request.POST.get("We"))
        Bw = float(request.POST.get("Bw"))
        Eo = float(request.POST.get("Eo"))
        Eg = float(request.POST.get("Eg"))
        Efw = float(request.POST.get("Efw"))
        m = float(request.POST.get("m"))

        numerator = F - (We * Bw)
        denominator = Eo + (m * Eg) + Efw

        if denominator != 0:
            N = numerator / denominator
        else:
            N = 0

        result = round(N, 2)
        unit = "STB"

    return render(
        request,
        "combination_drive_reservoir.html",
        {"result": result, "unit": unit}
    )


def oil_expansion_term(request):

    result = None
    unit = ""

    if request.method == "POST":

        Bo = float(request.POST.get("Bo"))
        Boi = float(request.POST.get("Boi"))
        Rs = float(request.POST.get("Rs"))
        Rsi = float(request.POST.get("Rsi"))
        Bg = float(request.POST.get("Bg"))

        Eo = (Bo - Boi) + ((Rs - Rsi) * Bg)

        result = round(Eo, 6)
        unit = ""
    return render(
        request,
        "oil_expansion_term.html",
        {"result": result, "unit": unit}
    )


def oil_fvf(request):

    result = None
    unit = ""

    if request.method == "POST":

        V_res = float(request.POST.get("V_res"))
        V_st = float(request.POST.get("V_st"))

        if V_st != 0:
            Bo = V_res / V_st
        else:
            Bo = 0

        result = round(Bo, 6)
        unit = "bbl/STB"
    return render(
        request,
        "oil_fvf.html",
        {"result": result, "unit": unit}
    )



def unit_converter(request):

    result = None
    unit = ""

    if request.method == "POST":

        value = float(request.POST.get("value"))
        conversion_type = request.POST.get("conversion_type")

        # =========================
        # PRESSURE
        # =========================
        if conversion_type == "psi_to_kpa":
            result = value * 6.89476
            unit = "kPa"

        elif conversion_type == "kpa_to_psi":
            result = value / 6.89476
            unit = "psi"

        elif conversion_type == "bar_to_psi":
            result = value * 14.5038
            unit = "psi"

        elif conversion_type == "psi_to_bar":
            result = value / 14.5038
            unit = "bar"

        elif conversion_type == "atm_to_psi":
            result = value * 14.696

        elif conversion_type == "psi_to_atm":
            result = value / 14.696

        # =========================
        # TEMPERATURE
        # =========================
        elif conversion_type == "f_to_r":
            result = value + 459.67
            unit = "°R"

        elif conversion_type == "r_to_f":
            result = value - 459.67
            unit = "°F"

        elif conversion_type == "c_to_k":
            result = value + 273.15
            unit = "K"

        elif conversion_type == "k_to_c":
            result = value - 273.15
            unit = "°C"

        # =========================
        # OIL VOLUME
        # =========================
        elif conversion_type == "m3_to_bbl":
            result = value * 6.28981
            unit = "bbl"

        elif conversion_type == "bbl_to_m3":
            result = value / 6.28981
            unit = "m³"

        elif conversion_type == "bbl_to_stb":
            result = value  # equivalent
            unit = "STB"

        elif conversion_type == "stb_to_bbl":
            result = value  # equivalent
            unit = "bbl"

        # =========================
        # GAS VOLUME
        # =========================
        elif conversion_type == "scf_to_m3":
            result = value * 0.0283168
            unit = "m³"

        elif conversion_type == "m3_to_scf":
            result = value / 0.0283168
            unit = "scf"

        elif conversion_type == "mscf_to_scf":
            result = value * 1000
            unit = "scf"

        elif conversion_type == "scf_to_mscf":
            result = value / 1000
            unit = "Mscf"

        elif conversion_type == "mmscfto_scf":
            result = value * 1_000_000
            unit = "scf"

        elif conversion_type == "scf_to_mmscft":
            result = value / 1_000_000
            unit = "MMscf"

        # =========================
        # RESERVOIR VOLUME
        # =========================
        elif conversion_type == "acreft_to_bbl":
            result = value * 7758
            unit = "bbl"

        elif conversion_type == "bbl_to_acreft":
            result = value / 7758
            unit = "m³"

        elif conversion_type == "acreft_to_m3":
            result = value * 1233.48
            unit = "acre-ft"

        elif conversion_type == "m3_to_acreft":
            result = value / 1233.48
            unit = "acre-ft"

        # =========================
        # PVT PROPERTIES (NORMALIZATION HELP)
        # =========================
        elif conversion_type == "psi_to_pa":
            result = value * 6894.76

        elif conversion_type == "pa_to_psi":
            result = value / 6894.76

        else:
            result = "Invalid conversion type..."

    return render(request, "converter/unit_converter.html", {"result": result, "unit": unit})


def unit_reference(request):
    return render(request, "converter/unit_reference_table.html")