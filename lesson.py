# 型宣言せずに自動で型が設定される
# 変数名は頭文字に数字は入れない
num = '1'
name = 'Mike'
is_ok = True

new_num = int(num)

# type関数で型を見れる
print(num, type(num))
print(new_num, type(new_num))
print(name, type(name))
print(is_ok, type(is_ok))

# print関数は他に引数が設定できる
print('Hi', 'Mike', sep=',', end='\n')
print('Hi', 'Mike', sep=',', end='\n')

# rを付けると\も出力できる
print(r'www.udemy.com\course')

word = 'python'

# インデックス表示
print(word[0])
# スライスでインデックス表示
print(word[0:2])
print(word[:2])
print(word[2:])
print(word[:])

# 文字数
n = len(word)
print(n)

# 文字列判定
s = 'My name is Mike. Hi Mike'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

# 文字列関数
print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))
