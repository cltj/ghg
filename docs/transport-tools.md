# Important fields


## 1 - scope, activity region
- source description
- region where the activity happens | (Required) | list[str]
- mode of transportation (Required) | list[str]
- scope (Required) | list[str|int]
- type of activity (Required) | list [str]


## 2 - vechicle and fuel
- vehicle type (Select or BYOV) | list [str]
- distance travelled | int
- units of measurement | list[str]
- freight weight | int or float
- number of passengers | int
- fuel used | list[str]
- fuel amount | int
- unit of fuel amount | list[str] -> calc


## 3 - ghg emission (output)
- Fossil fuels | metric tons | float
- ch4 | kilograms| float
- n2o | kilograms | float
- total ghg emission | metric tons CO2e | float
- biofuel co2 | metric tons | float

## 4 - Applied emission factors
- applied CO2 | KG CO2/liter | float
- applied CH4 | gram CH4/kilometer | float
- applied N2O | gram N2O/kilometer | float
- applied biofuel CO2 emissions factor | ? | float




 
