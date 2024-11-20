import time
import threading


def calc_square(numbers):
    print("Calculate Square Numbers")
    for n in numbers:
        time.sleep(0.2)
        print(f'Square: {n*n}')


def calc_cube(numbers):
    print("Calculate Cube of Numbers")
    for n in numbers:
        ##time.sleep(0.2)
        print(f'Cube: {n*n*n}')


if __name__ == '__main__':
    arr = [2, 3, 8, 9]
    t = time.time()
    thred1 = threading.Thread(target=calc_square, args=(arr, ))
    thred2 = threading.Thread(target=calc_cube, args=(arr, ))
    thred1.start()
    thred2.start()
    thred1.join()
    thred2.join()
    print(f'Done in : {time.time() - t}')
    print("Hah ... I am done with all my works Now!")

