from django.shortcuts import render

def home(request):
    return render(request, 'home.html')


def underground_withdrawal(request):

    result = None

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

    return render(
        request,
        'underground_withdrawal.html',
        {'result': result}
    )


# OIL EXPANSION
def oil_expansion(request):

    result = None

    if request.method == "POST":

        Bo = float(request.POST.get("Bo"))
        Boi = float(request.POST.get("Boi"))

        Eo = Bo - Boi

        result = round(Eo, 6)

    return render(
        request,
        "oil_expansion.html",
        {"result": result}
    )


# GAAS CAP 
def gas_cap_expansion(request):

    result = None

    if request.method == "POST":

        Boi = float(request.POST.get("Boi"))
        Bg = float(request.POST.get("Bg"))
        Bgi = float(request.POST.get("Bgi"))

        Eg = Boi * ((Bg / Bgi) - 1)

        result = round(Eg, 6)

    return render(
        request,
        "gas_cap_expansion.html",
        {"result": result}
    )


def formation_water_expansion(request):

    result = None

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

    return render(
        request,
        "formation_water_expansion.html",
        {"result": result}
    )



def general_mbe(request):

    result = None

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

    return render(
        request,
        "general_mbe.html",
        {"result": result}
    )



def gas_fvf(request):

    result = None

    if request.method == "POST":

        Z = float(request.POST.get("Z"))
        T = float(request.POST.get("T"))
        P = float(request.POST.get("P"))

        Bg = (0.02827 * Z * T) / P

        result = round(Bg, 6)

    return render(
        request,
        "gas_fvf.html",
        {"result": result}
    )


def gas_cap_ratio(request):

    result = None

    if request.method == "POST":

        Vg = float(request.POST.get("Vg"))
        Vo = float(request.POST.get("Vo"))

        if Vo != 0:
            m = Vg / Vo
        else:
            m = 0

        result = round(m, 6)

    return render(
        request,
        "gas_cap_ratio.html",
        {"result": result}
    )



def recovery_factor(request):

    result = None

    if request.method == "POST":

        Np = float(request.POST.get("Np"))
        N = float(request.POST.get("N"))

        if N != 0:
            RF = (Np / N) * 100
        else:
            RF = 0

        result = round(RF, 4)

    return render(
        request,
        "recovery_factor.html",
        {"result": result}
    )



def ogip(request):

    result = None

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

    return render(
        request,
        "ogip.html",
        {"result": result}
    )


def schilthuis_water_influx(request):

    result = None

    if request.method == "POST":

        C = float(request.POST.get("C"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))

        We = C * (Pi - P)

        result = round(We, 4)

    return render(
        request,
        "schilthuis.html",
        {"result": result}
    )


def van_everdingen_hurst(request):

    result = None

    if request.method == "POST":

        C = float(request.POST.get("C"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))
        dt = float(request.POST.get("dt"))
        n = int(request.POST.get("n"))

        # simplified cumulative approach
        We = C * (Pi - P) * dt * n

        result = round(We, 4)

    return render(
        request,
        "van_everdingen_hurst.html",
        {"result": result}
    )


import math

def fetkovich_water_influx(request):

    result = None

    if request.method == "POST":

        C = float(request.POST.get("C"))
        alpha = float(request.POST.get("alpha"))
        t = float(request.POST.get("t"))
        Pi = float(request.POST.get("Pi"))
        P = float(request.POST.get("P"))

        We = C * (1 - math.exp(-alpha * t)) * (Pi - P)

        result = round(We, 4)

    return render(
        request,
        "fetkovich.html",
        {"result": result}
    )