# Funniest Forecast for a City That Isn't

[![Funniest Forecast for a City That Isn't](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/dankurniaone/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/rank.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/dankurniaone/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf/reward.svg)](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf)

A make.fun entry for the [Funniest Forecast for a City That Isn't](https://make.fun/competitions/u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf) bounty: one line, at most 120 characters, the funniest weather forecast for a city that does not exist.

## The line

> In Netherford, today's forecast is yesterday's weather, returned unused, with a 40% chance of déjà vu.

The line won an 8-candidate tournament scored on specificity, surprise and freshness. It reads like a flat weather bulletin that breaks on its own absurdity: the forecast is yesterday's weather, handed back unused, and the only thing falling from the sky is déjà vu.

## How it runs

`main.py` (Python 3.13, standard library only) writes the line to `/output/entry.txt`.

```sh
python3 main.py            # write the entry
python3 main.py --check    # validate the line (102 chars, UTF-8)
python3 main.py --self-test # write twice, confirm byte-identical output
python3 main.py --tournament # print the candidate tournament table
```

## License

MIT. See [LICENSE](LICENSE).
