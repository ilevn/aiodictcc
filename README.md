## aiodictcc

An `asnycio`-based  wrapper for [Dict.cc](http://dict.cc).

## Installation
```
pip install aiodictcc
```
For the latest development version:
```
pip install git+https://github.com/ilevn/aiodictcc
```
## Example

```py
import asyncio
from aiodictcc import Translate

# Create a new instance of the API wrapper.
trans = Translate()
loop = asyncio.get_event_loop()

async def main():
    to_translate = input("Search: ")
    # Get translation for `to translate` en -> de.
    translated = await trans.get_translation(to_translate, "en", "de")
    # Returns a list of tuples.
    print(translated)

loop.run_until_complete(main())
```