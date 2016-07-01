path = '/home/becken/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
import json
from pandas import DataFrame, Series
records = [json.loads(line) for line in open(path)]
import pandas as pd
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
from pylab import *
tz_counts[:10].plot(kind='barh', rot=0)
