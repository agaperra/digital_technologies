from PIL import Image


# Возвращает диапазон, в котором находится value. Т.е. если в dict хранится
# 200, а затем 250, то при передаче, например, 225 в качестве значения value,
# функция вернет 200 и 250, т.к. 225 лежит между ними в dict.
# Функция используется для тех value, которые не содержатся в dict,
# для их последующей интерполяции
def get_range(my_dictionary, value):
    start = 0
    end = 0
    prev = 256

    for x in my_dictionary.keys():
        if value < x:
            if prev < value:
                end = x
                start = prev
                return start, end
        prev = x

    return start, end


# Вычисляет новое значение пикселя. Value - текущее значение пикселя
# Если value уже находится в dict, то функция возвращает соответсвующее ему
# гаммированное значение. Иначе с помощью функции getRange вычисляется диапазон,
# в котором находится value, считываются гаммированные значения начала и конца
# диапазона и вычисляется гаммированное значение value с помощью линейной интерполяции.
def calculate_value(my_dictionary, value):
    if value in my_dictionary:
        return my_dictionary[value]
    start, end = get_range(my_dictionary, value)
    alpha = (value - start) / (end - start)
    res = alpha * (my_dictionary[end] - my_dictionary[start]) + my_dictionary[start]
    return int(res)


image = Image.open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.jpg")
w, h = image.size
print(w, h)
image_bytes = image.tobytes()
data_bytes = bytearray(image_bytes)


# Для одной гаммы
gamma = 1 / 2.0
dictionary_for_gamma = dict()


# Заполнение таблицы для гаммы
for x in range(0, 255, 16):
    dictionary_for_gamma[x] = int(pow((x / 255.0), gamma) * 255.0)
dictionary_for_gamma[255] = int(pow((255.0 / 255.0), gamma) * 255.0)


# Вспомогательная переменная - таблица для выбранной гаммы
currentDict = dictionary_for_gamma

# computations
for y in range(0, h * 3):
    for x in range(0, w, 3):
        # Считывание значений пикселей
        r = data_bytes[y * w + x + 0]
        if (y * w + x + 1) != len(data_bytes) & (y * w + x + 2) != len(data_bytes):
            g = data_bytes[y * w + x + 1]
            b = data_bytes[y * w + x + 2]
        else:
            g = data_bytes[y * w + x + 0]
            b = data_bytes[y * w + x + 0]

        # Вычисление нового значения
        r = calculate_value(currentDict, r)
        g = calculate_value(currentDict, g)
        b = calculate_value(currentDict, b)

        # Запись результата
        data_bytes[y * w + x + 0] = r
        if (y * w + x + 1) != len(data_bytes) & (y * w + x + 2) != len(data_bytes):
            data_bytes[y * w + x + 1] = g
            data_bytes[y * w + x + 2] = b
        else:
            data_bytes[y * w + x + 0] = g
            data_bytes[y * w + x + 0] = b

result = bytes(data_bytes)
image_out = Image.frombytes('RGB', (w, h), result)
image_out.save(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\imageSecond.png", 'png')
