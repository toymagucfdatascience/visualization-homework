import pandas as pd

df = pd.read_csv('cities.csv')
df.head()
Out[2]:
City_ID	City	Cloudiness	Country	Date	Humidity	Lat	Lng	Max Temp	Wind Speed
0	0	jacareacanga	0	BR	1528902000	62	-6.22	-57.76	89.60	6.93
1	1	kaitangata	100	NZ	1528905304	94	-46.28	169.85	42.61	5.64
2	2	goulburn	20	AU	1528905078	91	-34.75	149.72	44.32	10.11
3	3	lata	76	IN	1528905305	89	30.78	78.62	59.89	0.94
4	4	chokurdakh	0	RU	1528905306	88	70.62	147.90	32.17	2.95
In [3]:
html_table = df.to_html()
html_table