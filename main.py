from Vehicle import vehicle


if __name__ == '__main__':
    car=vehicle()
    #print(car.feul)
    #try:
     #   car.gear_shift(15)
    #except IndexError as i:
     #   print(i)
    #print(car.gear)
    #print(car.feul)
    try:
        car.km_to_drive(2500)
    except Exception as i:
         print (i)
    print(car.feul)
    #car.km_to_drive(100)
    #print(car.feul)
    #try:
     #   car.monney_to_fill(5)
    #except:
     #  print('not enogh money or feul capcity at max')
    #print(car.money)
    #print(car.feul)
    #try:
     #   car.monney_to_fill(10)
    #except:
     #   print('not enogh money or feul capcity at max')
    #print(car.money)
    #print(car.feul)

