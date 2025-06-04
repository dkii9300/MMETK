def calculate_clo_mcr(mcr_kw, clo_rate_per_cyl, num_cyl):
    return mcr_kw / 1000 * clo_rate_per_cyl * num_cyl

def calculate_sfoc(fuel_consumed_kg, power_output_kw, hours):
    return (fuel_consumed_kg / (power_output_kw * hours)) * 1e6

def calculate_eexi(mcr_kw, sfoc_g_kwh, dwt, vref_knots):
    cf = 3.114  # for HFO
    return (mcr_kw * sfoc_g_kwh * cf) / (dwt * vref_knots)
