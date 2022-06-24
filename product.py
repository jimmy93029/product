products = []
import os

#讓使用者輸入
def user_input(products):
  while True :
    name = input('請輸入商品')
    if name =='q':
      break
    price = input('請輸入商品價格')
    products.append([name, price])
  print(products)
  return products



#印出購買明細
def print_product(products):
  for p in products:
    print( p[0], '的價格是', p[1])



#寫入購買清單
def write_file(filename, products):
  with open(filename,'w',encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
      f.write(p[0] + ',' + p[1] + '\n')



#檢查檔案是否存在
def main(filename):
  if os.path.isfile(filename):
      print('成功讀取檔案')
      read_file(filename)
  else:
      print('找不到檔案')



#讀取檔案
def read_file(filename):
  with open(filename,'r',encoding = 'utf-8') as f:
    for line in f :
      if '商品,價格/n' in line:
        continue
      else:
        name, price = line.strip().split(',')
        products.append([name, price]) 
      print(line)
    print(products)
  return products


main(input('請輸入要查詢的檔案'))
