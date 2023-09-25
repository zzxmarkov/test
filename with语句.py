# 2021-04-24  15:16
class mmm:
    def __enter__(self):
        print('enter方法')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法')

    def show(self):
        print('哈哈')


with mmm() as a:
    a.show()







