def myfunc(**kwargs):
    if 'model' in kwargs:
      print(f'the model received is {kwargs["model"]}')

myfunc(brand='Ford', year = '1964', model = 'mustang')