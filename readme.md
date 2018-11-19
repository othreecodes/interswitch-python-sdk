# Usage

```python

api = InterSwitchAPI(
            client_secret="FTbMeBD7MtkGBQJw1XoM74NaikuPL13Sxko1zb0DMjI=",
            client_id="IKIAF6C068791F465D2A2AA1A3FE88343B9951BAC9C3",
            env=Constants.ENV_SANDBOX,
            terminal_id="3ERT0001",
        )

result = api.get_billers()

print(result)
```