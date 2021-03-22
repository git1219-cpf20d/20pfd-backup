print('편집 창 선택 후 F1 키를 누르고 open shell 선택하면 bash 사용 가능합니다')
print('각자 실습 저장소를 clone 하여 실습 후 push 바랍니다')
print('repl.it 작업공간이 가끔 몇분 전 과거 상태로 돌아갈 수 있으니 자주 git push 바랍니다.')

print("실습실에서 repl.it 실습 마친 후 반드시 logout 바랍니다.")

import pylab as py
x = py.linspace(-5, 5)
y = x + py.cos(x) + 0.1 * py.randn(x.shape[0])

py.plot(x, y)
py.grid(True)

py.savefig('test.svg')
