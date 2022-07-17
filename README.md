# Covid-API
A Python API to get statistics about COVID-19's cases, recoveries and deaths.
# Requirements
• BS4 installed
# Usage
**Getting the World's in total cases, recoveries and deaths:**
```python
from covid import Covid

covid = Covid()
print(covid.total())
```
**Getting country specific data**
```python
from covid import Covid

covid = Covid()
print(covid.country("USA"))
```
