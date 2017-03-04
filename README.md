## aiodictcc

An `asnycio`-based  wrapper for [Dict.cc](http://dict.cc).

## Installation

```
pip install git+https://github.com/ilevn/aiodictcc.git
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
    # Query dict.cc.
    await trans.
    # Get translation for `word` en -> de.
    translated = await trans.get_translation("word", "en", "de")
    # Returns a list of tuples.
    print(translated)

loop.run_until_complete(main())
```