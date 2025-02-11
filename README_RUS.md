# SmartCalc 


В данном проекте тебе предстоит реализовать на языке программирования Python расширенную версию обычного калькулятора.


### Паттерн MVP

Паттерн MVP имеет два общих компонента с MVC: модель и представление. Но он заменяет контроллер на презентер.

Презентер реализует взаимодействие между моделью и представлением. Когда представление уведомляет презентер, что пользователь что-то сделал (например, нажал кнопку), презентер принимает решение об обновлении модели и синхронизирует все изменения между моделью и представлением. Однако презентер не общается с представлением напрямую, а делает это через интерфейс. Благодаря чему все компоненты приложения впоследствии могут быть протестированы по отдельности.


## Part 1. Реализация SmartCalc v3.0

Тебе необходимо реализовать SmartCalc v3.0:

- Программа должна быть разработана на языке Python версии 3.11.
- Код программы должен находиться в папке src.
- При написании кода придерживайся Google Code Style.
- Необходимо разработать десктопное приложение.
- Подготовь установщик, который будет устанавливать приложение в систему со стандартными настройками (путь инсталляции, создание ярлыка).
- Подготовь реализацию с графическим пользовательским интерфейсом или под Linux, или под Mac OS, на базе любой GUI-библиотеки или фреймворка (допустима реализация слоя GUI на HTML/CSS/JS).
- Программа должна быть реализована с использованием паттерна MVVМ или MVP, а также:
    - не должно быть кода бизнес-логики в коде представлений;
    - не должно быть кода интерфейса в модели, презентере и модели представления.
- «Ядро» калькулятора в виде алгоритма формирования и вычисления польской нотации и различных вычислительных функций подключить в виде динамической библиотеки на C/C++ из проектов SmartCalc v1.0 или SmartCalc v2.0.
- Модель должна представлять собой «Ядро» с оберткой на языке Python.
- В модель должны быть вынесены все функциональные возможности калькулятора таким образом, чтобы в будущем ее можно было использовать без остальных слоев.
- Подготовь полное покрытие unit-тестами методов, находящихся в слое модели.
- В приложении должен быть реализован раздел справки с описанием интерфейса программы в произвольной форме.
- Программа должна хранить историю операций, позволять загружать выражения из истории и очищать историю целиком.
- История должна сохраняться между запусками приложения.
- На вход программы могут подаваться как целые числа, так и вещественные числа, записанные и через точку, и в экспоненциальной форме записи.
- Вычисление должно производится после полного ввода вычисляемого выражения и нажатия на символ `=`.
- Вычисление произвольных скобочных арифметических выражений должно происходить в инфиксной нотации.
- Вычисление произвольных скобочных арифметических выражений должно происходить в инфиксной нотации с подстановкой значения переменной _x_ в виде числа.
- Построй график функции, заданной с помощью выражения в инфиксной нотации с переменной _x_ (с координатными осями, отметкой используемого масштаба и сеткой с адаптивным шагом):
    - Не нужно предоставлять пользователю возможность менять масштаб.
- Область определения и область значения функций ограничиваются по крайней мере числами от -1000000 до 1000000:
    - Для построения графиков функции дополнительно укажи отображаемые область определения и область значения.
- Проверяемая точность дробной части — минимум 7 знаков после запятой.
- У пользователя должна быть возможность ввода до 255 символов.
- Скобочные арифметические выражения в инфиксной нотации должны поддерживать следующие арифметические операции и математические функции:
    - **Арифметические операторы**:

      | Название оператора | Инфиксная нотация <br /> (Классическая) | Префиксная нотация <br /> (Польская нотация) |  Постфиксная нотация <br /> (Обратная польская нотация) |
      | ------ | ------ | ------ | ------ |
      | Скобки | (a + b) | (+ a b) | a b + |
      | Сложение | a + b | + a b | a b + |
      | Вычитание | a - b | - a b | a b - |
      | Умножение | a * b | * a b | a b * |
      | Деление | a / b | / a b | a b \ |
      | Возведение в степень | a ^ b | ^ a b | a b ^ |
      | Остаток от деления | a mod b | mod a b | a b mod |
      | Унарный плюс | +a | +a | a+ |
      | Унарный минус | -a | -a | a- |

      >Обрати внимание, что оператор умножения содержит обязательный знак `*`. Обработка выражения с опущенным знаком `*` является необязательной и остается на усмотрение разработчика.

    - **Функции**:

      | Описание функции | Функция |   
      | ---------------- | ------- |  
      | Вычисляет косинус | cos(x) |   
      | Вычисляет синус | sin(x) |  
      | Вычисляет тангенс | tan(x) |  
      | Вычисляет арккосинус | acos(x) | 
      | Вычисляет арксинус | asin(x) | 
      | Вычисляет арктангенс | atan(x) |
      | Вычисляет квадратный корень | sqrt(x) |
      | Вычисляет натуральный логарифм | ln(x) | 
      | Вычисляет десятичный логарифм | log(x) |

