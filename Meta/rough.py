def seasonalPattern(seasonTime):
    dataPattern = np.where(
        seasonTime < 0.4,
        np.cos(seasonTime * 2 * np.pi),
        1 / np.exp(3 * seasonTime),
    )

    return dataPattern


def seasonality(time, period, amplitude=1, phase=0):
    seasonTime = ((time + phase) % period) / period

    dataPattern = amplitude * seasonalPattern(seasonTime=seasonTime)

    return dataPattern
