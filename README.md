# Covid-API
A Python API to get statistics about COVID-19's cases, recoveries and deaths.
# Requirements
• Python 3 installed</br >
• BS4 installed via pip
# Usage
**Getting the World's in total cases, recoveries and deaths:**
```python
from covid import Covid

covid = Covid()
print(covid.total())
```
It'll output this (data will be incorrect due to new cases and such):
```{'name': 'World', 'cases': 181848442, 'deaths': 3938478, 'recovered': 166329519}```
</br >
**Getting country specific data**
```python
from covid import Covid

covid = Covid()
print(covid.country("USA"))
```
It'll output this (data will be incorrect due to new cases and such):
```{'name': 'USA', 'cases': 34494575, 'deaths': 619434, 'recovered': 28927335}```
</br >
For what countries are supported, check the nations from https://www.worldometers.info/coronavirus/.


