# converting present value to future.
def p_to_f(nper, rate, present_value=1):

    future_value = present_value*((1+rate)**nper)

    return future_value


# converting future value to present.
def f_to_p(nper, rate, future_value=1):

    present_value = future_value/((1+rate)**nper)

    return present_value


# converting annual payment to present.
def a_to_p(nper, rate, annual_payment=1):

    factor = (((1+rate)**nper) - 1)/(rate*((1+rate)**nper))
    present_value = annual_payment*factor

    return present_value


# converting present value to annual payment.
def p_to_a(nper, rate, present_value=1):

    factor = (rate*((1+rate)**nper)) / (((1+rate)**nper) - 1)
    annual_payment = present_value*factor

    return annual_payment


# converting annual payment to future.
def a_to_f(nper, rate, annual_payment=1):

    factor = (((1+rate)**nper)-1) / rate
    future_value = annual_payment*factor

    return future_value


# converting future value to annual payment.
def f_to_a(nper, rate, future_value=1):

    factor = rate/(((1+rate)**nper)-1)
    annual_payment = future_value*factor

    return annual_payment


# converting G to present value.
def g_to_p(nper, rate, g):

    factor_pt1 = (((1+rate)**nper)-1) / (((1+rate)**nper)*rate)
    factor_pt2 = nper/((1+rate)**nper)
    factor = (factor_pt1 - factor_pt2)/rate
    present_value = g*factor

    return present_value


# converting present value to G.
def p_to_g(nper, rate, present_value):
    factor_pt1 = (((1 + rate) ** nper) - 1) / (((1 + rate) ** nper) * rate)
    factor_pt2 = nper / ((1 + rate) ** nper)
    factor = (factor_pt1 - factor_pt2) / rate
    g = present_value / factor

    return g


# converting G to annual payment.
def g_to_a(nper, rate, g):

    factor_pt1 = 1/rate
    factor_pt2 = nper/(((1+rate)**nper)-1)
    factor = factor_pt1 - factor_pt2
    annual_payment = g*factor

    return annual_payment


# converting annual payment to G.
def a_to_g(nper, rate, annual_payment):

    factor_pt1 = 1 / rate
    factor_pt2 = nper / (((1 + rate) ** nper) - 1)
    factor = factor_pt1 - factor_pt2
    g = annual_payment / factor

    return g


# converting G to future value.
def g_to_f(nper, rate, g):

    factor_pt1 = (((1+rate)**nper)-1)/(rate**nper)
    factor_pt2 = nper/rate
    factor = factor_pt1 - factor_pt2
    future_value = g*factor

    return future_value


# converting future value to G.
def f_to_g(nper, rate, future_value):
    factor_pt1 = (((1 + rate) ** nper) - 1) / (rate ** nper)
    factor_pt2 = nper / rate
    factor = factor_pt1 - factor_pt2
    g = future_value / factor

    return g


# converting geometric to present value.
def geo_to_p(nper, rate, change_percent, a1):

    if rate == change_percent:
        factor = nper / (1+rate)
        present_value = a1 * factor

        return present_value

    else:
        factor_pt1 = 1 - (((1+change_percent)**nper) * ((1+rate)**(-1 * nper)))
        factor_pt2 = rate - change_percent
        factor = factor_pt1 / factor_pt2
        present_value = a1 * factor

        return present_value



