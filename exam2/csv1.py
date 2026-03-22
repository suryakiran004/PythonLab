import pandas as pd

data = {
    'name' : ['Anandhu' , 'Thatha' , 'ponni' , 'Devu'],
    'age' : [21 , 19 , 18 , 19] ,
    'city' : ['Alappuzha' , 'kozhikode' , 'Thrisur' , 'Ekm']
}

df = pd.DataFrame(data)
df.to_csv('student.csv' , index=False)