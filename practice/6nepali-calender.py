from datetime import date, timedelta

# Base reference: Jan 1, 1944 AD = 2000-09-17 BS
BASE_AD = date(2025, 6, 24)
BASE_BS = [2082, 3, 10]  # [year, month, day]

# Month data for BS years (partial sample: 2000–2002)
bs_month_data = {
    #  2080: [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 29, 30],
    # 2081: [31, 31, 32, 31, 31, 30, 30, 30, 29, 30, 30, 30],
    2082: [31, 31, 32, 31, 31, 31, 30, 29, 30, 29, 30, 30]
    # Add more years as needed
}

def ad_to_bs(ad_date):
    days_diff = (ad_date - BASE_AD).days
    bs_year, bs_month, bs_day = BASE_BS

    while days_diff > 0:
        days_in_month = bs_month_data[bs_year][bs_month - 1]
        if days_diff >= 1:
            bs_day += 1
            days_diff -= 1
            if bs_day > days_in_month:
                bs_day = 1
                bs_month += 1
                if bs_month > 12:
                    bs_month = 1
                    bs_year += 1
                    if bs_year not in bs_month_data:
                        raise ValueError("BS year data not available")
    return f"{bs_year}-{bs_month:02d}-{bs_day:02d}"

# Example usage
today_ad = date.today()
today_bs = ad_to_bs(today_ad)
print("Today's Nepali date (BS):", today_bs)