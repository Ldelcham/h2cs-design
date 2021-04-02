
# base class for PV inspired from REoptLite
class PV_Base(object):
    def __init__(
        self,
        tilt = 360.0,
        array_type = 1,
        module_type= 0,
        losses = 0.14,
        azimuth = 180.0,
        name = "PV",
        location = "both",
        existing_kw = 0.0,
        min_kw = 0.0,
        max_kw = 1.0e5,
        cost_per_kw = 1600.0,
        om_cost_per_kw = 16.0,
        degradation_pct = 0.005,
        macrs_option_years = 5,
        macrs_bonus_pct = 1.0,
        macrs_itc_reduction = 0.5,
        total_itc_pct = 0.26,
        total_rebate_per_kw = 0.0,
        kw_per_square_foot=0.01,
        acres_per_kw=6e-3,
        inv_eff=0.96,
        dc_ac_ratio=1.2):
        
        self.tilt = tilt
        self.array_type = array_type
        self.module_type = module_type
        self.losses = losses
        self.azimuth = azimuth
        self.name = name
        self.location = location
        self.existing_kw = existing_kw
        self.min_kw = min_kw
        self.max_kw = max_kw
        self.cost_per_kw = cost_per_kw
        self.om_cost_per_kw = om_cost_per_kw
        self.degradation_pct = degradation_pct
        self.macrs_option_years = macrs_option_years
        self.macrs_bonus_pct = macrs_bonus_pct
        self.macrs_itc_reduction = macrs_itc_reduction
        self.total_itc_pct = total_itc_pct
        self.total_rebate_per_kw = total_rebate_per_kw
        self.kw_per_square_foot = kw_per_square_foot
        self.acres_per_kw = acres_per_kw
        self.inv_eff = inv_eff
        self.dc_ac_ratio = dc_ac_ratio

        # validate inputs
        invalid_args = []

        if len(invalid_args)>0:
            err_msg = "Invalid argument values: {}".format(invalid_args)
            raise Exception(err_msg)